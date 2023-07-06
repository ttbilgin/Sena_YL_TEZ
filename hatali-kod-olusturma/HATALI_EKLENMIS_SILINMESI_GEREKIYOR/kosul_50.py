age = input('Enter your age:')
your_age = int(age)
if your_age < 5:
ticket_price = 5
elif your_age < 16:
in
ticket_price = 10
else:
ticket_price = 18
print(f"You'll pay ${ticket_price} for the ticket")