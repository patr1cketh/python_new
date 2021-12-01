#q1
items = "1,fruit,apples,bananas,grapes,pineapples,blueberries"
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
