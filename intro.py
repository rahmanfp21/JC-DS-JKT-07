# print('halo')

# Ini fungsi print, yang dipakai untuk mencetak 
# atau memunculkan apapun yang dimasukkan kedalam fungsi tersebut kedalam layar

# nama = 'Nama Saya Cornellius'
# umur = 26
# pekerjaan = 'Guru'

# nama = input('What is your name: ')

# a = 'My name is' + 'Cornellius'
# print(a)
# print('Pekerjaan')
# print(pekerjaan)

# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaAndi ** usiaBudi)
# print(usiaAndi // usiaBudi)


## gunakan fungsi str() untuk merubah tipe data yang tadinya semisal numerical menjadi string
# print('Usia saya' + str(26))
## gunakan fungsi int()untuk merubah tipe data menjadi integer dan float()
#  untuk menjadi tipe data float
# print(10 + float('2'))

# # Cara 1, inputan tetap string tapi di dalam printan dijadikan integer baru jadi string lagi
# nama = input('Masukkan Nama: ')
# umur = input('Masukkan Umur: ')
# print('Umur saya 5 tahun kedepan adalah: ' + str(int(umur)+5))
# print('Umur saya jika di modulus 2 adalah: ' +str(int(umur)%2))

# # Cara 2, inputan dijadikan Integer terlebih dahulu
# nama = input('Masukkan Nama: ')
# umur = int(input('Masukkan Umur: '))
# print('Umur saya 5 tahun kedepan adalah: ' +str(umur+5))
# print('Umur saya jika di modulus 2 adalah: ' +str(umur%2))
# usiaAndi = '40'
# usiaBudi = 20

# Variable apapun bisa ditimpa, bahkan oleh variablenya sendiri yang sudah diutak-atik
# usiaAndi *= 3
# usiaAndi = usiaAndi + 3
# usiaBudi *= 4

# print(usiaAndi)
# print(type(usiaAndi))
# print(usiaBudi)

# from math import pi, fabs, pow, sqrt, floor, ceil

# print(pi)
# print(fabs(-4.7))
# print(pow(8,2))
# print(sqrt(144))

## Memakai round hati-hati, karena jika pada saat .5 jika angka depannya ganjil 
# dia akan membulatkan ke atas sedangkan jika genap dia akan membulatkan kebawah. 
# Round juga dapat menerima parameter tambahan untuk memastikan berapa angka desimal dibelakang koma


# print(round(5.5741251, 2))
# print(int(5.5654))
# print(round(4.4))

# Floor berfungsi untuk membulatkan kebawah sedangkan ceil befungsi untuk membulatkan keatas
# print(floor(4.7))
# print(ceil(4.4))


# x = 'Halo Dunia lain '
# print(len(x))
# print(x.index('a'))
# print(x.split('a'))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())
# print(x.replace('Dunia', 'Apa'))

# Kita bisa memakai 3 petik jika ingin menuliskan string yang panjang dengan line yang berbeda

# a  = """Saya sedang makan 
#         nasi"""

## Kita juga bisa melakukan index terbalik dengan cara menggunakan angka negatif di dalam index
# text = "I'm Baron Nice to meet you"
# print(text[-1:-4])
# print(text[-4:-1])

# print(text[2:])
# print(text[:6])
# print(text[2:5])
# print(text[:])

## Soal latihan
nama = input('Masukkan Nama: ')
umur = int(input('Masukkan Umur: '))

print('Nama saya jika dimunculkan 2x: '+ nama*2 )

print('Karakter di nama saya pada posisi modulus 2 umur saya: ' + nama[umur%2])

print("""Karakter di nama saya pada posisi negatif modulus 2 umur saya lalu 
        ditambah 5 hingga sebelum -1 adalah """ + nama[ (-1*(umur%2))-5 : -1])

