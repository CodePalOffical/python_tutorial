# Check if a person is an adult 

# A person is an adult if they are older than and equal 18 years old
# Otherwise they are not a adult 

age = int(input("What is your age? "))

# if they are older than and equal 18 years old
if age >= 18:
    print("The person is an adult")
else:
    print("This person is not an adult") 

# We what us to tell if the person is senior or not 
# A person is a senior when they are over 60 


if age >= 60:
    print("The person is a senior")
elif age >= 18:
    # Tell me if the person is a teen or not
    if age > 19:
        # When age greater than 19 
        print("The person is an adult but not a teen")
    else:
        # when age 18, 19 
        print("The person is an adult and a teen")
else:
    print("The person is a kid")
    
