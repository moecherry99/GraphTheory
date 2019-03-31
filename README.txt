Graph Theory Project - By Alex Cherry, G00347106.

Aim of this project : Creating a Non-Deterministic Finite Automaton (declared as NFA from now on) from a regular expression 
and using to check if the regular expression matches a given string of text.

---------------------------------------------------

Project run through project.py in folder in VS Code.

1. Go to file path and type in python project.py to run.

This project will take a regular expression from the Shunting Yard Algorithm and
then convert it into postfix notation. This essentially means moving the operands 
and the characters in their required order of precedence (such as BOMDAS). This 
program uses the *, . or | operators. A demo version of the Shunting Yard 
algorithms capabilities is shown at the start of the program to show you how it 
changes these given strings. It then uses Thompsons Construction to show how these 
symbols are dealt with on the Non-Deterministic Finate Automaton.

A class called "nfa" is made with an initial and an accept state. What this 
constructor does is create the nfa in memory and we will then take our string made 
from the Shunting Yard algorithm and then our infix notation (created by this) and 
will show us if the string will end up on an accept state.

The "pofix" (postfix) is our stack and this is the Thompsons Construction algorithm, 
which is the main focus of the project. It deals with our operators and how the 
string that we've given the computer to solve can track where the NFA travels in 
through the program.

Our final class "followes" is basically "Follow the E arrows". These are the arrows 
in our Thompsons Construction NFA that will allow us to proceed to the next state 
if we choose to do so. This way we can have several "initial states" that we are in.

The end of our program is to give the program some infix notations and the strings 
that it must solve. The infix notations are changed to postfix notation by Shunting 
Yard, and then the strings are sent through the Thompsons Construction Algorithm 
and we will get back a "True" or "False" answer. This is basically saying that we 
have either accepted the string or not, if it is on the accept state after the 
string we have entered.


