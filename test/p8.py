'''
Problem 8

(20/20 points)
Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here

run_satisfiesF(L, satisfiesF)
For your own testing of satisfiesF, for example, see the following test function f and test code:

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L
Should print:

2
['a', 'a']
Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements. Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function for your code to work correctly.

For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases. If you are getting "Incorrect", first check to make sure you have no indentation errors. For example, make sure the line run_satisfiesF(L, satisfiesF) does not have any spaces before it.
'''

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    for i in range(len(L)):
        if not f(L[i]):
            L[i] = None

    while True:
        try:
            L.remove(None)
        except ValueError:
            break

    return len(L)

run_satisfiesF(L, satisfiesF)
