#user input number of products and number of days
sales=[]
days=int(input("Enter number of days: "))
products=int(input("Enter number of products: "))
# user input sales data
for i in range(days):
    prod=[]
    for j in range(products):
        s=int(input(f"Enter sales of product {j+1} on day {i+1}: "))
        prod.append(s)
    sales.append(prod)

print(sales)
# sales=[

#     [5,3,0,2],
#     [7,0,2,1],
#     [0,1,4,0]
# ]
# l=len(sales[0])
# # print(l)
# t=[0]*l
# # print(t)
# for i in sales:
#     for j in range(len(i)):
#         t[j]=t[j]+i[j]

# max_v=max(t)
# min_v=min(t)

# print(max_v)
# print(min_v)  
# print(t)  

# for i in range(len(t)):
#     print(f"Total sales of product {i+1} is {t[i]}")
# for i in range(len(t)):
#     if t[i]==max_v:
#         print(f"the product {i+1} has maximum sales of {max_v}")
# for i in range(len(t)):
#     if t[i]==min_v:
#         print(f"the product {i+1} has minimum sales of {min_v}")