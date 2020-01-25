'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Recursive algo runs at O(n)

def count_th(word):

    if len(word) <= 1:
        return 0

    word_list = list(word)

    if word_list[0] == 't' and word_list[1] == 'h':
        word_list.pop(0)
        return 1 + count_th(''.join(word_list))
    else:
        word_list.pop(0)
        return 0 + count_th(''.join(word_list))

