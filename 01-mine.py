grocery_list = []


print("How many items did you buy?")
n = input('> ')

# to ask user for exact item purchase n collect expiry dates
for i in range(n):
	item = {}
	item['name'] = str(raw_input("What did you buy? "))
	item['expiry date'] = str(raw_input("When will it expire? "))
	grocery_list.append(item)

# to print grocery in a list
# to match expiry dates to grocery list
for item in grocery_list:
	print item 





