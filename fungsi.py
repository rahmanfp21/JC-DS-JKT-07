
# def data(x, y):
#     print(x +' Lahir th. '+ y)
# x = 10
# y = 50

# data('Adi', '1990')
# data(y = '1991', x = 'Charlie')    

# def total(x,y):
#     for i in range(x):
#         if i < 2:
#             print(i)
#         else:
#             print(y)    
#     a = x*y
#     z = x+y
#     return a, z

# print(total(4,5))
# var1, var2 = total(4,5)
# print(var1)
# print(var2)



# def contoh():
#     print(x+y)

# contoh()    

# def namaku(nama):
#     print(nama + ' Susilo')

# namaku('Adi')
# namaku('Budi')

# def kali(x):
#     if x < 2:
#         return 1
#     else:
#         return (x * tiga())

# def tiga():
#     return 3

# print(kali(5))

# def kali(x, y =4):
#     if x < 2:
#         return 1
#     else:
#         return (x/y * tiga())

# def tiga():
#     return 3

# print(kali(4))


# def bagi(x):
#     a, func = kali(5)
    
#     if x < 2:
#         return 1
#     else:
#         return (x / func())


# print(bagi(5))

# mobil = ['Alya', 'Xenia', 'Avanza']
# print(mobil[0])
# print(mobil[1])
# print(mobil[2])
# print(mobil[3])



# print(buah[1:])
# print(buah[:3])
# print(buah[2:5])
# print(buah[:])
# buah[1:3] = 'Kelapa', 'Anggur'
# print(buah)

# buah.extend(['Kelapa', 'Pir'])
# print(buah)

# List Comprehension

# contoh_list = [angka if angka < 3 and angka % 2 else angka * 2 for angka in range (5)]
# print(contoh_list)

# for i in range(5):
#     if i < 3 and i % 2:
#         contoh_list.append(i)

buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga']
# # def something():
# #     return 2

# tugas_buah = [ i[:2] if len(i)> 4 else 'Buah lain' for i in buah ]
# print(tugas_buah)

# Fungsi enumerate untuk mendapatkan index dan value dari list secara langsung
print(enumerate(buah))

for item in enumerate(buah):
    print(item)

for idx, val in enumerate(buah):
    print(idx)
    print(val)    