actual_cost= float(input("please enter the actual cost"))
sale_cost= float (input("please enter your sale cost"))

if actual_cost<sale_cost:
    profit= sale_cost-actual_cost
    print("your profit is",profit)
else:
    print("no profit!")    