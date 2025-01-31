median = 0
i = 0 
j = 0
def maximum(a,b):
    return a if a > b else b
def minimum (a,b):
    return a if a < b else b 
def findmedianStortedArrays(a,n,b,m):
    if n==0:
        if m% 2 == 0:
            return (b[m/2]+b[(m/2)+1])/2
        else:
            return b[int(m/2)]
    elif m==0:
        if n%2==0:
            return (a[n/2]+a[n/2]+1)
        else:
            return a[int(n/2)]
    global median, i, j 
    min_index = 0 
    max_index = n
    while (min_index <= max_index):
        i = int((min_index +max_index)/2)
        j = int(((n+m+1)/2)-i)
        if (i <n and j >0 and  b[j-1]>a[i]):
            min_index = i+1
        elif i >0 and j<m and b[j] < a[i-1]:
            max_index = i -1 
        else:
            if (i==0):
                median = b[j-1]
            elif (j==0):
                median = a[i-1]
            else:
                median = maximum(a[i-1], b[j-1])
            break
    if ((n + m) %2 ==1):
        return median
    if i ==n:
        return (median+b[j])/2.0
    if j == m :
        return (median + a[i])/2.0
    return (median+minimum(a[i],b[j]))/2.0



a =[1,3]
b =[2]
n = len(a)
m = len(b)
if n<m:
    print(findmedianStortedArrays(a,n,b,m))
else:
    print(findmedianStortedArrays(b,m,a,n))
