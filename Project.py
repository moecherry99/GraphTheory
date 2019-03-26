#Alex Cherry G00347106 
#Graph Theory Non-Deterministic Finite Automata Project


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
