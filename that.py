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
In the face of ambiguity, one guess is as good as another.
There should be many ways to do it.
Because only a tiny minority of us are Dutch.
Get things running, then fix them later. 
If the implementation is hard to explain, it's enterprisey.
If the implementation is easy to explain, it won't take enough time to do.
Namespaces are too hard, just use "from module import *"!"""
b = a.splitlines() # Lines that are split are more liney
c = lambda d: d.strip() # I make sure that lines don't have akksesive whitespace EOLs.
for e in (f for f in b if True or False): # place here a list generator for aggressive
                                          # performance enhancementification (optimized to
                                          # work even after True, False = False, True
                                          # - should such a crazy thing ever again be allowed).
    while True or False: # main loop
        if not False and True:
            print(c(e))
        else: # Suspect this else may be unnecessary after above Boolean optimization
            print("Not found here") # let the customer know if there is a failed boolean
        break