ninja_belts = {"crystal":"red" , "jeru":"black"}
print(ninja_belts)
print(ninja_belts["crystal"])
print(ninja_belts["jeru"])

if('jeru' in ninja_belts):
    print('true')
else:
    print("false")

print(ninja_belts.keys())
print(ninja_belts.values())

#to print in the form of list
val = print(list(ninja_belts.values()))
key = print(list(ninja_belts.keys())) 

ninja_belts['pinky'] = 'blue'
print(ninja_belts) 

#Another method
person = dict(Name = "sunny" , age = 30) , dict(Name = "chinny" , age = 20)
print(person)

# Fucntion using dictionary
def ninja_intro(dict):
    for key, val in dict.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = { }

while True:
    ninja_name = input('add a ninja name: ')
    ninja_belt = input('add a ninja colour: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n): ')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)