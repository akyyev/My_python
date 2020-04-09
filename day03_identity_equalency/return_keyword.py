def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return [amount, tax, total_amount]


price = value_added_tax(100)
print(price[1], type(price))

