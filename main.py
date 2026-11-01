def total_bill(bill_amount, tip_per):
    total = bill_amount + (bill_amount*(tip_per/100))
    rounded_total = round(total, 2)
    print(f"please pay ${total}")
    return total

total_bill(150,20)


def seating_arrangements(guests):
    '''this function calculates the number of seating arrangements for guests'''
    if guests==0 or guests==1:
        return 1
    else:
        return guests*seating_arrangements(guests-1)
print(seating_arrangements.__doc__)

print("for 1 guest:", seating_arrangements(1))
print("for 2 guests:", seating_arrangements(2))
print("for 3 guests:", seating_arrangements(3))
print("for 4 guests:", seating_arrangements(4))
print("for 5 guests:", seating_arrangements(5))

