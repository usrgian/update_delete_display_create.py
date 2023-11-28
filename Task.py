

database = []

def create_task():

    while True:
        user1 = input('ID Task: ')
        user2 = input('Task Name: ')
        new_task = [int(user1),user2,'Not Complete']
        database.append(new_task)
        print('Added!')

        user = input('Add again? y/N: ')

        if str(user.lower()) == 'y':
            continue
        else:
            break

def dislay_task(database):

    if len(database) == 0: 
        print('No tasks!')
    else:
        print('\n')
        x = 0 # for the completed tasks
        i = 0 # for the incomplete tasks 
        for _ in database:
            print(F'ID: {_[0]} Name: {_[1]} STATUS: {_[2]}') 

            if 'Completed' == _[2]:
                x += 1
            else:
                i += 1

        print(f'Completed: {x}')
        print(f'Not Complete: {i}')
        print('\n')
        

def delete_task(database):
    
    
    if len(database) == 0:
        print('No deletes!')
    else:
        for _ in database:
            print(F'ID: {_[0]} Name: {_[1]} STATUS: {_[2]}')


    user = input('Enter ID to Delete: ')

    for _ in database:
        if _[0] == int(user):
            del database[:2]
            print('Deleted!')

def update_task(database):
    
    if len(database) == 0:
        print('No updates!')
    else:
        for _ in database:
            print(F'ID: {_[0]} Name: {_[1]} STATUS: {_[2]}')

    
    user = input('Enter ID to Update: ')

    for _ in database:
        if _[0] == int(user):
            _[0] = input('New ID: ')
            _[1] = input('New Task Name: ')
            _[2] = input('New Status: ')
            print('Updated!')

while True:

    print('1) Create Task')
    print('2) Display Task')
    print('3) Delete Task')
    print('4) Update Task')
    print('5) Log out')

    user = input('>> ')

    if int(user) == 1:
        create_task()

    elif int(user) == 2:
        dislay_task(database)
    
    elif int(user) == 3:
        delete_task(database)
        
    elif int(user) == 4:
        update_task(database)
    
    else:
        quit('Logged out!')