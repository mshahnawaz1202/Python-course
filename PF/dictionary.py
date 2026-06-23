# Dictionary is a data structure that stores key-value pairs. Each key is unique.
'''
1. Unordered (in Python 3.6 and below, from 3.7 it preserves insertion order)
2. Can be changed (mutable)
3. No indexing like lists or tuples, access using keys
4. No duplicate keys (latest value overwrites)
'''
e={} # empty dictionary
# Example dictionary
marks = {
    "shah": 79,
    "nawaz": 78,
    "Ali": 80,
    "Haider": 23
}

# Accessing values using keys
print("Shah's marks:", marks["shah"])  # Output: 79

# Another dictionary with list as value
m = {
    "name": "Shahnawaz",
    "City": "Pakistan",
    "Marks": [78, 77, 79]
}
print("\nPersonal Info Dictionary:", m)

# ----------------------------- Dictionary Methods -----------------------------

# 1. .items() → returns all key-value pairs as tuples
print("\nmarks.items():", marks.items())  # dict_items([('shah', 79), ...])

# 2. .keys() → returns all the keys
print("marks.keys():", marks.keys())  # dict_keys(['shah', 'nawaz', ...])

# 3. .values() → returns all the values
print("marks.values():", marks.values())  # dict_values([79, 78, 80, 23])

# 4. .get(key) → returns value of given key, returns None if not found (safe)
print("\nmarks.get('shah'):", marks.get("shah"))   # 79
print("marks.get('shah1'):", marks.get("shah1"))   # None (no error)

# 5. Accessing with [] gives error if key not found
# print(marks["shah1"])  # ❌ KeyError

# 6. .update() → updates existing key or adds new key-value pair
marks.update({"shah": 99, "Chomu": 24})  # shah updated, Chomu added
print("\nUpdated marks dictionary:", marks)

# 7. .pop(key) → removes a key and returns its value
removed_value = marks.pop("nawaz")  # Removes 'nawaz'
print("Removed 'nawaz':", removed_value)
print("After pop:", marks)

# 8. .popitem() → removes the last inserted item (Python 3.7+)
last_item = marks.popitem()
print("Last item removed (popitem):", last_item)
print("After popitem:", marks)

# 9. .clear() → removes all key-value pairs
# marks.clear()
# print("After clear():", marks)  # {}

# 10. .copy() → returns a shallow copy of the dictionary
marks_copy = marks.copy()
print("\nCopied dictionary:", marks_copy)

# 11. .fromkeys() → creates new dictionary from given keys and one value
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print("New dictionary using fromkeys():", new_dict)

# 12. .setdefault(key, default) → returns value if key exists; otherwise adds it
print("setdefault existing key:", marks.setdefault("Ali", 0))  # 80
print("setdefault new key:", marks.setdefault("newGuy", 100))  # Adds 'newGuy'
print("After setdefault:", marks)
