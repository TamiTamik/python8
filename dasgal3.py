#nasandhursen hunii toog ol
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
    if item['age'] >= 18:
        s = s+1
print("nasand hursen hunii too:" ,s)