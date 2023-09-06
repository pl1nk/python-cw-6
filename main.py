# write your code here
person = {

    "name": "Abdullah",
    "age": 27,
    "hobbies": ['Gaming', 'Coding','fixing cars' ]



}

print(person["name"])
print(person["age"])

person.update({'age':19})
person['country'] = 'Kuwait'
print(person)
print(len(person))

person["hobbies"].append("food") 

def check_hobbies(person):
    if len(person["hobbies"]) > 3 :
        print("WOW YOU ARE AMAZING!!!")
    

check_hobbies(person)            
