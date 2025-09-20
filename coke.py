amount_due = 50 # Price of coke
coins_acceptable = [25, 10, 5] # Coins the machine accepts

while(amount_due > 0): # Loop while the client pays
    print('Amount Due:', amount_due)
    coin_inserted = int(input('Insert Coin: '))

    if coin_inserted in coins_acceptable:
        amount_due -= coin_inserted # The amount the user still has to pay

print('Change Owed:', abs(amount_due))
