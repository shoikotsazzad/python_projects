temperature = 35
if temperature > 30:
    print("It's warm")
    print('Drink Water')
elif temperature >20:
    print("It's nice")
else:
    print("It's cold")

print("Done") #it will run always


# Another clean example

age = 22
# if age >= 18:
#     message = "Elegible"
# else: 
#     message = "Not Elegible"
# print(message)

#Write that same code with easy cleaner way

message = "Eligible" if age >= 18 else "Not Eligible"
print(message)