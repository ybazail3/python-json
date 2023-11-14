# Importing the json class library to be able to use methods and functions in that library
import json

# Create a dictionary key: value pair for JSON. Values can be arrays.
data = {

    "name": "Jane Doe",
    "age": 25,
    "city": "Seattle",
    "interest": ["True crime", "video games", "working out"],
    "is_student": True,

}

# With Statement, opening a file named data.json and the w letters means we will be writing to that file. And created an object named json_files to be used/passed through.
with open("data.json", "w") as json_file:
    # calling the json class library/object and using the dump method from json library to add and save the data being passed through. And indent 4 spaces.
    json.dump(data, json_file, indent=4)

print("Data has been written to data.json")

# Opening the data.json file and reading ("r") the content and making it an object named json_file
with open("data.json", "r") as json_file:
    # Created an object named loaded_data that will use the json library and load method to display the file
    loaded_data = json.load(json_file)

print("Sucessfully able to read data.json")
# This will print the data.json file
print(loaded_data)

# Calling loaded_data and modifying the data.json file. Changing the age to 21 and adding an interest of reading to the list
loaded_data["age"] = 21
loaded_data["interest"].append("reading")

# Writing to the data.json file and using json_file as the object
with open("data.json", "w") as json_file:
    # Passing through 3 args to be changed in the data.json file
    json.dump(loaded_data, json_file, indent=4)

print("Modified data written to data.json")
