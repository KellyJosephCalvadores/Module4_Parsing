import json

course = []

with open('sample.json', 'r') as json_file:
    x = json.load(json_file)

    for courses in x['certifications']:
        print(courses['name'])
        print(courses['courses'])