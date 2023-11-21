# Expansioner
*Get Expansions for any string from all of the words in the english dictionary in Python!*

## How does it work?
Expansioner utilizes 460,000 words in the english dictionary ([Credit to DWYL for the list of words](https://github.com/dwyl/english-words)) to be able to filter out the individual letters as words in the sentence and then returns the words that are randomly picked that match the letters in the sentence and then returns all the words into a string for easy use.

## How to use it?

First, you would want to download the list of words (from here)[https://github.com/dwyl/english-words/raw/master/words_alpha.txt] and then put it in the same directory as the Python script. Then you would want to import the script utilizing ``from expansioner import get_expansion`` and then you would want to utilize the "get_expansion" function like below.

```python
from expansioner import get_expansion

get_expansion("Hi")
# Can return any 2 words from the letters "H" and "i", but for me, it returned "happing inclemently".
```

## Final Considerations
Overall, this was a very fun project, but it still contains offensive language inside of the dictionary that would take a lot of time to remove. If you want to use this for a project in a commercial setting, I would recommend removing the offensive language from the dictionary.

## Credits
- [DWYL](https://github.com/dwyl/english-words) for the list of words
