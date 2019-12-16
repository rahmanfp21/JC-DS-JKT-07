# def backwardsPrime(start, stop):

#     def prime_num(num):    
#         prime_tab = []
#         for i in range(2,num+1):
#             if num % i == 0:
#                 prime_tab.append(True)
#         if sum(prime_tab) == 1:
#             return True
#         else:
#             return False 
#     check_prime = []
#     backward_prime = []
    
#     for prime in range(start, stop+1):
#         if prime_num(prime):
#             check_prime.append(prime)        

#     for j in check_prime:
#         if prime_num(int(str(j)[::-1])) and j > 11:
#             backward_prime.append(j)

#     return backward_prime        


# print(backwardsPrime(2,100))
# print(backwardsPrime(9900,10000))
# print(backwardsPrime(501,599))

# highest_xnum

# def get_highest_xnum(num, sequence):
#    from math import floor,pow

#    if num < pow(10,sequence) or sequence >5:
#       print('Input valid num or sequence')
#    else:
#       angka = []
#       while (num > 0):
#          angka.append(num%10)   
#          num = floor(num/10)
#       highest = 0
#       for idx in range(len(angka)-1,sequence-2,-1):
#          test = ''
#          for i in range(sequence):
#             test += str(angka[idx-i])   
#          if int(test) > highest:
#             highest = int(test)
#       print('The highest {}-number is {}'.format(sequence,highest))
      
# get_highest_xnum(81919173, 4)


#ay_word

# def ay_word(text):
#     new_text = []
#     for i in text.split():
#         new_text.append(i[1:]+i[0]+'ay')

#     return ' '.join(new_text)    

# print(ay_word('Pig Latin is Cool'))    