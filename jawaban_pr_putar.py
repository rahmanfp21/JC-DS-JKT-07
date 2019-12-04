# #Fungsi Jumlah Kata
# def jumlah_kata(string):
#     kata = {}
#     for word in string.lower().split():
#         if word in kata.keys():
#             kata[word] += 1
#         else:
#             kata[word] = 1
#     for keys, val in kata.items():
#         print("Jumlah kata '{}' ada sebanyak {}".format(keys.capitalize(), val))        

# tampung = {}
# kata = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# for word in kata.lower().split():
#     print(tampung)
#     print(tampung.keys())
#     if word in tampung.keys():
#         tampung[word] += 1
#     else:
#         tampung[word] = 1

# jumlah_kata(kata)

# contoh = ['Apel', 'Mangga']

# print('Apel' in  contoh)
# print('Kuda' in contoh)














import random

# Generate_x*y_angka
def number_generate(x):
    number = []
    pilihan = int(input('Pilih\n1.Angka urut\n2.Angka random\nMasukkan pilihan: '))
    if pilihan == 1:
        for i in range(x):
            temp_number =[]
            for j in range(x):
                temp_number.append((j+1)+(i*x))
                # temp_number awalnya [1,2,3,4] karena j awalnya 0 sampai 3 dan i awalany 0
                # temp_number setelah itu [5,6,7,8] karena i sekarang 1 tapi j tetap 0 sampai 3
            number.append(temp_number)
    elif pilihan == 2:            
        for i in range(x):
            temp_number = []
            for j in range(x):
                temp_number.append(random.randint(1,101))
            number.append(temp_number)   
    return number
# [[1,2,3,4], [5,6,7,8], [9,10, 11, 12], [13,14,15,16]]


# Print_angka
def print_angka(angka):
    for i in angka:
        # i ini isinya diawal adalah [1,2,3,4]
        z = ''
        for j in (range(len(angka))):
            # len angka semisal 4, berarti range 4 menghasilkan 0,1,2,3
            z += str(i[j])
            z += ' '
        print(z)

#Memutar
def putarputar():
    ukuran = int(input('Masukkan ukuran: '))
    angka = number_generate(ukuran)
    print_angka(angka)
    putar = input('Putar ke arah?: ')
    kali = int(input('Putar berapa kali: '))
    if putar == 'Kanan' or putar == 'kanan':
        for c in range(kali):
            list_kanan = []
            for i in range(len(angka)):
                # misal kita punya [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
                list_temp =[]
                for j in range((len(angka)-1),-1,-1):
                    list_temp.append(angka[j][i])
                list_kanan.append(list_temp)
            angka = list_kanan            
    elif putar == 'Kiri' or putar == 'kiri':
        for c in range(kali):
            list_kiri = []
            for i in range((len(angka)-1),-1,-1):
                list_temp =[]
                for j in range((len(angka))):
                    list_temp.append(angka[j][i])
                list_kiri.append(list_temp)    
            angka = list_kiri
    print_angka(angka)
                
while(True):
    angka = []
    putarputar()
    exit = input('Coba lagi [y/n]: ')
    if exit == 'y':
        True
    elif exit == 'n':
        print('Terima kasih')
        break    

