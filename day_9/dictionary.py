# to store key and value, use dictionaries
marks = {"math": 50, "english": 65, "physics": 66, "chemistry": 80, "biology": 56}

# empty dictionaries
empty_dictionary = {} # can use to wipe the existing dictionaries

# editing dictionary
marks["math"] = 72
print(marks)

# retriving the value
math_score = marks["math"]
print(math_score)

# loop with for~in get all the keys
for key in marks:
    print(f"{key} - {marks[key]}")
    
# nesting list and dictionaries
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# printing Lille
print(travel_log["France"][1])

# dictionary inside dictionary
travel_log = {
    "France": {
        "times_visited": 5,
        "city_visited": ["Paris", "Lille", "Dijon"]
    },
    "Myanmar": {
        "city_visited": ["Bagan", "Yangon", "Mandalay"],
        "times_visited": 8
    }
}

# accessing Bagan
print(travel_log["Myanmar"]["city_visited"][0])