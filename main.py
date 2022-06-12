from random import randint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# reads text of restaurant.txt and stores it into restaurant list
def read_txt():
    with open('restaurants.txt', 'r') as restaurants_txt:
        # creates empty list
        restaurant_list = []

        # for loop --
        for restaurant in restaurants_txt:
            # reads the txt file line by line

            stripped_line = restaurant.strip()
            # appends the list with the contents of the txt file

            restaurant_list.append(stripped_line)

    # returns the new list
    return restaurant_list


# writes the contents of a list into a txt file
def write_txt(restaurant_list):
    # opens txt file in write mode
    with open('restaurants.txt', 'w') as txt_file:
        # for loop --
        for restaurant in restaurant_list:
            # writes "restaurants" from "restaurant list" into the txt file
            # del_empty_spaces(restaurant_list)
            txt_file.write(restaurant + "\n")


# uses randint to select a random integer from the length of restaurant list
def random_pick(restaurant_list):
    list_length = len(restaurant_list) - 1
    # creates and returns a random into from the designated length of list
    random_int = randint(0, list_length)
    return random_int


def pick_restaurant():
    # uses read_txt function to read in the txt file and to store its contents into an empty list
    restaurant_list = read_txt()

    if len(restaurant_list) > 0:
        # uses random_pick function to get a random int and pick it from the restaurant_list, list
        random_restaurant = random_pick(restaurant_list)

        # returns the pick it selected
        return restaurant_list[random_restaurant]

    else:
        return "# ERROR: No restaurants in list"


# appends restaurant.txt from user input and puts new restaurant at the end of the file
def append_restaurants(new_res):
    # read in text file with read_txt, which creates an empty list and stores txt contents in it
    restaurant_list = read_txt()

    # append list with new_res
    restaurant_list.append(new_res)

    write_txt(restaurant_list)


# deletes restaurant from restaurant.txt from user input
def delete_restaurants(del_res):
    # reads txt file for the restaurants
    restaurant_list = read_txt()

    # if the restaurant to be deleted is in that file then removes it
    if del_res in restaurant_list:

        # removes restaurant from list
        restaurant_list.remove(del_res)
        print(bcolors.OKBLUE + "+ Deleted " + del_res + " from the restaurant list" + bcolors.ENDC)

        # writes new list that excludes the deleted restaurant
        # del_empty_spaces(restaurant_list)
        write_txt(restaurant_list)

    # anything else, the restaurant cannot be found in the restaurant list
    else:
        print(bcolors.FAIL + "~ " + del_res + " could not be found on the list" + bcolors.ENDC)


# list the restaurants that are stored in the txt file
def list_restaurant():
    # reads in txt file as read and stores it into empty string
    restaurant_list = read_txt()
    # initialize count to use later to print number of restaurants in list
    count = 1

    # iterate over restaurants in restaurant list
    for restaurant in restaurant_list:
        # print restaurant and the count that it is at
        print("* " + str(count) + ": " + restaurant)
        # increase count
        count = count + 1


# delete all restaurants from txt file
def delete_all_restaurants():
    # reads txt file as write and writes it as an empty string
    with open('restaurants.txt', 'w') as txt_file:
        txt_file.write("")


def main():
    divider = "--------------------------------------------------------"
    print(divider)
    while True:
        # user picks a number from menu list
        choice = input("- Input '1' to choose a restaurant\n"
                       "- Input '2' to enter a new restaurant\n"
                       "- Input '3' to delete a restaurant\n"
                       "- Input '4' to list restaurants\n"
                       "- Input '5' to delete all restaurants\n"
                       '- Input "quit" to quit the program\n'
                       "+ Choice:  ")

        # if option is '1' -- choose restaurant
        if choice == '1':
            print(bcolors.OKBLUE + "+ The restaurant chosen is " + pick_restaurant() + "\n" + bcolors.ENDC + divider)

        # if option is '2' -- enter new restaurant
        elif choice == '2':
            new_res = input(bcolors.OKGREEN + '- Input a new restaurant (or type "cancel"):  ' + bcolors.ENDC)
            if new_res == 'cancel':
                print(bcolors.OKBLUE + "+ Input a restaurant was cancelled by user" + bcolors.ENDC + "\n" + divider)
                continue
            append_restaurants(new_res)
            print(bcolors.OKBLUE + "+ Inputted " + new_res + " into the restaurant list\n" + bcolors.ENDC + divider)

        # if option is '3' -- delete restaurant
        elif choice == '3':
            del_res = input(bcolors.OKGREEN + '- Input a restaurant to delete (or type "cancel"):  ' + bcolors.ENDC)
            if del_res == 'cancel':
                print(bcolors.OKBLUE + "+ Delete a restaurant was cancelled by user" + bcolors.ENDC + "\n" + divider)
                continue
            delete_restaurants(del_res)
            print(divider)

        # if option is '4' -- list restaurants
        elif choice == '4':
            print(bcolors.OKBLUE + "+ List of restaurants: " + bcolors.ENDC)
            list_restaurant()
            input("- Press any button to continue")
            print(divider)

        # if option is '5' -- delete all restaurants in list
        elif choice == '5':
            del_choice = input(bcolors.OKGREEN + '- Type "yes" to delete all or any key to quit: ' + bcolors.ENDC)
            if del_choice == "yes":
                delete_all_restaurants()
                print(bcolors.OKBLUE + "+ Deleted all restaurants from list\n" + bcolors.ENDC + divider)
            else:
                print(divider)

        # if option is 'quit' -- quit the program
        elif choice == "quit":
            print(divider)
            print("Bye")
            break

        # anything else is invalid
        else:
            print(bcolors.FAIL + "~ " + choice + " is not a valid option dummy\n" + bcolors.ENDC + divider)


# calls main
if __name__ == '__main__':
    main()
