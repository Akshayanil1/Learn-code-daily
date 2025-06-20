# ----- Bio generator -----
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# hometown = input('Enter your hometown: ')

# print(f"""
# Your name is {name}, you are {age} years old, and you come from {hometown}.
# """)

tax_rate = 0.18

price1 = float(input("Enter the price of the first item: "))
price2 = float(input("Enter the price of the second item: "))
price3 = float(input("Enter the price of the third item: "))

subtotal = price1 + price2 + price3

sales_tax_amount = subtotal  * tax_rate

total = subtotal + sales_tax_amount

print(f"""
\n---------- RECEIPT ----------
Subtotal: ${subtotal:>8.2f}
Sales Tax (18%): ${sales_tax_amount:>8.2f}
---------------------------
Total: ${total:>8.2f}
---------------------------
""")