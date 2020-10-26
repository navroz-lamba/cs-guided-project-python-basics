"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    # keep two variables 
    # one tha tracks # of Xs and Os
    xs = 0
    os = 0

    for character in txt:

        if character.lower() == "x":
            xs += 1
        
        if character.lower() == "o":
            os += 1
    
    return xs == os

print(XO("XxOo"))



