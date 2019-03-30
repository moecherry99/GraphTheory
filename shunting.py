# Alex Cherry - G00347106
# Shunting Yard Algorithm

def shunting(infix):

  specials = {'*': 50, '.': 40, '|': 30}

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

print(shunting("(a.b)|(c*.d)"))
