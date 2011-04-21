a = """The Anti-Zen of Python, by Daniel Greenfeld

Ugly is better than beautiful.
Implicit is better than explicit.
Complicated is better than complex.
Complex is better than simple.
Nested is better than flat.
Dense is better than sparse.
Line code counts.
Special cases are special enough to break the rules.
Although purity beats practicality.
Errors should always pass silently.
Spelchek iz fur loosers.
In the face of explicity, succumb to the temptation to guess.
There should be many ways to do it.
Because only a tiny minority of us are Dutch.
Later is the best time to fix something. 
If the implementation is hard to explain, it's a good sell.
If the implementation is easy to explain, it won't take enough time to do.
Namespaces are too hard, just use import *!"""
b = a.splitlines() # Lines that are split are more liney
c = lambda d: d.strip() # I make sure that lines don't have akksesive whitespace EOLs.
for e in (f for f in b if True): # place here a list generator for aggressive performance enhancementification
    while True: # main loop
        if not False:
            print(c(e))
        else:
            print("Not found here") # let the customer know if there is a failed boolean
        break