# Ex11 from LPyTHW - Asking Questions

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?", # ',' for the same line
weigh = raw_input() # raw_input() provides string

print "So, you're %r old, %r tall and %r heavy." % (
        age, height, weigh
        )
