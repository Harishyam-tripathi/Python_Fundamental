''' continue is a keyword when which get executed executed inside a loop then the loop skip 
the current iteration and jump to the next iteration.'''

for i in range (1,6):
    if i == 3:
        continue
    print(i)


for i in range (1,6):
    for j in range(1,6): 
        if j ==3:
            continue
        print(i,j)   # Jb tak j pura execute nhi hota tb tk (i) 1 hi rahega 
        
        
