# print number 1 to 5

print(1)
print(2)
print(3)
print(4)
print(5)

# Loop 

# while loop 

i = 1 
while i < 6:
    # body 
    print(i)
    i += 1 # i = i + 1


# infinite loop 

# while True:
#     print("I will keep printing")




# for loop 

for i in range(1, 6):
    print(i)

# Birthday Names
names = ['Robert', 'John', 'Kyle', 'Kelly']

# Happy birthday Robert
# Happy birthday John

for name in names:
    message = "Happy Birthday " + name + "!"
    print(message)


for i in range(len(names)): # equal to range(0, len(names))
    message = "Happy Birthday " + names[i] + "!"
    print(message)

for index, name in enumerate(names):
    message = name + " is in index " + str(index) 
    print(message)



# Loops with logic 


ages = [15, 26, 18, 44, 98, 52]

for age in ages:
    # Using logic inside the for loop
    if age >= 60:
        print("The person is a senior")
    elif age >= 18:
        # Tell me if the person is a teen or not
        if age > 19:
            # When age greater than 19 
            print("The person is an adult, but not a teen")
        else:
            # when age 18, 19 
            print("The person is an adult and a teen")
    else:
        print("The person is a kid")

