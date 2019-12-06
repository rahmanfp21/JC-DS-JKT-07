# #Duplikat Filter
def filterlist(function,list_container):
    hasil = []
    for i in list_container:
        if function(i):
            hasil.append(i)
    return hasil

# #Duplikat Map
def maplist(function,list_container):
    hasil =[]
    for item in list_container:
        hasil.append(function(item))
    return hasil


list_kata=['Merdeka', 'Hello', 'Hellos', 'sohib', 'Kari Ayam']

# print(maplist(lambda x: x.capitalize(), list_kata))
# print(filterlist(lambda x: 'H' in x, list_kata))

from math import floor, pow, sqrt, ceil

def bubblesort(list):
    for k in range(len(list)-1, 0, -1):
        for i in range(k):
            if (list[i] > list[i+1]):
                list[i], list[i+1] = list[i+1], list[i]
    return list

def mean_list(list):
    return sum(list)/len(list)

def median_list(list):
    list = bubblesort(list)
    if len(list)%2 == 0:
        return (list[int(len(list)/2)-1] + list[int((len(list)/2))])/2
    else:
        return list[floor(len(list)/2)]

def mode_list(list):
    ind = set(list)
    counter = {}
    modus = []
    for i in ind:
        z = 0
        for j in list:
            if i == j:
                z += 1
        counter[i] = z
    max_count = max(counter.values())
    for k in counter:
        if counter[k] == max_count:
            modus.append(k)
    if len(modus) == len(set(list)):
        modus = []
    return modus

def variance_list(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 2)
    return z/(len(list)-1)

def stdev_pop(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 2)
    return sqrt(z/(len(list)))    

def skewness(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 3)
    z /= len(list)
    return z/(pow(stdev_pop(list),3))

def kurtosis(list):
    z = 0
    mean =  mean_list(list)
    for i in list:
        z += pow((i - mean), 4)
    z /= len(list)
    return (z/(pow(stdev_pop(list),4)))-3

def statistic_sample(list, type = 'stdev'):
    if type == 'variance':
        return variance_list(list)
    elif type == 'stdev':
        return sqrt(variance_list(list))
    elif type == 'mean':
        return mean_list(list)
    elif type == 'median':
        return median_list(list)
    elif type == 'mode':
        return mode_list(list)
    elif type == 'skewness':
        return skewness(list)
    elif type == 'excess kurtosis':
        return kurtosis(list)
    else:
        return 'Invalid Input'    



list_angka = [1,3,3,3,4,4,2,4]
print(statistic_sample(list_angka, 'excess kurtosis'))


# mean
# median
# mode
# stdev
# variance
# skewness
# excess kurtosis

def sum_triangular_numbers(n):
   if n < 0:
      return 0
   else:    
      number = []
      for i in range(1,n+1):
         number_temp = []
         for j in range(i,i*2):
            if i == 1 or i == 2:
               number_temp.append(j)
            else:
               number_temp.append(j + number[i-3][-1])
               # print(j)
               # print(number[i-3][-1])
               # print(number_temp)
         number.append(number_temp)
      sum_ = 0
      number_print = number.copy()
      z = ''
      for item in number:
         sum_ += item[-1]

      for item in number_print:
         item[-1] = [item[-1]]

      for item in number_print:
         for val in item:
            z+=str(val)
            z+=' '
         z+='\n'
      print(z)        
      return print('sum of each last part of the triangle is {}'.format(sum_))

# sum_triangular_numbers(8)


contoh_list = [1,2,3,4,5]
list_lain = contoh_list.copy()
list_lain[2] = 10191
print(contoh_list)








