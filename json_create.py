import json
import os
val = input("input flag here: ")
directory = val
parent_dir = "Documents/UIBUilder"
path = os.path.join(parent_dir, directory)
try:
	os.makedirs(path, exist_ok = True)
	print("Directory '%s' created successfully" % directory)
except OSError as error:
	print("Directory '%s' can not be created" % directory)

user_data = [{ "user" : val}]
with open('new_file.json', 'w') as f:
    json.dump(user_data, f)