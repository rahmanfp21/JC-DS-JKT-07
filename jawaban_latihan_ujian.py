#Soal Nomor 1

# def calculate_years(principal, interest, tax, desired):
#     year = 0
#     while(principal < desired):
#         principal = principal + ((principal*interest) - ((principal*interest)*tax))
#         year += 1
#     return year  

# print(calculate_years(1200, 0.17, 0.05, 2000))




















#Soal Nomor 2
# def expanded_form(nomor): 
#     from math import floor,pow
#     #semisal nomor =  70304
#     #angka = [4,0,3,0,7]
#     angka = []
#     while(nomor > 0):
#         angka.append(nomor%10)
#         nomor = floor(nomor/10)
#     print(angka)    
#     for idx,val in enumerate(angka):
#         angka[idx] = int(val * pow(10,idx))
#     print(angka)
#     #angka = [4,0,300,0,70000]
#     z =''
#     for idx in range(len(angka)-1,-1,-1):
#         if angka[idx] != 0 and idx != 0:
#             z += str(angka[idx])
#             z += ' + '
#         elif angka[idx] !=0 and idx == 0:
#             z += str(angka[idx])                        
#     print("'"+z+"'")

# expanded_form(70403)





#Soal Nomor 3

def tower_builder(n_floors, block_size) :
    w,h = block_size
    build = []
    
    for i in range (n_floors):     
        for j in range(h):
            z=''
            for k in range (n_floors*2+1):
                if k >= n_floors-i and k <= n_floors+i:
                    z += '*' * w
                else: 
                    z += ' ' * w
            build.append(z)
    print(build)
    for item in build:
        print(item)       

tower_builder(6,(3,2))






