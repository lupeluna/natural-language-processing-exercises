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
