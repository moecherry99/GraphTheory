# Alex Cherry G00347106 
# Graph Theory Non-Deterministic Finite Automata Project
# Using Thompsons Construction Algorithm

# Thompsons Construction Tester
# o = not accept, O = accept
# ab.cd.|
#
#
#            a     b
#          o - > o - > o 
#       e /             \ e
# - > o                  O
#       e \             / e
#          o - > o - > o 
#            c     d
#
#



####################################
        # Block 4 of Code
####################################

# Shunting Yard Algorithm here

def shunting(infix):

  specials = {'*': 50, '.': 40, '|': 30}
  # pofix is the output
  pofix = ""

  stack1 = ""

  for c in infix:
    if c == '(':
      stack1 = stack1 + c
    elif c == ')':
      while stack1[-1] != '(':
        pofix, stack1 = pofix + stack1[-1], stack1[:-1]
      stack1 = stack1[:-1]
    elif c in specials:
      while stack1 and specials.get(c, 0) <= specials.get(stack1[-1], 0):
        pofix, stack1 = pofix + stack1[-1], stack1[:-1]
      stack1 = stack1 + c
    else:
      pofix = pofix + c

  while stack1:
    pofix, stack1 = pofix + stack1[-1], stack1[:-1]
        
  return pofix

print("Shunting Yard Conversion : " + shunting("(a.b)|(c*.d)"))

####################################
        # Block 1 of Code
####################################
# This is where we start with our NFA

class state:

  # None is the E state, we don't need a character
  # representation for these as it will move anyway.
  label = None
  edge1 = None
  edge2 = None

# Creating the NFA
class nfa: 
  initial = None # Our start state
  accept = None # Our accept state

####################################
        # Block 2 of Code
####################################

# constructor
  def __init__(self, initial, accept):

  # initialize the variables
    self.initial = initial
    self.accept = accept

  # postfix notation 
def compile(pofix):
  stack=[]

####################################
        # Block 3 of Code
####################################

  # for 
  for char in pofix:
    # if char is one of the following in ifs
    if char == '.':
      # LIFO (stack)
      nfa2 = stack.pop()
      nfa1 = stack.pop()
      # 
      nfa1.accept.edge1 = nfa2.initial

      new = nfa(nfa1.initial, nfa2.accept)
      stack.append(new)

    elif char == '|':
      # pop off stack
      nfa2 = stack.pop()
      nfa1 = stack.pop()

      # new initial state has been made
      initial = state()
      initial.edge1 = nfa1.initial
      initial.edge2 = nfa2.initial
      # instance of state created, it is now a new state
      accept = state()

      nfa1.accept.edge1 = accept
      nfa2.accept.edge1 = accept

      # push new nfa
      new = nfa(initial, accept)
      stack.append(new)

    elif char == '*':
      # remove from stack
      nfa1 = stack.pop()

      # create new initial and accept state
      initial = state()
      accept = state()

      # join new state with old accept state
      initial.edge1 = nfa1.initial
      initial.edge2 = accept

      # join new state with initial state
      nfa1.accept.edge1 = nfa1.initial 
      nfa1.accept.edge2 = accept

      # push on to stack
      new = nfa(initial, accept)
      stack.append(new)
    # elif char =='+':


    else:
    # both will be the current state for now
      accept = state()
      initial = state()
      initial.label = char
      initial.edge1 = accept
      # initial.edge2 = None 

      # creating the nfa and it is the initial and accept
      new = nfa(initial, accept)
      stack.append(new)

  # only 1 nfa per stack
  return stack.pop()

print(compile("ab.cd.|"))

####################################
        # Block 5 of Code
####################################

def followes(state):
  states = set()
  set.add(state)

  # check if state contains e arrows
  if state.label is None:

    states |= followes(state.edge1)

    states |= followes(state.edge2)

    # |= is Union.
  return states

def match(infix, string):

  #compile reg expression
  postfix = shunting(infix)
  nfa = compile(postfix)

  # current/next states
  currentstate = set()
  nextstate = set()

  currentstate |= followes(nfa.initial)

  for s in string:
    for char in currentstate:
      nextstate |= followes(char.edge1)

      # current is now the next
    currentstate = nextstate

    # next is now empty
    nextstate = set()

  return(nfa.accept in currentstate)
# test states
# infixes = []
# strings = []
