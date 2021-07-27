from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd



def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
             .encode('ascii', 'ignore')\
             .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string




def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string



def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string



def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))
    # Split words in string.
    words = string.split()
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords





def prep_article_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['stemmed'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['lemmatized'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df[['title', column,'clean', 'stemmed', 'lemmatized']]











def convert_date_format(target):
    '''
    This function takes in a pandas Series. It creates an empty pandas DataFrame. Creates a column of the original input_date that is in MM/DD/YY format. It then converts that format to YYYY-MM-DD and returns a 'converted_date' column. This new column is then converted to datetime. Finally, the entire DataFrame is returned with the original input date, and the converted datetime format as well.
    '''
    # Create a blank dataframe
    df = pd.DataFrame()
    # assign the target variable list to a column in the df
    df['input_date'] = target
    # create the regexp to compile the sections of the phone numbers
    date_regexp = r'(\d+)/(\d+)/(\d+)'
    # create output format
    output = r'20\3-\1-\2'
    # create new column of converted dates
    df['converted_date'] = [re.sub(date_regexp, output, i) for i in target]
    # convert to datetime
    df['converted_date'] = pd.to_datetime(df['converted_date'])
    return df



def extract_lines(target):
    '''
    This function takes in a string of logfiles. It creates an empty pandas DataFrame. 
    Creates an 'input_line' column that splits the original string by line, and returns the original input.
    Finally, it extracts the following sections of the original line, and returns a new column for each:
    - method
    - path
    - timestamp
    - status
    - bytes_sent
    - user_agent
    - ip
    '''
    # (?P<method>[A-Z]+) = begins with 1 or more cap letters, stored as 'method'
    # \s = separated by whitespace
    # (?P<path>.*) = 'path' could be any character(s) of any length
    # \s = separated by whitespace
    # [(?P<timestamp>.*)\] = 'timestamp' beginning/ending with literal [] with zero or more of any character type
    # HTTP/1.1 = literall HTTP/1.1
    # \s = separated by whitespace
    # {(?P<status>\d+)} = 'status' of 1 or more non-digit characters, beginning and ending with {}
    # \s = separated by whitespace
    # (?P<bytes_sent>\d+) = 'bytes_sent' of 1 or more digit characters
    # \s = separated by whitespace
    # "(?P<user_agent>.*)" = 'user_agent' inside "" of any character(s) zero or more times, beginning and ending with ""
    # \s = separated by whitespace 1 or more times
    # (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) = 'ip' of 1 to 3 digits, '.' 4x
    regexp = r'''
(?P<method>[A-Z]+)
\s
(?P<path>.*)
\s
\[(?P<timestamp>.*)\]
\s
HTTP/1.1
\s
{(?P<status>\d+)}
\s
(?P<bytes_sent>\d+)
\s
"(?P<user_agent>.*)"
\s+
(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
'''
    # compiles the VERBOSE regexp
    regexp = re.compile(regexp, re.VERBOSE)
    # creates empty pandas DataFrame
    df = pd.DataFrame()
    # creates 'input_line' column of original data
    df['input_line'] = lines.strip().split('\n')
    # concatenates 'input_line' and the extracted regexp data
    df = pd.concat([df, df['input_line'].str.extract(regexp)], axis=1)
    return df





