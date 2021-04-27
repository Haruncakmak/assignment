age = input("Are you a cigarette addict older than 75 years old?:")
if age.title() == "Yes" :
    age = True
elif age.title() == "No" :
    age = False
else :
    print("Invalid Answer")
chronic = input("Do you have a severe chronic disease?:")
if chronic.title() == "Yes" :
    chronic = True
elif chronic.title() == "No" :
    chronic = False
else :
    print("Invalid Answer")
immune = input("Is your immune system too weak?:")
if immune.title() == "Yes" :
    immune = True
elif immune.title() == "No" :
    immune = False
else :
    print("Invalid Answer") 
if (age or chronic or immune) :
    print("You are in risky group")
else :
    print("You are not in risky group")
    