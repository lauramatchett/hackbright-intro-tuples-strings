#our_names = "kelsey, laura"
#print our_names.split(",")


#string = "1, 2,3, 4, 5"
#print string.split(",")

#drseuss = "one fish two fish red fish blue fish"
#split = drseuss.split("fish")
#print split



str = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:bananas,quantity:6,price:3.00\n"]
#split_str = bill.split(", ")


def calculate_bill(bill): 
	split_string = bill.split(",")
	quantity = float(split_string[1].split(":")[1])
	price = float(split_string[2].split(":")[1].strip())
	total = quantity * price
	return total

#index = 0
#total = 0
#while(len(str)-1<=index):
#	index = index +1
#	total +=


def loop(str):
	total = 0
	for elem in str:
		total += calculate_bill(elem)
	return total

print loop(str)
