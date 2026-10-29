
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Vo Chi Hung - Harry 
"""
def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    # your code here
    new_amount = amount * float(conversion_rate[from_currency][to_currency])
    return new_amount

_amount = float(input('please enter your amount: '))
print('GBP CNY PHP INR')
f_currency = input('please enter your current currency: ')
t_currency = input('please enter the currency that you want to convert to: ')

x = currency_converter(_amount, f_currency, t_currency)
print(x)

# Submit only this file currency_converter.py with the completed function.
# Remove any additional code you may have added during development and testing.
