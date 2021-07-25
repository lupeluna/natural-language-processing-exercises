### Hello,

##### This repository will hold all of my NLP exercies.


#### Regex Data Dictionary

| character             | description                                                 |
| ---------             | -----------                                                 |
| `abcABC123`           | Themselves literally (letters or digits)                    |
| **character classes** |                                                             |
| `.`                   | anything                                                    |
| `\w`                  | letters, numbers, or underscores (opposite is `\W`)         |
| `\d`                  | numbers (opposite is `\D`)                                  |
| `\s`                  | whitespace (opposite is `\S`)                               |
| **repitition**        |                                                             |
| `?`                   | optional                                                    |
| `*`                   | zero or more                                                |
| `+`                   | one or more                                                 |
| `{n}`                 | exacltly `n`                                                |
| `{n,}`                | `n` or more                                                 |
| `{n,m}`               | `n` to `m` times                                            |
| **any/none of**       |                                                             |
| `[abc]`               | `a`, `b`, or `c`                                            |
| `[a-zA-Z]`            | any of abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ|
| `[^abc]`              | anything that's not `a`, `b`, or `c`                        |
|**anchors**            |                                                             |
| `^`                   | starts                                                      |
| `$`                   | end                                                         |
| `\b`                  | word boundary                                               |
| **groups**            |                                                             |
| `(a)`                 | Capture Group (referenced with `\1`)                        |

Anything that's not `a-zA-Z0-9` must be *escaped* to match the character itself
literally.


#### Beautiful Soup Methods and Properties

• soup.title.string gets the page's title (the same text in the browser tab for a page, this is the <title> element
• soup.prettify() is useful to print in case you want to see the HTML
• soup.find_all("a") find all the anchor tags, or whatever argument is specified.
• soup.find("h1") finds the first matching element
• soup.get_text() gets the text from within a matching piece of soup/HTML
• The soup.select() method takes in a CSS selector as a string and returns all matching elements. super useful
