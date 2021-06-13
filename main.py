arr = [[0,0,0,0,0,0,0,0,0,0] for i in range(11)]
r = c = 0
print("SIMULATION OF NFA")
print(":(((((((((((())))))))))))):")
for i in range(10):
    for j in range(10):
        arr[i][j] = ''
exp = input("Enter the regular expression: ")
length = len(exp)
for i in range(length-1):
    if exp[i]=='|':
        arr[r][r+1] = 'E'
        arr[r+1][r+2] = exp[i-1]
        arr[r+2][r+5] = 'E'
        arr[r][r+3] = 'E'
        arr[r+4][r+5] = 'E'
        arr[r+3][r+4] = exp[i+1]
        r = r+5
    elif exp[i]=='*':
        arr[r-1][r] = 'E'
        arr[r][r+1] = 'E'
        arr[r][r+3] = 'E'
        arr[r+1][r+2] = exp[i-1]
        arr[r+2][r+1] = 'E'
        arr[r+2][r+3] = 'E'
        r = r+3
    elif exp[i]=='+':
        arr[r][r+1] = exp[i-1]
        arr[r+1][r] = 'E'
        r = r+1
    if c==0:
        if exp[i].isalpha() and exp[i+1].isalpha():
            arr[r][r+1] = exp[i]
            arr[r+1][r+2] = exp[i+1]
            r=r+2
            c = 1
        c=1
    elif c==1:
        if exp[i+1].isalpha():
            arr[r][r+1] = exp[i+1]
            r = r+1
            c=2
    else:
        if exp[i+1].isalpha():
            arr[r][r+1] = exp[i+1]
            r=r+1
            c=3
for j in range(r+1):
    print(j,end = ' ')
print()
print("_____________")
for i in range(r+1):
    for j in range(r+1):
        print('',arr[i][j],end = ' ')
    print(" |{}".format(i))
print("Final state: {}".format(i))
