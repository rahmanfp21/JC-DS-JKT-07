# timeConverter

# def timeConverter(seconds):
#     from math import floor
#     if seconds < 0 or seconds > 359999:
#         print('Invalid Input')
#     else:    
#         hour = floor(seconds/3600)
#         minute = floor((seconds%3600)/60)
#         second = floor((seconds%3600)%60)
#         if hour < 10:
#             hour = f'0{hour}'
#         if minute < 10:
#             minute = f'0{minute}'
#         if second < 10:
#             second = f'0{second}'

#         print("'{}:{}:{}'".format(hour,minute,second))

# timeConverter(3600)    
# timeConverter(7201)  







#spinwords
# def spinWords(string):
#     word = []
#     for i in string.split():
#         if len(i) >= 5:
#             reverse = []
#             for idx in range(len(i)-1,-1,-1):
#                 reverse.append(i[idx])
#             word.append(''.join(reverse))
#         else:
#             word.append(i)
#         print(word)    
#     return ' '.join(word)

# print(spinWords('This is not easy but everyone is capable to pass the test'))


#Move Zeros

# def moveZeros(list):
#     new_list = []
#     zero = 0
#     for i in list:
#         if i != 0 or type(i) == type(False) :
#             new_list.append(i)
#         else:
#             zero += 1
#     for i in range(zero):
#         new_list.append(0)

#     return new_list               

# print(moveZeros([False, 1, 0, 1, 2, 0, 1, 3, 'a']))  
# print(moveZeros([0,0,0,"Test",0,3,"a", True, False]))     


#Pagination helper class

from math import ceil
class PaginationHelper:
    def __init__(self, list, page):
        self.book = list
        self.page = page
        self.page_count =  ceil(len(self.book)/self.page)
        self.item_count = len(self.book)
        self.book_list = []
        self.page_dict = {}
        #membuat list dalam list
        for i in range(self.page_count):
            temp = []
            if i == self.page_count - 1:
                if self.item_count % self.page > 0:
                    for j in range(self.item_count % self.page):
                        temp.append(self.book[j + i*self.page])
                else:
                    for l in range(self.page):
                        temp.append(self.book[l + i*self.page])      
            else:    
                for k in range(self.page):
                    temp.append(self.book[k + i*self.page])
            self.book_list.append(temp)
        

        for idx, val in enumerate(self.book_list):
            for idx1 in range(len(val)):
                self.page_dict[idx1 + (self.page * idx )] = idx

        #{key:value} = {index dari item: index dari page}    


    def page_item_count(self, num):
        try:    
            print(len(self.book_list[num]))
        except:
            print(-1)
            
    def page_index(self, num):
        if num > self.item_count or num < 0:
            print(-1)        
        else:
            print(self.page_dict[num])


helper = PaginationHelper('a b c d e f g h'.split(), 4)   
print(helper.page_count)
print(helper.item_count)  
helper.page_item_count(0)
helper.page_item_count(1)
helper.page_item_count(3)  
# helper.page_index(7)    
# helper.page_index(2)
# helper.page_index(20)               
# helper.page_index(-10)    