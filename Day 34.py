# Dictionaries Methods.

dic = {
    "name": "Himanshu Soni",
    "city": "Kanpur",
    "state": "UP",
    "phone": "6386333099",
    "roll": 13,
    "country": "India"
}

dic2 = {
    "name": "Nitin Soni",
    "city": "Kanpur",
    "state": "UP",
    "phone": "9616570665",
    "roll": 14
}

# Update method updates the values of calling dict with the values of called dict. If new key value pair is found then new pair will be created. Otherwise old pair will be updated.
dic.update(dic2)

# Clear method remove all data from dictionary.
dic2.clear()

# Pop method pops out the passed item.
dic.pop("country")

# PopItem method will pop out the last item.
dic.popitem()

# Del keyword will delete the dictionary.
del dic2

# Del keyword will delete the item passed as key also.
del dic["roll"]

print(dic)
print(dic2)
