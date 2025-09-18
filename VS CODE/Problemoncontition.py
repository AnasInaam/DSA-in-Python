species = input("Enter the species in this three Zorg , Xen , Plok: ")
age = int(input("Enter the age of the species: "))
ability_score = int(input("Enter the ability score of the species: "))

if species == "Zorg":
    if age >= 300 and ability_score >= 80:
        print("Allowed")
    elif age >=250 and ability_score == 100:
        print("Allowed")
    else:
        print("Not Allowed")

if species == "Xen":
    if ability_score >= 60 and 200 <= age <= 500:
        print("Allowed")
    elif age < 100 and ability_score >= 90:
        print("Allowed")
    else:
        print("Not Allowed")


from sympy import isprime

if species == "Plok":
    if isprime(age) and ability_score % 5 == 0:
        print("Allowed")
    else:
        print("Not Allowed")
