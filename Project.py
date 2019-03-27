#Alex Cherry G00347106 
#Graph Theory Non-Deterministic Finite Automata Project
#Using Thompsons Construction Algorithm

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yay! It is Tuesday.")
else:
  print("Unfortunately it is not Tuesday.")



# Thompsons Construction Tester
# o = not accept, O = accept
# ab.cd.|
#            a     b
#          o - > o - > o 
#       e /             \ e
# - > o                  O
#       e \             / e
#          o - > o - > o 
#            c     d
#
#
#

# This is where we start with our NFA
class state:
  label = None
  edge1 = None
  edge2 = None

# Creating the NFA
class nfa: 
  initial = None # Our start state
  accept = None # Our accept state

