#ex1
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = list(zip(l1, l2))
print(l)

#ex2
from itertools import zip_longest
numbers=[1,2,3,4,5,6,7,8]
letters=['a','b','c','d','e','f','g','h']
longest=range(1,9)
zipped=zip_longest(numbers,letters,longest,fillvalue='?')
l=list (zipped)
print(l)

#ex3
a=[6,8,5,7,2,3,4,1]
a.sort()
print(a)

#ex4
numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False

evenNums = filter(even_numbers, numbers)
print('Even Numbers are:')
for num in evenNums:
    print(num)
