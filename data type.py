cars=["Ford", "Volvo", "BMW"]
#cars[0]="marcedes"
x = cars[0]
#print(cars[0])
cars.pop(2)
#print(cars[0])
cars.remove("Volvo")
y=len(cars)
print (y)
for x in cars:
    print (x)


#dictionary
z = {"name" : "John", "age" : 36}
print(z)
print(z["age"]+1)


element = {
  "name": "Chlorine",
  "weight": 35.5,
  "Pt group": 17,
  "E group":7,
  "E name":"halogen",
  "Element structure":"C:/Users/sandra/AppData/Local/images/Elements/17.jpeg"

}
Elements=[{
  "name": "","Boron"
  "weight": 35.5,
  "Pt group": 13,
  "E group":7,
  "E name":"halogen",
  "Element structure":"C:/Users/sandra/AppData/Local/images/Elements/17.jpeg"

},{
  "name": "Chlorine",
  "weight": 35.5,
  "Pt group": 17,
  "E group":7,
  "E name":"halogen",
  "Element structure":"C:/Users/sandra/AppData/Local/images/Elements/17.jpeg"

}]
print (Elements[0])

print(element["Pt group"])
print(element.values())
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
