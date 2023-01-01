# Dictionaries in Python.

# Key value pair.
dic = {
    "name": "Himanshu Soni",
    "city": "Kanpur",
    "phone": "6386333099"
}

# This will generate an error if requested data is not available.
print(dic["name"])

# This will return None if requested data is not available.
print(dic.get("city"))

# To print only values we will use this.
print(dic.values())

# To access the whole dict we will use:
for key in dic.keys():
    print(key, ":", dic[key])

# Another method is
for key, value in dic.items():
    print(f"{key}:{value}")
