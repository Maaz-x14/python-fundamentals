# Dictionaries are data structures used to store data in key-value pairs
# Defined using curly braces and values are assigned using colon
employee = {
    "name": "Maaz",
    "id": 112,
    "age": 19,
    "is_new": True
}
# You can access the value associated with a specific key using square brackets []
print(employee["name"])
# We can also use
print(employee.get("age"))
# You can add a new key-value pair or update an existing one by assigning a value to a key
employee["email"] = "Lostunknown06@gmail.com"  # Add
employee["id"] = 140  # Update
del employee["is_new"]  # Deletes
# print(employee["is_new"]) , gives error