import sys


def old_master():
    add()


# Function to add a new master to masters text file
def new_master():
    with open('masters.txt', mode='a') as m:
        m.write(master_pwd)


# Function to Add Passwords to a certain master profile
# if current master does not have a profile it creates one

def add():
    name = input('Account: ')
    pwd = input('Password: ')
    with open(master_pwd + '.txt', mode='a') as f:
        f.write(name + '|' + pwd + '\n')


def view():
    with open(master_pwd + '.txt', mode='r') as f:
        print(f.read())


# start

# creating a text file that will hold the masters passwords
with open('masters.txt', mode='a') as f:
    f.write('')

# Identifying the master, if it can't create another master or quit
while True:
    # Identifying
    master_pwd = input('What is the master Password: ')
    # checking if master exists
    with open('masters.txt', mode='r') as k:
        x = master_pwd not in k.readlines()
        if x:
            create = input(
                'Wrong Password do you want to create new master press (y) else press (t) to try again or press (q) to quit: ')
        else:
            break
        # quit option
        if create == 'q':
            print('quitting...')
            quit()
        # create option
        if create == 'y':
            new_master()
            break
        else:
            continue
# Step 2
# add or view current master passwords
while True:
    mode = input('Would you like to add a new Password or view Passwords (add , view) press q to quit:  ')
    # Quit Option
    if mode == 'q':
        print('quitting...')
        sys.exit(1)
    # View Option
    if mode.lower() == 'view':
        view()
    # Add Option
    elif mode.lower() == 'add':
        add()

    else:
        continue
