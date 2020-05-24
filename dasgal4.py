#nasand hursen ba huuhdiin nasni dundjiin zuruug ol
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
c1 = 0
b = 0
c2 = 0
for item in person:
    if item['age'] >= 18:
        s = s + item['age']
        c1 = c1 + 1
    else:
        b = b + item['age']
        c2 = c2 + 1
print(abs(s/c1-b/c2))