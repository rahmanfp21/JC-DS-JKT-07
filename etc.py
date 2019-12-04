# t = (1, [0, 'test'], {'a1':True})
# print(type(t))
# print(t[1])
# print(t[2]['a1'])
# print(t[1][1])
# t[1][1] = 'akan'
# print(t[1][1])
# t[1] = 'mark'
# print(t[1])

# s = {1,3,1,2,2,3, 'a', 'a', True, True, 'b', 1.4, 1.4}
# print(s)
# print(type(s))
# print(set(list(s)))

# kata = 'Aku baru mau makan tapi makan apa aku baru mau'
# print(set(kata.split()))

# def times2(num):
#     num = num*2
#     for i in range(num):
#         num = num ** i
#     return num * 2

# listNum = [1,2,3,4,5]
# listNum = [times2(item) for item in listNum]

# print(listNum)

# print('Without Lambda')
# def times2(num):
#     return num *2
# listNum = [1,2,3,4,5]
# listNum = list(map(times2, listNum))
# print(listNum)

# print('With Lambda')
# listNum = [1,2,3,4,5]
# listNum = list(map(lambda num: num *2 if num ==2 else num/2, listNum))
# print(listNum)

# def genap(num):
#     return num % 2 == 0

# print('Without Lambda')
# listNum = [1,2,3,4,5]
# listNum = list(filter(genap, listNum))
# print(listNum)    

# print('With Lambda')
# listNum = {'Ini string': 'not string'}
# listNum = list(filter(lambda num: len(num) < 20, listNum))
# print(listNum)

num = [1,2,3]
input = 'ku'

print(input in num)
print(input in ['x', 'y', 'z'])
print(input in 'kurakas')

func = lambda num: num *2
print(func(2))