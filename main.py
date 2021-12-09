import os
import random


WHOLE_GROUP = ['Kornél', 'Nelli', 'Balázs', 'Nándi', 'Évi', 'Bence', 'Barbi', 'Orsi', "Gee"]


def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def choose_try_again():
    try_again = input('\nDo you want to try again? \n 1 - Yes \n 2 - No \n')
    if try_again == '1':
        screen_clear()
        main()
    elif try_again == '2':
        quit()
    else:
        print('Please provide a valid input!')
        choose_try_again()


def print_groups(final_group):
    print('The members for the groups are: \n')
    for count, members in enumerate(final_group):
        print(f'Group {count + 1} : {members}')


def choose_method_remainders(number_of_groups, final_group, shuffled_group, group_index):
    method = input(f'''
    There are remaining members, {len(group_index)} person(s).
    How do you want to portion them?
    1 - Add to existing grops
    2 - Create a new group
    ''')
    if method == '1':
        for count in range(len(group_index)):
            index_num = random.choice(group_index)
            group_index.pop(group_index.index(index_num))
            final_group[count].append(shuffled_group[index_num])
    elif method == '2':
        final_group.append([])
        for count in range(len(group_index)):
            index_num = random.choice(group_index)
            group_index.pop(group_index.index(index_num))
            final_group[number_of_groups].append(shuffled_group[index_num])
    return final_group
  

def get_groups(group, number_of_group_members, number_of_groups):
    final_group = [[ '' for j in range(int(number_of_group_members))] for i in range(number_of_groups)]
    shuffled_group = list(group)
    random.shuffle(shuffled_group)
    group_index = [i for i in range(len(group))]
    for i in range(number_of_groups):
        for j in range(int(number_of_group_members)):
            index_num = random.choice(group_index)
            group_index.pop(group_index.index(index_num))
            final_group[i][j] = shuffled_group[index_num]
    if len(group_index) != 0:
        final_group = choose_method_remainders(number_of_groups, final_group, shuffled_group, group_index)
    return final_group


def get_number_of_group_members(group):
    number_of_group_members = int(input('How many people should be in a group? \n'))
    number_of_groups = len(group) // number_of_group_members
    if number_of_groups == 0:
        print('Please provide a valid input')
        get_number_of_group_members(group)
    return number_of_group_members, number_of_groups
   
 
def add_members(group):
    screen_clear()
    new_member = input('Please provide the name of the new member! \n')
    group.append(new_member)
    return group
  

def delete_members(group):
    group_dict = get_group_dict_from_list(group)
    print(f'{group_dict}')
    remove_member = int(input('\nPlease choose the member\'s number to remove the member! \n'))
    if remove_member not in group_dict.keys():
        print('Provide a valid input!')
        delete_members(group)
    del group_dict[int(remove_member)]
    group = get_group_list_from_dict(group_dict)
    return group
  

def choose_custom_members(group):
    while True:
        screen_clear()
        method = input(f'''
The current members are: {group}

Do you want to add or delete a member or create a new list?
        
    1 - Add
    2 - Delete
    3 - Create new list
    4 - I am done
        
    ''')
        if method == '1':
            screen_clear()
            group = add_members(group)
        elif method == '2':
            screen_clear()
            group = delete_members(group)
        elif method == '3':
            screen_clear()
            group = []
            group = add_members(group)
        elif method == '4':
            return group
        else:
            print('Please provide a valid input! \n')
            choose_custom_members(group)
    


def get_group_list_from_dict(group):
    temp_group = []
    for key, value in group.items():
        temp_group.append(value)
    return temp_group


def get_group_dict_from_list(group):
    group_list = {}
    for i in group:
       group_list[len(group_list) + 1] = i
    return group_list
    

def choose_group():
    group = WHOLE_GROUP
    names = input(f'''
Please provide the members to make the groups of!
1 - Whole group - {group}
2 - Custom members
    
''')
    if names == '1':
        return group
    elif names == '2':
        group = choose_custom_members(group)
        return group
    else:
        print('Please provide a valid input! \n')
        choose_group()
    

def welcome():
    print('''
  /$$$$$$$                            /$$                              
| $$__  $$                          | $$                              
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$       
| $$$$$$$/ |____  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$      
| $$__  $$  /$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$      
| $$  \ $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$      
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$      
|__/  |__/ \_______/|__/  |__/ \_______/ \______/ |__/ |__/ |__/      
        /$$$$$$                                                       
       /$$__  $$                                                      
      | $$  \__/  /$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$                
      | $$ /$$$$ /$$__  $$/$$__  $$| $$  | $$ /$$__  $$               
      | $$|_  $$| $$  \__/ $$  \ $$| $$  | $$| $$  \ $$               
      | $$  \ $$| $$     | $$  | $$| $$  | $$| $$  | $$               
      |  $$$$$$/| $$     |  $$$$$$/|  $$$$$$/| $$$$$$$/               
       \______/ |__/      \______/  \______/ | $$____/                
                                             | $$                     
  /$$$$$$                                 /$$| $$                     
 /$$__  $$                               | $$|__/                     
| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$  
| $$       /$$__  $$/$$__  $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$ 
| $$      | $$  \__/ $$$$$$$$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/ 
| $$    $$| $$     | $$_____/ /$$__  $$  | $$ /$$| $$  | $$| $$       
|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$       
 \______/ |__/      \_______/ \_______/   \___/   \______/ |__/       
                                                                      
                                                                      
                                                                                                                                                     
                                                                                                              ''')
    print('\nWelcome to the Random Group Creator! \n')


def main():
    welcome()
    temp_group = choose_group()
    screen_clear()
    number_of_group_members, number_of_groups = get_number_of_group_members(temp_group)
    final_groups = get_groups(temp_group, number_of_group_members, number_of_groups)
    screen_clear()
    print_groups(final_groups)
    choose_try_again()

if __name__ == '__main__':
    main()