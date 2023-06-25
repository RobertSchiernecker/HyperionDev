import math


#printed statements to explain what this is
#the user will choose whether they want to calculate an investment or a bond which if have created by using if-else statement
#the user will then enter the interest rate the deposit they want to put down and the smount of years the investment is over
# the interest rate is divided by 100 to give 'r' a value for the future sums.
#use of .lower() so the input is not case sensitive



investment = print("investment - to calculate the amount of interest you'll earn on your investment ")
bond = print("bond - to calculate the amount of interest you'll have to pay on a home loan ")




choice = input("Enter either investment or bond to proceed :\n> ").lower()



if choice == "investment":
    interest_rate = float(input("please now enter the interest rate percentage as number and decimal only "))
    deposit = int(input("please enter the deposit amount as number only "))
    years = int(input("the amount of time in years you want to invest over "))
    r = interest_rate/100
    
    
    print("now please choose which type of investment you want to calculate")


#if they choose investment they will then have to choose either simple interest or compound interest plan
#to create more optons within the first option i started another if-else statement within the first one by indenting the line further
#use of .lower() so the input isnt case sensitive
    
    investment_choice = input("please enter 'simple' for simple interest plan or 'compound' for a compound interest plan :\n>").lower()

   
   
    if investment_choice == "simple":

    #this section is activated if they select simple and this is the sum to work out returns on a simple plan
    
        print(f" you will return £{deposit * (1 + r * years)} from your simple investment")
    
    
   
   
    elif investment_choice == "compound":    
    
    #this is activated if the user selects compound plan and the sum to work out the returns for this below
    
        print(f"you will return £{deposit * math.pow((1 + r),years)} from your compound investment")
        



elif choice == "bond":
    
    #if the user selects bond this choice will activate asking for the user to input the value of their house, the interest rate and how many months they will pay over
    #the interest rate is divided by 100 and then again by 12 to get the monthly amount.
    
    
    value = float(input("please type in the value of your house in numbers and decimals, if applicable "))
    interest_rate2 = float(input("please type in the annual interest rate in numbers and decimals "))
    months1 = int(input("please enter the amount of months the bond will be repaid over "))
    i = (interest_rate2/100) / 12
    
    repayment = (i * value)/(1 - (1 + i) ** (-months1))
    print(f" you will pay £{repayment} monthly over {months1} months" )
    
else:
    print("you have not entered a required option")
    
#if the user types in anything other than investment or bond then this message will appear.

