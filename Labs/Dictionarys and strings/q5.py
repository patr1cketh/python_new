#q1
items = "1,fruit,apples,bananas,grapes,pineapples,blueberries"

"""
items_as_list = items.split(",")
print(items_as_list)

category_number = items_as_list[0]
print(category_number)

#q3
category_name = items_as_list[1]
print(category_name)

#q5
items_in_category = []
for i in range(2, len(items_as_list)):
    items_in_category.append(items_as_list[i])

print(items_in_category)
"""

#q6
def translate_to_dict(string):
    items_as_dict = {}
    items_as_list = string.split(",")
    category_number = items_as_list[0]
    category_name = items_as_list[1]
    items_in_category = []
    for i in range(2, len(items_as_list)):
        items_in_category.append(items_as_list[i])

    items_as_dict[category_number] = {
        "category": category_name,
        "items": items_in_category
    }
    return items_as_dict

print(translate_to_dict(items))
