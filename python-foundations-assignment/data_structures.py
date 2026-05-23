#SECTION 4
#favtools
tools =  ["laptop", "python", "vs code"]
tools.append("github")
tools.remove("laptop")
print(tools)

#stuscores
scores = (70, 85, 90, 60, 75)
print("highest:", max(scores))
print("lowest:", min(scores))
print("average:", sum(scores)/len(scores))

#shopping
shopping_list = ["rice", "milk", "bread"]
shopping_list.append("eggs")
shopping_list.remove("milk")
print(shopping_list)

#cap
countries = {
    "Ghana": "Accra",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi"
}
print(countries)


#visitors
visitors = ("Sandra", "Gillian", "Cassandra", "Prince")
unique_visitors = set(visitors)
print(unique_visitors)

#skills
skills1 = ["python", "HTML", "CSS"]
skills2 = ["python", "javascript", "CSS"]
skills1_set = set(skills1)
skills2_set = set(skills2)
common = skills1_set.intersection(skills2_set)
print(common)

#student record
student = {
     "name": "Sandra",
     "age": 25,
     "course": "political science"
}

print(student)

contacts = {
"Ama": "0546750350",
"Abena": "0545939739",
}

name = input("Enter contact name: ")

if name in contacts:
    print(f"{name}'s phone number is {contacts[name]}")
else:
    print(f"{name} not found in contacts.")
