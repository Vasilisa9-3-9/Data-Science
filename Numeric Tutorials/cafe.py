
#create a list of 4 cafe's products 

menu = ["coffe", "pastry", "fruits", "chips"]

#create a dictionary of stock prices of earlier stated products 

stock_dict = {"coffe": 1.85,
              "pastry": 2.84,
              "fruits": 2.45,
              "chips": 2.75
              }

#create a dictionary of prices of earlier stated peoducts 

price_dict = {"coffe": 3.75,
              "pastry": 4.50,
              "fruits": 4.02,
              "chips": 3.20
              }

#create a loop, calculating a value of each produuct form the "menu" list 
#add each of those value to the earlier created "total" list 

total  = []

for key in stock_dict:

    value = stock_dict[key] * price_dict[key]

    total.append(value)

#using the "sum" function, calculate the total if the values in the "total" list 

final_total = sum(total)

#print out the answer 

print("The total stock worth in the cafe = ", round(final_total, 2))


    
  













