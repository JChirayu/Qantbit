import json

def parseJson(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print (data)

    for key, value in data.items():
        print(f'{key}:{value}')
    
parseJson('demo.json')