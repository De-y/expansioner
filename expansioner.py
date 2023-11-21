from random import choice

def get_expansion(string:str):
    """
    Get expansions of a string from all of the words in the english dictionary (Doesn't work with symbols or numbers).
    """
    words_relating_to_string = []
    for words in list(string):
        word_filtered_bank =  []
        l = open('words.txt','r+')
        for word in l:
            if words == word[0]:
                word_list = word.split('\n')
                word_filtered_bank.append(word_list[0])
        words_relating_to_string.append(choice(word_filtered_bank))
    return ' '.join(words_relating_to_string)
