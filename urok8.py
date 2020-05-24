#dictionary -> key, value
#get - poluchit' kachestva elementa
#pered ":" - key, posle ":" - value
person = {
    "name":"bold",
    "age": 22
}
name1 = person['name']
name2 = person.get('name')
person['friends'] = ['bat','tulga']
person['name'] = 'tumur'
person['ddd'] = 'aaa'
print(name1,name2)
print(person)