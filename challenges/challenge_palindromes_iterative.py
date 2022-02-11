def is_palindrome_iterative(word):
    if not word:
        return False
    return word == word[::-1]

# https://stackoverflow.com/questions/40580558/why-is-word-word-1-to-test-for-palindrome-faster-than-a-more-algorithmi
# https://stackoverflow.com/questions/509211/understanding-slice-notation
