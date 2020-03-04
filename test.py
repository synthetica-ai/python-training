from main import HandPowder

k =[1, 2, 2, 5, 8]
a= []
for i in k:
    if i == i+1:
        a.append(2)
        a.append(i)
        k.remove(i)
    a.extend(k)
print(a)


