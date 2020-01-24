#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This function contains a while loop which means the `n` will have to be iterated over once, so the function is O(n). More precisely, n is multiplied 3 times (n * n * n) so it could be defined at O(3n) but for simplicity, mostly it'll be described as O(n).


b)
This function has a while loop nested inside a for loop, which means that for each increment on `n`, the amount of times it will be iterated over will increase exponentially by a a factor a 2, so the time complexity could be described as O(n^2).

c)
The function calls itself recursively once, therefore we can take the formula O(b^n) * n where b = the number of times the function is called recursively inside the function, in our case once (1). Therefore we could write the time complexity as O(1^n) * n or since anything to the power of 1 is 1, O(1) * n and finally arriving to the end: 

O(n) as the recursive function will run linearly and the function will run in constant relation to the input n.

## Exercise II

I would structure this problem so that we iterate through the array of n-floors and comparing each floor to f (the floor off of which an egg will break.) Before writing the for loop, I would instantiate a counter at 1 (for the first floor). In my for loop I would check if n floor equals f, if it doesn't, I would add 1 to the counter and go to the next floor to compare. If it does, I would return the value of the counter, as the counter value (floor) will match the number on which f is located. 

Since we would be iterating over n once, the time complexity would be O(n)

Code:

def egg_break(n):

    counter = 1

    for i in n:
        if i != f:
            counter += 1
        else:
            return counter
