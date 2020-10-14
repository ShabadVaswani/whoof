print('lets play cross and os')#57198264
pbd={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
j=[]
def pb(pbd):
    print(pbd['7']    + pbd['8']    + pbd['9'])
    print(pbd['4']    + pbd['5']    + pbd['6'])
    print(pbd['1'] +    pbd['2']    + pbd['3'])
pb(pbd)
n=0
while n<9:
    xl=input('xtrn')
    if xl in j:
            print('already filled')
            
    else:
            pbd[xl]='X'
            pb(pbd)
            j.append(xl)
            if pbd['7'] == pbd['8'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")                
                    break
            elif pbd['4'] == pbd['5'] == pbd['6'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break
            elif pbd['1'] == pbd['2'] == pbd['3'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break
            elif pbd['1'] == pbd['4'] == pbd['7'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break
            elif pbd['2'] == pbd['5'] == pbd['8'] != ' ':
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break
            elif pbd['3'] == pbd['6'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break 
            elif pbd['7'] == pbd['5'] == pbd['3'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break
            elif pbd['1'] == pbd['5'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'x' + " won. ****")
                    break 
            n=n+1
    if n<9:
        yl=input('otrn')
        if yl in j:
            print('already filled')
            
        else:
            pbd[yl]='O'
            pb(pbd)
            j.append(yl)
            if pbd['7'] == pbd['8'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")                
                    break
            elif pbd['4'] == pbd['5'] == pbd['6'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break
            elif pbd['1'] == pbd['2'] == pbd['3'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break
            elif pbd['1'] == pbd['4'] == pbd['7'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break
            elif pbd['2'] == pbd['5'] == pbd['8'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break
            elif pbd['3'] == pbd['6'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break 
            elif pbd['7'] == pbd['5'] == pbd['3'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break
            elif pbd['1'] == pbd['5'] == pbd['9'] != ' ': 
                    pb(pbd)
                    print("\nGame Over.\n")                
                    print(" **** " +'o' + " won. ****")
                    break 
            n=n+1 
    
print('dn')
