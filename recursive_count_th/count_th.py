'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):
    global count

    if len(word) < 1:
       return 0

    left, right = word[:len(word)//2], word[len(word)//2 if len(word)%2 == 0 else ((len(word)//2)+1) - 1:]

    if left.endswith('t') and right.startswith('h'):
        count += 0.5
    elif left == 'th':
        count += 1
    elif len(left) == 1:
        return
    else:
        count_th(left)

    if left.endswith('t') and right.startswith('h'):
        count += 0.5  
    elif right == 'th':
        count += 1
    elif len(right) == 1:
        return  
    else:
        count_th(right)

    print(int(count)) 
    return count



test_word = "THtHThth"

count_th(test_word)
