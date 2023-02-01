import json

data = '''{
    "name" : "Meet" ,
    "phone" : {
        "type" : "int1" ,
        "number" : "+1 734 303 4456"
    } ,
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data) # converts data from JSON format to dictionary

print("Name :- " , info["name"])
print("Hide :- " , info["email"]["hide"])


def p(obj):
  return json.dumps(obj , sort_keys=True, indent=2)

#dictionary is printed in json format, in alphabetical order(since we used sort_keys) and well indented(to help us understand better)
print(p({'a' : 5 , 'b' : 6}))
