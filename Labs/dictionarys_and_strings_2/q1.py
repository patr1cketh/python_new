#q1
items = "1,fruit,apples,bananas,grapes,pineapples,blueberries\n2,vegetables,celery,cabbage,carrots\n3,soda,7up,club orange,coca cola"
items_as_list = items.split("\n")
print(items_as_list)

#q3
for line in items_as_list:
    line_as_list = line.split(",")
    if line_as_list[0] in ["1","2"]:
        print(line)