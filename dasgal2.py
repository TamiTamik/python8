#dundaj nasig ol
person = [
    {
        "name" : "bold",
        "age" : 22
    },{
        "name" : "tulga",
        "age" : 25
    },{
        "name" : "bat",
        "age" : 16,
        "friends" : ['Purew']
    }
]
s = 0
for item in person:
    s = s + item['age']
print(s/len(person))
