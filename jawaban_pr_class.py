# class classy:
#     my_class = 5

# contoh = classy()
# print(contoh.my_class)
# contoh_lain = classy()
# print(contoh_lain.my_class)

class Manusia:
    def __init__(self, nama, umur = 17):
        self.name = nama
        self.age = umur
    
    def salamkenal(self):
        print('Nama saya adalah {} dan saya ber-umur {}'.format(self.name, self.age))

Cornell = Manusia('Cornellius', 26)
# print(Cornell)
# print(Cornell.name)
# print(Cornell.age)
# Cornell.age = 35
# print(Cornell.__dict__)
# Cornell.pekerjaan = 'guru'
# print(Cornell.__dict__)
# print(Cornell.__dict__['name'])        
# Cornell.salamkenal()

# class Anak(Manusia):
#     pass

# anak1 = Anak('Cornellius')
# anak1.salamkenal()

# class anak(Manusia):
#     def __init__(self, name, age, gender):
#         super().__init__(name, age)
#         self.kelamin = gender

#     def salamkenal(self):
#         print('''Nama saya adalah {} dan saya ber-umur {}, serta {}'''.format(self.name, self.age, self.kelamin))  


# Nel = anak('Nel', 26, 'Male')
# Nel.salamkenal()









class BikinMenu:
    def __init__(self, nama, menu, harga, beli =[]):
        self.name = nama
        self.menus = menu
        self.price = harga
        self.history = beli

    def menu_price(self):
       buy = int(input('Mau beli yang mana: '))
       try:
           print('{} telah membeli {} dengan harga {}'.format(self.name, self.menus[buy-1], self.price[buy-1]))
           self.history.append(self.menus[buy-1])
       except:
           print('Invalid input')    
       
    def get_menu(self):      
        print('Menu Makanan\n')
        for idx, val, price in zip(range(len(self.menus)),self.menus, self.price):
            print('{}. {} harganya adalah {}'.format(idx+1, val, price))
        print('\n')
        
    def get_history(self):
        if len(self.history):
            z = '{} telah membeli'.format(self.name)
            if len(self.history) == 1:
                z += ' {}'.format(self.history[0])
                print(z)
            else:
                if len(self.history) == 2:
                        z += ' {} dan {}'.format(self.history[0], self.history[1])

                for idx, val in enumerate(self.history):
                    if len(self.history) == 2:
                        break
                    elif idx == len(self.history) - 1:
                        z += ' dan {}'.format(val)
                    elif idx == len(self.history) - 2:
                        z += ' {}'.format(val)    
                    else:
                        z += ' {},'.format(val)
                print(z)        
        else:
            print('Belum ada pembelian')                        

Paul=BikinMenu('Paul', ['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000, 2000, 3000])

Paul.get_menu()

Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.get_history()

# Paul.menu_price()
# Paul.get_history()
# Paul.menu_price()
# Paul.get_history()
# Paul.menu_price()
# Paul.get_history()