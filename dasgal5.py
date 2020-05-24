person = [
    {
        "name" : "bold",
        "age" : 22,
        "friends" : ['Bat']
    },{
        "name" : "tulga",
        "age" : 25,
        "friends" : ['Sugar','Tamir']
    },{
        "name" : "bat",
        "age" : 16,
        "friends" : ['Purew','Lkham','Yoshi']
    }
]
friend = 0
for item in person:
    if len(item['friends'])> friend:
        friend = len(item['friends'])
        index = person.index(item)
print(person[index])
