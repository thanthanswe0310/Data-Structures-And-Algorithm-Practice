# Store apple's stock price for 5 days and answer,
# 1. What was the price on day 1?
# 2. What was the price on day 2?

# stock_prices = [298,305,320, 301, 292]

# stock_prices[0] <- 298 <- price on day 1
# stock_price[2] <- 320 <- price on day 3

# Scenario 1: What was the price on day 3?

stock_prices = [1,2,3,2]
for i in range(len(stock_prices)):
    if stock_prices[i] == 301:
        print(i)  # O(n)

# Insertion element is O(n)

# Deletion element at index => O(n) --> stock_prices.remove(1)

# In python, list is implemented as dynamic array

stock_prices = [2,3,5,6]

stock_names = ["AAPL","IBM","TATA"]

stock_prices = [
    [2,3,4,5],
    [40,30,43,44],
    [78,89,71,66]
]

# Exercise: Array Datastructure

# 1. Let us say your expense for every month are listed below:

# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
 
monthly_expenses = [2200, 2350,2600,2130, 2190]
                    

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb, how many dollars you spent extra compare to January? ", monthly_expenses[1]-monthly_expenses[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
print("2. Find out your total expense in first quarter (first three months) of the year.: ", monthly_expenses[0]+monthly_expenses[1]+monthly_expenses[3])

# 3. Find out if you spent exactly 2000 dollars in any month
print("3. Find out if you spent exactly 2000 dollars in any month : ",2000 - monthly_expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list : ",monthly_expenses.append(1980))

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
print("5. ", monthly_expenses[3] - 200)

### Question 2: You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# Add 'black panther' at the end of this list
print(heros.append("black panther"))

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

print(heros.remove('black panther'))
print(heros.insert(3,'black panther'))
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3] = ['doctor strange']
print(heros)


# 5. Sort the list in alphabetical order
heros.sort()
print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
odd_num =[]
max =int(input("Enter max number : "))

odd_num = []

for i in range(1, max):
    if i%2 ==0:
        odd_num.append(i)

print("Odd numbers: ", odd_num)

