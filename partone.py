import sys

def stripans(a):
    a = a.replace(' ', '')
    a = a.lower()
    a = a.replace('e','')
    a = a.replace('s','')
    a = a.replace('o','')
    a = a.replace('!', '')
    return(a)

def gamerules():
    print('QUARK is an Edutainment Game helping YOU to learn about the wonderful world of particle physics and Feynman diagrams!')
    print('You can visualize the potential interactions of two or three particle systems.')
    print('Here are the particles you can work with:')
    print('Up Quark Charge: +2/3')
    print('Down Quark Charge: -1/3')
    print('Electron Lepton Charge: -1')
    print('Anti-Up Quark Charge: -2/3')
    print('Anti-Down Quark Charge: +1/3')
    print('Positron Lepton Charge: +1')
    print('You must make sure net charge is a whole number integer.')
    
print( '░█▀▀█ ░█─░█ ─█▀▀█ ░█▀▀█ ░█─▄▀\n░█─░█ ░█─░█ ░█▄▄█ ░█▄▄▀ ░█▀▄─\n─▀▀█▄ ─▀▄▄▀ ░█─░█ ░█─░█ ░█─░█')
print('\nBegin game?')
resp1=str(input(('>Yes         >No\n')))
resp1=stripans(resp1)

if resp1=='n':
  sys.exit()  

resp2=str(input('Would you like to hear the rules? (This is advised)\n'))
resp2=stripans(resp2)

if resp2 == 'y':
    gamerules()
    resp2_1=str(input('Would you like to hear the rules again?\n'))
    resp2_1 = stripans(resp2_1)
    if resp2_1 == 'y':
        gamerules()
        
def numdef(x):
    x = x.replace(' ', '')
    x = x.lower()
    x = x.replace('two','2')
    x = x.replace('three','3')
    x = x.replace('one','1')
    x = x.replace('four','4')
    x = x.replace('five','5')
    x = x.replace('six','6')
    x = x.replace('seven','7')
    x = x.replace('eight','8')
    x = x.replace('nine','9')
    x = x.replace('zero','0')
    x = int(x)
    return(x)

resp3 = str(input('Would you like to play with a two or three particle system? \n'))
resp3 = numdef(resp3)

while (resp3 != 2) and (resp3 != 3):
    print('This is an invalid responce, please try again')
    resp3 = str(input('Would you like to play with a two or three particle system? \n'))
    resp3 = numdef(y)

if resp3 == 2:
    exec(open("two_particle_system.py").read())
    
elif resp3 == 3:
    exec(open("three_particle_system.py").read())
