#no 1
def generate_hashtag(s):
    z ="#"
    for i in s.split():
        z += i.capitalize()
        
    if len(z) > 140 or z == '#':
        print(False)
    else:
        print(z)
generate_hashtag("Hello there how are you doing")
generate_hashtag("   Hello  world")
generate_hashtag("")








#no 2
def create_phone_number(n):
    try:
        print('({}{}{}) {}{}{}-{}{}{}{}'.format(n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9]))
    except:
        print(False)    
create_phone_number([1,2,3,4,5,6,7,8,9,0])
create_phone_number([1,2,3,4,5,6,7,8,9])





#no 3
def sort_odd_even(num):
    idx_ganjil = []
    val_ganjil = []
    idx_genap = []
    val_genap = []
    hasil = [0 for i in range(len(num))]
    for idx, val in enumerate(num):
        if val % 2 != 0:
            idx_ganjil.append(idx)
            val_ganjil.append(val)
        else:
            idx_genap.append(idx)
            val_genap.append(val)
    # val_ganjil.sort()
    for i in range(len(val_ganjil)):
        for j in range(i+1, len(val_ganjil)):
            if val_ganjil[i] > val_ganjil[j]:
                val_ganjil[i], val_ganjil[j] = val_ganjil[j], val_ganjil[i]
    # val_genap.sort(reverse= True)
    for i in range(len(val_genap)):
        for j in range(i+1, len(val_genap)):
            if val_genap[i] < val_genap[j]:
                val_genap[i], val_genap[j] = val_genap[j], val_genap[i]

    for idx, val in zip(idx_ganjil, val_ganjil):
        hasil[idx] = val
    for idx, val in zip(idx_genap, val_genap):
        hasil[idx] = val
    print(hasil)    

sort_odd_even([5,3,2,8,1,4,77,1,6,0,12])
sort_odd_even([5,3,2,8,1,4])
sort_odd_even([])


#no 4
def hollow_triangle(n):
    if n == 1:
        print("#")
        return False

    atas = ["_" * (n - 1) + "#" + "_" * (n - 1)]
    bawah = ["#" * ((2 * n) - 1)]
    mid = []
    for i in range(n - 2, 0, -1):
        mid.append(("_" * i) + "#" + ("_" * ((2 * n) - (2 * i) - 3)) + "#" + ("_" * i))
    
    print(atas[0])

    for i in mid:
        print(i)

    print(bawah[0])  
    
for i in range(1, 7):
    hollow_triangle(i)        