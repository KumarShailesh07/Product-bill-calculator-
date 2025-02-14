# Product Bill Calculator 
print('------Welcome to the Product Bill Calculator------')
price_input = input('Enter the price seperated by commas : ')

product_price = price_input.split(',')
print(product_price)

final_bill = 0
for price in product_price :
    final_bill = final_bill + float(price)

print('Final_Bill :', final_bill)
print(f'Please pay {final_bill} at the counter')