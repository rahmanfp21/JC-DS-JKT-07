# Dictionary
# Dictionary itu sama kayak list, bisa menampung value apapun. Perbedaanya, indexnya bisa kita 
# tentukan namanya

#nama index di dictionary adalah Key
# Urutan pengisian dictionary adalah nama key: value 
d = {'key1': 'item1', 'key2': 12.5, 'kucing':[3,'Jerapah', True]}

# print(d['key1'])
# print(d['key2'])
# print(d['kucing'])
# print(d['kucing'][1])

# Cara isi dictionary

d[0] = 'Ini angka'
d['key lain'] = 'Ini item'

# # print(d[0])
# print(d['key lain'])

# d['key lain'] = 0

# for i in range(3):
#     d['key lain'] += 1
#     print(d['key lain'])

# print(d)

# Attribute keys() untuk mendapatkan seluruh keys dari dictionary
# print(list(d.keys())[0])

# # Attribute values() untuk mendapatkan seluruh values dari dictionary
# print(d.values())

# Kita bisa looping di dictionary key ataupun values 
# print('Ini looping di key')
# for key in d.keys():
#     print(key)

# print('ini looping di values')
# for value in d.values():
#     print(value)    

# Attribute items() untuk mendapatkan bersamaan seluruh key dan values
# print(d.items())    

# for key, val in d.items():
#     print(key)
#     print(val)

# Jika looping di dictionary, maka yang didapatkan adalah key nya
# for i in d:
#     print(i)

# Fungsi Zip untuk menggabungkan hal yang bisa iterable (bisa di looping) menjadi satu
list_buah = ['Nanas', 'Mangga', 'Apel', 'Jeruk', 'Keledai']

for item in zip(range(2), d, list_buah):
    print(item)

for angka, key, buah in zip(range(2), d, list_buah):
    print(str(angka) + str(key) + buah)
