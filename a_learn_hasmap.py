from collections import defaultdict

# =========================
#  ARRAY AND HASHING
# =========================

# - DIFFERENTS HASHMAP

new_map = {}                # create key pair value. 
#                           Can not access a key that is not created yet.
#                           Each key that is already define can have different type of value. (one key can store an int and the other can store an array)

new_defaultdict = defaultdict(int) # create key pair value and allow to define default value.
#                           will return 0 when trying to access a key that does not existe.
#                           allow to define the type of the future value, in this case integer (int).

new_set = set()             # It'slike a map but only store unique value


# # 1 - HASHMAP {} 
# # ---------------------
# # Creating a hashmap
# new_map = {}
# # print(new_map)

# # Adding key-value pairs to the hashmap
# new_map['apple'] = 3
# new_map['banana'] = "Hello"
# new_map['orange'] = [True, 1, "hello"]
# new_map['mango'] = {"color":"yellow", "size": "medium", "number": 5}

# print(new_map)

# # Accessing values using keys
# print(new_map['apple'])  # Output: 3

# # Modifying a value associated with an existing key
# print(new_map['banana'])  # Output: Hello
# new_map['banana'] = 7
# print(new_map['banana'])  # Output: 7

# # Checking the presence of a key
# print('orange' in new_map)  # Output: True
# print('blueberry' in new_map)  # Output: False

# # Removing a key-value pair
# print(new_map)  # Output: {'apple': 3, 'banana': 'Hello', 'orange': [True, 1, 'hello'], 'mango': {'color': 'yellow', 'size': 'medium', 'number': 5}}
# del new_map['apple'] 
# print(new_map)  # Output : {'banana': 'Hello', 'orange': [True, 1, 'hello'], 'mango': {'color': 'yellow', 'size': 'medium', 'number': 5}}

# # Iterating through the keys and values
# for key, value in new_map.items():
#     print(key, value)
# # Output:
# # apple 3
# # banana Hello
# # orange [True, 1, 'hello']
# # mango {'color': 'yellow', 'size': 'medium', 'number': 5}



# # Sample dictionary with integer values
# new_map_int = {}
# print(new_map_int)

# new_map_int['apple'] = 5
# new_map_int['Banana'] = 10
# new_map_int['Orange'] = 3
# new_map_int['Grapes'] = 8

# print(new_map_int)

# # Sort the dictionary items in descending order based on the integer values
# sorted_data = dict(sorted(new_map_int.items(), key=lambda item: item[1], reverse=True))

# # The sorted_data dictionary will maintain the sorted order

# # Printing the sorted dictionary
# # for key, value in sorted_data.items():
# #     print(f"{key}: {value}")

# print(sorted_data)


# # 2 - DICTIONARY dict() : upgraded version of a map {} 
# # ---------------------

# new_defaultdict = defaultdict(int)

# new_defaultdict['Apple'] += 5
# print(new_defaultdict['Apple'])  # Output: 5

# print(new_defaultdict['Banana'])  # Output: 0 (the default value)

# 3 - HASHSET set() 
# ---------------------

# # Creating a hashset
# # new_set = set()
## nums =[1,3,4,5,3,6,7,82,4]
## other_set = set(nums) # will initialize a set with all the unique value in the array.

# # Adding elements to the hashset
# new_set.add(1)
# new_set.add(2)
# new_set.add(3)

# # Adding a duplicate element won't create a new entry
# new_set.add(1)

# # The hashset will contain only unique elements
# print(new_set)  # Output: {1, 2, 3}

# # Removing an element from the hashset
# new_set.remove(2)

# # Checking the presence of an element
# # print(1 in new_set)  # Output: True
# # print(2 in new_set)  # Output: False
