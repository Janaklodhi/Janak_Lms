# # # Encapsulation:
# # # # data and var ko hide karna class ke andar
# # class BankAccount:
# #     def __init__(self, balance):
# #         self.__balance = balance  # Privaate variable

# #     def deposit(self, amount):
# #         self.__balance += amount

# #     def get_balance(self):
# #         return self.__balance  # Access private variable via method

# # acc = BankAccount(1000)
# # acc.deposit(500)

# # print(acc.get_balance())  # 1500
# # print(acc.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

    
# # # this is my custom decorator
# # def my_decorator(func):
# #     def wraper():
# #         print("Something is happening before the function is called.")
# #         func()
# #         print("Something is happening after the function is called")        
# #     return wraper
    
# # @my_decorator
# # def hello():
# #     print("good morninng")
# # hello()


# # import json
# # # this is the dict 
# # data = {

# #     "name": "jannnak", "age": 10, "city": "mumbbai"
# # }
# # parsed = json.dumps(data)
# # json.loads(parsed)
# # print(parsed["name"])

# # def binary_search(array, target):
# #     left = 0
# #     right = len(array)-1
# #     while left < right:
# #         mid = left *(left + right)//2
# #         if mid == target:
# #             return mid
# #         elif mid < target:
# #             left = left+1
# #         else:
# #             right = right-1
# #     return -1
# # array = [10,20,30,40,50]
# # target = 50
# # print(binary_search(array, target)
# # )

# # def find_duplicate(array):
# #     element_count = {}
# #     duplicates = []  #return all the duplicates numbers arrays
# #     for num in array:
# #         if num in element_count:
# #             element_count[num]+=1
# #         else:
# #             element_count[num]=1

# #     for key, value in element_count.items():
# #         if value > 1:
# #             duplicates.append(key)
# #     return duplicates
# # array = [1,2,3,4,5,6,6,7,7,8,9,9]
# # print(find_duplicate(array))


# # def sort01(input_array):
# #     zeros_count = input_array.count(0)
# #     i = 0
# #     while zeros_count:
# #         input_array[i] = 0
# #         zeros_count = zeros_count-1
# #         i=i+1

# #     for i in range(i, len(input_array)-1):
# #         input_array[i] = 1

# # input_array = [0,1,0,1,0,1,0,1]
# # print(sort01(input_array))

# # programs as well we need to master of python
# # orm django

# # cacheing, docker
# # kafka 
# # celery
# # real time chat app 
# # we need to master all these topics 
# # dsa
# # binary search
# # bubble sort
# # linear search
# # opps 
# # # class , object , encapsulation, inheritance, abstraction, polymorphism
# # python 
# # django 
# # DRF 
# # aws 
# # git
# # mysql
# # postgresql 
# # sql 
# # django orm 
# # redis 
# # generator are the itrator
# # def my_gen():
# #     for i in range(1,4):
# #         yield i
# # gen = my_gen()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))



# # decorator
# # generator
# # lambda


# # this is the class and objects
# class Bank():
#     def __init__(self,name, bal):
#         self.name = name
#         self.___bal = bal

#     def show_name(self):
#         return self.name
    
#     def  show_bal(self):
#         return self.bal
# object =  Bank("ICICI", 4000)
# pr

# int(object.show_name())
# object.bal = 500000
# print(object.show_bal())