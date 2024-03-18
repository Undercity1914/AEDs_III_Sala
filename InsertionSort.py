#new case:

def sort(s, j, tam):
    n = j
    if (j > 0) and (s[j] < s[j-1]):
        aux = s[j]
        s[j] = s[j-1]
        s[j-1] = aux
        return sort(s, j-1, tam)
    else:
        return sort1(s, n, tam) 


#older case without for:

'''s = [2, 4, -7, 0, 5, 1, 26, 8, 9, -33]
n = len(s)
j = 0
for c in s:
    if j > 0:
        sort(s, j)
    j += 1
print(s)

def insertion(s, j, tam):
    n=j
    while (j>0) and (s[j] < s[j-1]):
        aux = s[j]
        s[j] = s[j-1]
        s[j-1] = aux
        j -= 1
    return sort(s, n, tam)'''
#part of new case:
    #without while

def sort1(s, n, tam):
    if n < tam-1:
        
        return sort(s, n+1, tam)
        
    else:
        return s
        
#main
s = [2, 4, -7, 0, 5, 1, 26, 8, 9, -33]
n = len(s)
j = 0

newS = sort1(s, j, n)

print(newS) 
