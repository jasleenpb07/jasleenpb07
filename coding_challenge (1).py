num = int(input("Enter a number: "))
list1 = []
if num > 0:
    print(f"Number is: {num}")
    for i in range(1,num + 1):
        if num % i == 0:
            list1.append(i)
            list1.append(-i)
            
elif num < 0:
    print(f"Number is: {num}")
    for i in range(-1,num - 1,-1):
        if num % i == 0:
            list1.append(i)
            list1.append(-i)
            
else:
    print(f"Number is: {num}")

if num > 0:
    print("Factors are: ")
elif num < 0:
    print("Factors are: ")
else:
    print("Factors are: N/A")

for i in list1:
    print(i)
    print(f"> {i} X {num//i} = {num}")
    print()

"""count = 0
while count < len(list1):
    print(list1[count])
    count += 1"""

print(" ")

if len(list1) == 0:
    if num == 0:
        print("0 cannot have any factors, Try something else!")

elif len(list1) == 2:
    if num < 0:
        print("Neither prime,nor composite(A negative odd number)")
    elif num > 0:
        print("Neither prime,nor composite(A positive odd number)")
        

elif len(list1) == 4:
    if num < 0:
        if num % 2 == 0:
            print("It is an even prime number.(Negative)")
        else:
            print("It is an odd prime number.(Negative)")
    elif num > 0:
        if num % 2 == 0:
            print("It is an even prime number.(Positive)")
        else:
            print("It is an odd prime number.(Positive)")
        

else:
    if num < 0:
        if num % 2 == 0:
            print(f"It is an even composite number with {len(list1)} factors.(Negative)")
        else:
            print(f"It is an odd composite number with {len(list1)} factors.(Negative)")
    elif num > 0:
        if num % 2 == 0:
            print(f"It is an even composite number with {len(list1)} factors.(Positive)")
        else:
            print(f"It is an odd composite number with {len(list1)} factors.(Positive)")

        
        

