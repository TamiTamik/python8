person = {
    "name":"bold",
    "age": 22
}
for key in person:
    print(person[key])

for element in person.values():
    print(element)

for x,y in person.items():
    print(x, y)

person.clear()
print(person)