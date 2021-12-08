import os
import random

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# WHOLE_GROUP = {1:'Kornél', 2:'Nelli', 3:'Balázs', 4:'Nándi', 5:'Évi', 6:'Bence', 7:'Barbi', 8:'Orsi', 9:"Gee"}
WHOLE_GROUP = {'Kornél', 'Nelli', 'Balázs', 'Nándi', 'Évi', 'Bence', 'Barbi', 'Orsi', "Gee"}


def get_number_of_group_members(group):
    number_of_group_members = input('How many people should be in a group? \n')
    number_of_groups = len(group) // number_of_group_members
    


def add_members(group):
    screen_clear()
    new_member = input('Please provide the name of the new member! \n')
    group[len(group) + 1] = new_member
    screen_clear()
    print(f'Current members are: {get_group(group)}')
    do_it_again = input('Do you want to add more members? \n 1 - Yes \n 2 - No \n 3 - Other change \n')
    if do_it_again == '1':
        add_members(group)
    elif do_it_again == '2':
        return group
    elif do_it_again == '3':
        choose_custom_members(group)


def delete_members(group):
    screen_clear()
    print(f'{group}')
    remove_member = input('Please choose the member\'s number to remove the member! \n')
    del group[int(remove_member)]
    print(f'{group}')
    do_it_again = input('Do you want to delete more members? \n 1 - Yes \n 2 - No \n 3 - Other change \n')
    if do_it_again == '1':
        delete_members(group)
    elif do_it_again == '2':
        return group
    elif do_it_again == '3':
        choose_custom_members(group)


def create_new_list(group):
    screen_clear()
    new_member = input('Please give the members\'s name! \n') 
    group[len(group + 1)] = new_member
    do_it_again = input('Do you want to add more members? \n 1 - Yes \n 2 - No \n 3 - Other change \n')
    if do_it_again == '1':
        create_new_list(group)
    elif do_it_again == '2':
        return group
    elif do_it_again == '3':
        choose_custom_members(group)


def choose_custom_members(group):
    screen_clear()
    method = input('''
Do you want to add or delete a member or create a new list?
    
1 - Add
2 - Delete
3 - Create new list
4 - I am done
    
''')
    if method == '1':
        add_members(group)
    elif method == '2':
        delete_members(group)
    elif method == '3':
        group = {}
        create_new_list(group)
    elif method == '4':
        get_number_of_group_members(group)
    else:
        print('Please provide a valid input! \n')
        choose_custom_members(group)


def get_group(WHOLE_GROUP):
    temp_group = []
    for key, value in WHOLE_GROUP.items():
        temp_group.append(value)
    return temp_group
    

def get_names():
    group_list = get_group(WHOLE_GROUP)
    group = WHOLE_GROUP
    names = input(f'''
Please provide the names to make the groups of!
1 - Whole group - {group_list}
2 - Custom members
    
''')
    if names == '1':
        return WHOLE_GROUP
    elif names == '2':
        choose_custom_members(group)
    else:
        print('Please provide a valid input! \n')
        get_names()


def welcome():
    print('welcome to the Random Group Creator! \n')


def main():
    welcome()
    group = get_names()


if __name__ == '__main__':
    main()