
#create a list space where the input numbers will be added to 

numbers_list = []

#activate the math mode 

import math

#ask the user for input of 10 integers

for numbers in range(10):
     
     input_numbers = input("Please enter a number, it can be a whole or a deciamal number: ")

#add those integer inputs to the earlier created list space 

     numbers_list.append(input_numbers)

#convert the string list numbers into integer for further use in calculations 

new_numbers_list = [int(numbers) for numbers in numbers_list]

#calculate and print the total of the entered numbers 

total = sum(new_numbers_list)

print("The total of your numbers = ", total)

#identify and print the biggest number out of the users's created list 

maximum_index  = new_numbers_list.index(max(new_numbers_list))

print("The index of the largest number on your list is: ", maximum_index)

#identify and print the smallest number out of the users's created list 

minimum_index = new_numbers_list.index(min(new_numbers_list))

print("The index of the smallest number on your list is: ", minimum_index)

#calculate and print(rounding to two decimal points) the avarge number from the user's list 

avarage = (sum(new_numbers_list)/len(new_numbers_list))

print("The avarage of your list = ", round(avarage), 2)

#sort the user's created list in the ascending order

final_numbers_list = sorted(new_numbers_list)

#identify the integer's index positions 

n = len(new_numbers_list)

#idetify the middle of the index list 

middle_number = int(n / 2)

#if the index list is an even number, create a median calculation with a use of specific number indexes  

if n % 2 == 0:
    
     median = (((final_numbers_list[middle_number-1]) + (final_numbers_list[middle_number])) / 2)

 #print the result 

     print("The median of your list is: ", median)

 #if the index list is odd, idtify a median number through a "middle_number" index usage

else: 
 
     median = (final_numbers_list[middle_number])

 #print the result 

     print("The median of your list is: ", median)











