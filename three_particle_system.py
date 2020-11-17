'''Three particle system'''
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

def threepart(a,b,c):
    if a == 'd' and b == 'up' and c== 'up':
        print(''' ^\nT|d u d    v e+\nI|^ ^ ^    ^ ^\nM|| | \ W+  \/\nE|| |  ~~~~~~\n || | / \n |d u u\n -------------> SPACE''')
    elif a == 'd' and b == 'd' and c== 'up':
        print(''' ^\nT|d u u    v e-\nI|^ ^ ^    ^ ^\nM|| | \ W-  \/\nE|| |  ~~~~~~\n || | / \n |d u d\n -------------> SPACE''')
    elif a == 'ad' and b == 'aup' and c== 'aup':
        print(''' ^\nT|-d-u-u  -v e+\nI|^ ^ ^    ^ ^\nM|| | \ W-  \/\nE|| |  ~~~~~~\n ||  \ / \n |-d-u-d\n -------------> SPACE''')
    elif a == 'ad' and b == 'ad' and c== 'aup':
        print(''' ^\nT|-d-u-d -v e-\nI|^ ^ ^    ^ ^\nM|| |  \ W+ \/\nE|| |  ~~~~~~\n || |  / \n |-d-u-u\n -------------> SPACE''')
    elif a == 'e' and b == 'e' and c== 'e':
        print(''' ^\nT|e-  e-   e-\nI|^   ^     ^\nM||    \ g /\nE||     ~~~ \n ||    /  \ \n |e-  e-  e-\n -------------> SPACE''')
    elif a == 'e' and b == 'e' and c== 'p':
        print(''' ^\nT|  g     g\nI|  ~     ~  \nM|   ~ e- ~\nE|    ---> \n |   /   \ \n |  e-   e+\n -------------> SPACE''')
    elif a == 'e' and b == 'p' and c== 'p':
        print(''' ^\nT|  g     g\nI|  ~     ~  \nM|   ~ e+~\nE|    <--- \n |   /   \ \n |  e-   e+\n -------------> SPACE''')
    elif a == 'p' and b == 'p' and c== 'p':
        print(''' ^\nT|e+  e+   e+\nI|^   ^     ^\nM||    \ g /\nE||     ~~~ \n ||    /  \ \n |e+  e+  e+\n -------------> SPACE''')
    elif a == 'aup' and b == 'e' and c== 'up':
        print(''' ^\nT| e-  g     g\nI| ^  ~     ~  \nM| |  ~    ~\nE| | ^    ^ \n | |  \/ \n | e-   p0\n -------------> SPACE''')
    elif a == 'aup' and b == 'p' and c== 'up':
        print(''' ^\nT| e+  g     g\nI| ^  ~     ~  \nM| |  ~    ~\nE| | ^    ^ \n | |  \/ \n | e+   p0\n -------------> SPACE''')
    elif a == 'ad' and b == 'd' and c== 'e':
        print(''' ^\nT| e-  g     g\nI| ^  ~     ~  \nM| |  ~    ~\nE| | ^    ^ \n | |  \/ \n | e-   p0\n -------------> SPACE''')
    elif a == 'ad' and b == 'd' and c== 'p':
        print(''' ^\nT| e+  g     g\nI| ^  ~     ~  \nM| |  ~    ~\nE| | ^    ^ \n | |  \/ \n | e+   p0\n -------------> SPACE''')
    elif a == 'aup' and b == 'd' and c== 'e':
        print(''' ^\nT| e-  m+   mn\nI| ^  \    /  \nM| |    W+\nE| |    ~~~ \n | |   /  \ \n | e-  au   d\n -------------> SPACE''')
    elif a == 'aup' and b == 'd' and c== 'p':
        print(''' ^\nT| e+  m+   mn\nI| ^  \    /  \nM| |    W+\nE| |    ~~~ \n | |   /  \ \n | e+  au   d\n -------------> SPACE''')
    elif a == 'ad' and b == 'e' and c== 'up':
        print(''' ^\nT| e-  m+   mn\nI| ^  \    /  \nM| |    W+\nE| |    ~~~ \n | |   /  \ \n | e-  u  ad\n -------------> SPACE''')
    elif a == 'ad' and b == 'p' and c== 'up':
        print(''' ^\nT| e+  m+   mn\nI| ^  \    /  \nM| |    W+\nE| |    ~~~ \n | |   /  \ \n | e+  u  ad\n -------------> SPACE''')


first=str(input(('What is the first particle of your system?\n')))
first = stripq(first)
system.append(first)

second=str(input(('What is the second particle of your system?\n')))
second = stripq(second)
system.append(second)

third=str(input(('What is the third particle of your system?\n')))
third = stripq(third)
system.append(third)

system.sort()

if system == ['d', 'up', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a proton with charge = +1!')
    ask2= str(input('Would you like to see a Feynman Diagram involving a proton?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['d', 'd', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a nutron with charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram involving a nutron?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['ad', 'aup', 'aup']:
    print('Congratulations, this is a valid combination!')
    print('You have created an anti-proton with charge = -1!')
    ask2= str(input('Would you like to see a Feynman Diagram involving an anti-proton?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['ad', 'ad', 'aup']:
    print('Congratulations, this is a valid combination!')
    print('You have created an anti-nutron with charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram involving an anti-nutron?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['e', 'e', 'e']:
    print('Congratulations, this is a valid combination!')
    print('You have created a thee electron system with net charge = -3!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['e', 'e', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a two electron one positron system with net charge = -2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['e', 'p', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a one electron two positron system with net charge = 2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['p', 'p', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a three positron system with net charge = 3!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['aup', 'e', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson electron system with net charge = -1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['aup', 'p', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson positron system with net charge = +1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['ad', 'd', 'e']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson electron system with net charge = -1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['ad', 'd', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a meson positron system with net charge = +1!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['aup', 'd', 'e']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion electron system with net charge = -2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])

elif system == ['aup', 'd', 'p']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion positron system with net charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['ad', 'e', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion electron system with net charge = 0!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
elif system == ['ad', 'p', 'up']:
    print('Congratulations, this is a valid combination!')
    print('You have created a pion positron system with net charge = +2!')
    ask2= str(input('Would you like to see a Feynman Diagram with this system?\n'))
    ask2=stripans(ask2)
    if ask2 == 'y':
        threepart(system[0],system[1], system[2])
    
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
        if (x).is_integer() == False:
            print('This is a net charge of', x, '\nSorry! This is an invalid combination.\n')
            print('Would you like to play again?')
            user_ask2= str(input())
            user_ask2=stripans(user_ask2)
            if user_ask2 == 'y':
                exec(open("three_particle_system.py").read())
            else:
                sys.exit()
        elif (x).is_integer() == True:
            print('This is a net charge of', x, '\nSorry! While this is a whole number charge combonation, a baryon made of three identical quarks is forbidden under the Pauli exclusion principle.\n')
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
        
