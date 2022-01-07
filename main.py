from operator import itemgetter
lis = [
    { "name" : "Nandini", "age" : 20},
    { "name" : "Manjeet", "age" : 20 },
    { "name" : "Nikhil" , "age" : 19 }
]
print("The list is printed in descending order: ")
print(sorted(lis, key=itemgetter('age'),reverse = True))