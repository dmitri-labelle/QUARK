'''Two particle system'''
import sys

system=[]

def stripq(c):
    c = c.replace(' ', '')
    c = c.lower()
    c = c.replace('quark','')
    c = c.replace('lepton','')
    c = c.replace('own','')
    c = c.replace('-', '')
    c = c.replace('nti','')
    c = c.replace('ositron','')
    c = c.replace('lectron','')
    return(c)

def stripans(a):
    a = a.replace(' ', '')
    a = a.lower()
    a = a.replace('e','')
    a = a.replace('s','')
    a = a.replace('o','')
    a = a.replace('!', '')
    return(a)

def twopart(a,b):
    if a == 'aup' and b == 'up':
        print(''' ^\nT|  g     g\nI|  ~     ~  \nM|  ~    ~\nE|  ^   ^ \n |   \/ \n |   p0\n -------------> SPACE''')
    elif a == 'aup' and b == 'd':
        print(''' ^\nT|  m+     mn\nI|   \    /  \nM|     W+\nE|    ~~~ \n |   /  \ \n |  au   d\n -------------> SPACE''')
    elif a == 'ad' and b == 'up':
        print(''' ^\nT|  m+     mn\nI|   \    /  \nM|     W+\nE|    ~~~ \n |   /  \ \n |   u   ad\n -------------> SPACE''')
    elif a == 'ad' and b == 'd':
        print(''' ^\nT|  g     g\nI|  ~     ~  \nM|  ~    ~\nE|  ^   ^ \n |   \/ \n |   p0\n -------------> SPACE''')
    elif a == 'e' and b == 'e':
        print(''' ^\nT|e-  e-   e-\nI|^   ^     ^\nM||    \ g /\nE||     ~~~ \n ||    /  \ \n |e-  e-  e-\n -------------> SPACE''')
    elif a == 'p' and b == 'p':
        print(''' ^\nT|e+  e+   e+\nI|^   ^     ^\nM||    \ g /\nE||     ~~~ \n ||    /  \ \n |e+  e+  e+\n -------------> SPACE''')
    elif a == 'e' and b == 'p':
        print(''' ^\nT|  g     g\nI|  ~     ~  \nM|   ~ e- ~\nE|    ---> \n |   /   \ \n |  e-   e+\n -------------> SPACE''')

first=str(input(('What is the first particle of your system?\n')))
first = stripq(first)
system.append(first)

second=str(input(('What is the second particle of your system?\n')))
second = stripq(second)
system.append(second)

system.sort()

if system == ['aup', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson with charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])
    
elif system == ['aup', 'd']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion with charge = -1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])
    
elif system == ['ad', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion with charge = +1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])

elif system == ['ad', 'd']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson with charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])

elif system == ['e', 'e']:
    print('Congratulations, this is a valid combination!')
    print('You have created a two electron system with net charge = -2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])
    
elif system == ['p', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a two positron system with net charge = +2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])
    
elif system == ['e', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a positron-electron system with net charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        twopart(system[0],system[1])
    
else:
    system=[(2/3) if x=='up' else x for x in system]
    system=[(-2/3) if x=='aup' else x for x in system]
    system=[(-1/3) if x=='d' else x for x in system]
    system=[(1/3) if x=='ad' else x for x in system]
    system=[(-1) if x=='e' else x for x in system]
    system=[(1) if x=='p' else x for x in system]
    charge = system
    x= sum(charge)
    while x!= int:
        print('This is a net charge of', x, '\nSorry! This is an invalid combination.\n')
        print('Would you like to play again?')
        user_ask2= str(input())
        user_ask2=stripans(user_ask2)
        if user_ask2 == 'y':
            exec(open("partone.py").read())
        else:
            sys.exit()
            
print('Would you like to play again?')
user_ask2= str(input())
user_ask2=stripans(user_ask2)
if user_ask2 == 'y':
    exec(open("partone.py").read())
else:
    sys.exit()
        