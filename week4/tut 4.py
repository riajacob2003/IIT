print("Welcome to the Python Coffee Shop!")
 
customer_name = input("What is your name? ")
category = input("student/ other")
print("Hello, " + customer_name + "! Let's order some coffee.")
print(" Are u a student/others," + category )
 
price_coffee = 3.50
price_latte = 4.00
price_mocha = 5.00

     
print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("mocha: $" + str(price_mocha))
 
choice = input("What would you like to order? (coffee/latte/mocha): ")
 
if choice == "coffee":
    cost = price_coffee
elif choice == "latte":
    cost = price_latte
elif choice == "mocha":
    cost = price_mocha
else:
    print("Sorry, we do not have that.")
    cost = 0
 
quantity = int(input("How many cups would you like? "))
 
total_cost = cost * quantity
 
if quantity > 1:
    print("You get a discount of $1.00!")
    total_cost -= 1.00
if category == "student":
    print( " U get a discount of 10% ")
    total_cost -= 0.10

else:
    print ( " Discount only applies for students")
 
print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")

print("Would u like to have another drink")
response = input( "YES/NO")


while response:
    choice = input("What would you like to order? (coffee/latte/mocha): ")
    print (f" you ordered: {choice}")
    
    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        cost = 0

 
    quantity = int(input("How many cups would you like? "))
 
    total_cost = cost * quantity
 
    if quantity > 1:
        print("You get a discount of $1.00!")
        total_cost -= 1.00
    if category == "student":
        print( " U get a discount of 10% ")
        total_cost -= 0.10

    else:
        print ( " Discount only applies for students")
 
    print("Your total is: $" + str(total_cost))
    print("Thank you, " + customer_name + "! Please come again.")

    again = input("Would u like to have another drink (Yes/No):")
    if again == "no":
        print("Thanku for ur order")
        break 

print(sum("468+751"))
