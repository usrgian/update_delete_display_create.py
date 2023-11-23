

DATABASE = []  # collections of products 


def create(): # create func
	
	while True: 
	    product = input('Product: ') # prompts the user to enter the name of the product and stores the input in the variable product.
	    quantity = input('Quantity: ') # prompts the user to enter the name of the product and stores the input in the variable quantity.
	    price = int(input('Price: '))  # prompts the user to enter the price of the product and stores the input in the variable price. int() to converts the input to an integer, which is a whole number.
	    new_product = [product, quantity, price]  # creates a new list called new_product and stores the values of product, quantity, and price in the DATABASE list
	    DATABASE.append(new_product)   # adds the new_product list to the DATABASE list.
	    print('Created!') # prints the message "Created!" to the console

	    usr = input('Would you like to add more? (y/n): ')  # takes user input and stores it in the variable usr.
	    if usr.lower() == 'y': # if the user entered 'Y', 'y', or 'YeS' the program will still consider it a 'y' response.
	    	continue  # tells the program to go back to the beginning of the loop.
	    break #  tells the program to exit the loop. 

def display(): # display func

	if len(DATABASE) == 0:  # checks if the length of the DATABASE list is equal to 0. If it is, then the code inside the if block is executed.
		print('No display!') # prints the message "No display!" to the console.
	else:
	    for i in DATABASE:  #  iterates over the DATABASE list. This means that the loop will execute once for each item in the list. The current item in the list is stored in the variable i.
	        print(f'PRODUCT: {i[0]} QUANTITY: {i[1]} PRICE: ${i[2]}')  # prints out the product name, quantity, and price  as well for the current item in the list. The f-string  is used to format the string so that the values of i[0], i[1], and i[2] are inserted into the string.


def delete(): # delete func

	if len(DATABASE) == 0:  # checks if the length of the DATABASE list is equal to 0. If it is, then the code inside the if block is executed.
		print('No delete!') # prints the message "No display!" to the console.
	else:
	    for i in DATABASE:  #  iterates over the DATABASE list. This means that the loop will execute once for each item in the list. The current item in the list is stored in the variable i.
	        print(f'PRODUCT: {i[0]} QUANTITY: {i[1]} PRICE: ${i[2]}') # prints out the product name, quantity, and price  as well for the current item in the list. The f-string  is used to format the string so that the values of i[0], i[1], and i[2] are inserted into the string.

	    del_prodcut = input('Enter product name to delete: ') 

	    for x,y in enumerate(DATABASE): # terates over the DATABASE . The enumerate()  returns a tuple of two values for each item in the list the index of the item and the item itself. The index is stored in the variable x, and the item is stored in the variable y.
	        if y[0] == del_prodcut: #  checks if the product name at the current index (stored in y[0]) is equal to the del_product variable. If it is, then the code inside the if block is executed.
	            del DATABASE[x] #  deletes the item at the current index (DATABASE[x]) from the DATABASE
	            print('Deleted!')  #  prints the message "No display!" to the console.
	            break  # breaks out of the loop

def update(): # update func

	for i in DATABASE:  #  iterates over the DATABASE list. This means that the loop will execute once for each item in the list. The current item in the list is stored in the variable i.
		print(f'PRODUCT: {i[0]} QUANTITY: {i[1]} PRICE: ${i[2]}') # prints out the product name, quantity, and price  as well for the current item in the list. The f-string  is used to format the string so that the values of i[0], i[1], and i[2] are inserted into the string.

	recent_product = input('Enter product name to update: ') 

	new_product = input('Enter new product: ')  # prompts the user to enter the new name for the product and stores the input in the variable new_product. 
	new_quantity = input(f'Enter new quantity for {new_product}: ')  # prompts the user to enter the new quantity for the product and stores the input in the variable new_quantity. 
	new_price = input(f'Enter new price for {new_product}: ') # prompts the user to enter the new price for the product and stores the input in the variable new_price. 

	for i in DATABASE:  # iterates over the DATABASE list. The current item in the list is stored in the variable i.
		if i[0] == recent_product:  # checks if the product name at the current index (stored in i[0]) is equal to the recent_product variable. If it is, then the code inside the if block is executed.
			i[0] = new_product # updates the product name to the value of new_product.
			i[1] = new_quantity # updates the quantity name  to the value of new_quantity.
			i[2] = new_price # updates the price name to the value of new_price.
			print('Updated successfully!') # prints the message "Updated successfully!" to the console.
		break # breaks out of the loop

while not False: # while not False is equivalent to while True 

    print('1) Create ')  # printsthe message 'Create' to the console
    print('2) Update ')  # prints the message 'Update' to the console
    print('3) Delete ')  # prints the message 'Delete' to the console
    print('4) Display ')  # prints the message 'Display' to the console
    print('5) Quit ')  # prints the message 'Quit' to the console

    usr = input('Enter between 1 & 5: ') 
    
    if not usr.strip(): # checks if the usr variable is empty. If it is, then the code inside the if block is executed.
    	print('Please, enter between 1 & 5!')  # prints the message 'Please, enter between 1 & 5!' to the console.
    elif int(usr) == 1: 
        create() # calls the create func
    elif int(usr) == 4:
        display() # calls the display func
    elif int(usr) == 3:
        delete() # calls the delete func
    elif int(usr) == 2:
        update() # calls the update func
    else:
    	print('Quited!')
    	break  # break out of the loop




