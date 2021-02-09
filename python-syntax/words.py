
word_list = ['hello','hey','yo','yes','ear','goodbye','zebra']

def print_upper_words(words):
    """Converts every word in a list in uppercase
    Only prints words that start with the letter 'e'"""

    for word in words:
        upper_word = word.upper()
        if upper_word.startswith('E'):
            print(upper_word)

print_upper_words(word_list)


def print_upper_words2(words,must_start_with):
    """Converts every word in a list in uppercase
    Print words with letters provided in must_start_with"""

    for word in words:
        upper_word = word.upper()
        for char in must_start_with:
            if upper_word.startswith(char.upper()):
                print(upper_word)

print_upper_words2(word_list,must_start_with={'z','g'})