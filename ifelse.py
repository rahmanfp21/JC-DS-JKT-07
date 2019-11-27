# x = 5
# y = '5'
# z = 6

# print(x == int(y) and int(y)<z)
# print(x == int(y) or int(y)>z)
# print(not(x == int(y) and int(y)>z))

# nilai = int(input('Masukkan Nilai: '))

# if (nilai > 80):
#     print('Excellent')
# elif (nilai >= 60 and nilai <= 80 ):
#     print('Good Job')
# else:
#     print("Don't Give up")    
#     if nilai == 40:
#         print('Try again')
#     else:
#         print(nilai * 2)    


#Soal 1
# angka = int(input('Masukkan angka: '))
# if (angka%2 == 0 ):
#     print('Angka {} tergolong bilangan GENAP!'.format(angka))
# else:
#     print('Angka {} tergolong bilangan GANJIL!'.format(angka))    


# #Soal 2
# massa = float(input('Masukkan Massa(kg): '))
# tinggi = float(input('Masukkan Tinggi(cm): '))
# tinggi_m = tinggi/100
# imt = massa/(tinggi_m**2)

# imt1 = round(imt, 1)

# if imt1 < 18.5:
#     k= 'BERAT BADAN KURANG!'
# elif (imt1 >= 18.5 and imt1 <= 24.9):
#     k= 'BERAT BADAN IDEAL!'
# elif (imt1 > 24.9 and imt1 <= 29.9):
#     k= 'BB BERLEBIH!'
# elif (imt1 > 29.9 and imt1 <= 39.9):
#     k= 'BB SANGAT BERLEBIH!'
# else: 
#     k= 'OBESITAS'

# print ('Massa {} kg & tinggi {} m'.format(massa, tinggi_m))
# print ('IMT = {}, {}'.format(imt, k))

# nama = input('Masukkan Nama anda: ')
# umur = int(input('Masukkan Umur anda: '))

# if len(nama) > 10 and umur%2 ==1:
#     print('Banyak Rejeki')
# elif len(nama)> 10 and umur%2 == 0:
#     print('Panjang umur')
# elif len(nama) <= 10 and umur%2 ==1:
#     print('Kesehatan baik')
# else:
#     print('Pekerjaan lancar')            
