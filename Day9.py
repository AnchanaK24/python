#ex1
a=lambda x,y: x*y
print(a(3,4))

#ex2
def fibonacci (count):
    list=[0,1]
    any(map(lambda _:list.append(sum(list[-2:])),range(2,count)))
    return list[:count]
print(fibonacci(6))

#ex3
lst=[1,2,3,4,5]
list(map(lambda x:x*2,lst))

#ex4
lst=[6,9,18,24,27,30,58,90]
list(filter(lambda x:x%9==0,lst))

#ex5
lst = [6,9,18,24,27,30,58,90]
lst = list(filter(lambda x:(x%2 ==0),lst))
len(lst)
