# JSON Structure:
# {
#   "id" : 1,
#   "data" : { 
#       "input" : (data from dataset.log before ' --- ')
#       "output": (data from access.log after ' --- ')
#   }
# }  
import json

dataset = [] 
input_file = "data\dataset.log"
output_file = "data\dataset.json"

with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    x = 0
    for line in lines:
        if ' --- ' in line:
            x += 1
            input_data, output_data = line.split(' --- ', 1)
            entry = { 
                "id": x,
                "data": {
                    "input": input_data.strip(),
                    "output": output_data.strip()
                }
            }
            dataset.append(entry)


with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(dataset, json_file, indent=4)