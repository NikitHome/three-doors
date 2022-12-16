a = int(input())

for i in range(a):
    i = input()
    
    array = list(i)
    
    if array.index('r') < array.index('R') and array.index('g') < array.index('G') and array.index('b') < array.index('B'):
        print('YES')
    else:
        print('NO')
                   