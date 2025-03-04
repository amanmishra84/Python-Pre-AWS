#!/usr/bin/env python3

sales_data = [
    {
        'product_id': 101,
        'product_name': 'Laptop',
        'quantity_sold': 50,
        'price_per_unit': 750.00
    },
    {
        'product_id': 102,
        'product_name': 'Smartphone',
        'quantity_sold': 150,
        'price_per_unit': 500.00
    },
    {
        'product_id': 103,
        'product_name': 'Headphones',
        'quantity_sold': 200,
        'price_per_unit': 80.00
    },
    {
        'product_id': 104,
        'product_name': 'Keyboard',
        'quantity_sold': 120,
        'price_per_unit': 40.00
    },
    {
        'product_id': 105,
        'product_name': 'Monitor',
        'quantity_sold': 80,
        'price_per_unit': 200.00
    },
    {
        'product_id': 104,
        'product_name': 'Keyboard',
        'quantity_sold': 145,
        'price_per_unit': 40.00
    },
    {
        'product_id': 105,
        'product_name': 'Monitor',
        'quantity_sold': 40,
        'price_per_unit': 150.00
    }

]

#Aggregate and print total sales per product 
result = []
for data in sales_data:
    found = False
    for result_data in result:
        if data['product_id'] == result_data['product_id']:
            result_data['total_sales'] += data['quantity_sold'] * data['price_per_unit']
            result_data['quantity_sold'] += data['quantity_sold']
            found = True
            break
    if not found:
        result.append({
            'product_id': data['product_id'],
            'product_name': data['product_name'],
            'total_sales': data['quantity_sold'] * data['price_per_unit'],
            'quantity_sold': data['quantity_sold']
        })
   
result.sort(key=lambda x: x['total_sales'], reverse=True)
for data in result:
    print(f"Product ID: {data['product_id']}, Product Name: {data['product_name']}, Total Sales: {data['total_sales']}, Quantity Sold: {data['quantity_sold']}")