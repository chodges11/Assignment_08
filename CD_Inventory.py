# -----------------------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Beginning Object-Oriented Programming
# Change Log: (Who, When, What)
# Charles Hodges(hodges11@uw.edu), 2021-Aug-29, created file
# -----------------------------------------------------------#

import pickle

# -- DATA -- #
# String Variables
str_file_name = 'cdInventory.dat'
str_menu = (
    '\n'
    'MENU\n\n'
    '[l] Load Inventory from file\n'
    '[a] Add CD\n'
    '[i] Display Current Inventory\n'
    '[s] Save Inventory to file\n'
    '[x] Exit\n'
    )
str_which_operation = (
    'Which operation would you like to perform?'
    '[l, a, i, s, or x]: '
    )

# Non-String Variables
lst_input_options = ['l', 'a', 'i', 's', 'x']
lst_of_cd_objects = []


class CD():
    """Stores data about a CD.

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        increment_cd: Increments the counter for each CD object created
        how_many_cds: returns number of CDs objects created
    """

    # Constructor
    def __init__(self, cd_id, cd_title, cd_artist):
        # Attributes
        print("\nA new CD was created!\n")
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist

    # Getter and Setter for the CD's ID number
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, cd_id):
        self.__cd_id = cd_id

    # Getter and Setter for the CD's Title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, cd_title):
        self.__cd_title = cd_title

    # Getter and Setter for the CD's Artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, cd_artist):
        self.__cd_artist = cd_artist

    # Methods
    def __str__(self):
        """Represents the class objects as a string."""
        return ('{: <7} {: <20} {: <20}'.format(
            str(self.__cd_id), str(self.__cd_title), str(self.__cd_artist)))


# -- PROCESSING -- #
class FileIO():
    """Processes data to and from a file.

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

    @staticmethod
    def save_inventory(str: str_file_name, list: lst_of_cd_objects) -> None:
        """Function to save a file.

        After the User either confirms or declines saving this function
        processes the answer and either completes the objective to save, or
        returns the User back to the menu.

        Args:
            str_file_name(string): File name where the data will be saved
            lst_of_cd_objects(list): List to hold data

        Returns:
            None.
        """
        # Save data
        obj_file = open(str_file_name, 'wb')
        pickle.dump(lst_of_cd_objects, obj_file)
        obj_file.close()
        print("\nInventory saved to file.\n")

    @staticmethod
    def load_inventory(str_file_name, lst_of_cd_objects):
        """Function to manage data ingestion from file to a list of
           CD Objects.

        Reads the data from file identified by file_name into a 2D table
        (list of CD objects).

        Args:
            str_file_name(string): File name from which the data will be read
            lst_of_cd_objects(list): List of lists to hold data

        Returns: None.
        """
        # Clears existing data
        lst_of_cd_objects.clear()

        # Loads data from file
        obj_file = open(str_file_name, 'rb')
        try:
            lst_of_cd_objects = pickle.load(obj_file)
        except EOFError:
            pass
        obj_file.close()
        print("\nInventory loaded from file.")
        return lst_of_cd_objects

    @staticmethod
    def create_file(str: str_file_name) -> None:
        """Function to create a binary file.

        Args:
            str_file_name(string): File name where the data will be saved

        Returns:
            None.
        """
        # Create file with temp file object and close it immediately
        obj_file = open(str_file_name, 'ab')
        obj_file.close()


# -- PRESENTATION (Input/Output) -- #
class IO():
    """Processes Input from the User, and Output to the User.

    methods:
    print_menu(str_menu): Prints a string displaying the menu of options
    menu_choice(): Requests and accepts user input of their selection
    show_inventory(lst_of_cd_objects): Shows current inventory of CD objects
    add_cd(lst_of_cd_objects): Allows User to create a new CD object
    """

    @staticmethod
    def print_menu(str_menu):
        """Displays a menu of choices to the user.

        Args:
            str_menu(string): User options to interact with their Inventory

        Returns:
            None.
        """
        print(str_menu)

    @staticmethod
    def menu_choice():
        """Requests and accepts user input for menu selection.

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input, out of
            the choices: l, a, i, s, or x
        """
        choice = ' '
        while choice not in lst_input_options:
            choice = input(str_which_operation).lower().strip()
        print()  # Add extra line for layout
        return choice

    @staticmethod
    def show_inventory(list: lst_of_cd_objects) -> None:
        """Show the User their inventory, if any.

        Args:
            lst_of_cd_objects(list): List to hold data

        Returns:
            None.

        """
        print('\n======= The Current Inventory: =======')
        print("{: <5} {: <20} {: <20}".format("ID", "| CD Title", "| Artist"))
        print("{: <5} {: <20} {: <20}".format("--", "| --------", "| ------"))
        counter = 0
        for row in lst_of_cd_objects:
            cd = lst_of_cd_objects[counter]
            print(cd)
            counter += 1
        print('======================================')

    @staticmethod
    def add_cd(list: lst_of_cd_objects) -> None:
        """Create a CD object and add it the User's Inventory'.

        Accepts the User input of new CD information, and creates a CD
        object, which is appended to the list table which makes up the
        Inventory.

        Args:
            lst_of_cd_objects(list): List of CD Objects

        Returns:
            lst_of_cd_objects(list): Updated list of CD Objects
        """
        # Collect the CD ID
        while True:
            try:
                cd_id = int(input("Enter the ID number of your CD: "))
                break
            except ValueError:
                print("Please only enter whole numbers.")
        # Collect the CD Title
        cd_title = input("Enter the Title of the CD: ")
        # Collect the CD Artist's Name
        cd_artist = input("Enter the Artist who created the CD: ")
        # Create a CD object with the provided information and
        # append that CD object to list of CD objects
        lst_of_cd_objects.append(CD(cd_id, cd_title, cd_artist))
        IO.show_inventory(lst_of_cd_objects)
        return lst_of_cd_objects


# -- Main -- #
# When program starts, read in the currently saved Inventory, if it exists.
# Otherwise, create the inventory file.
try:
    lst_of_cd_objects = FileIO.load_inventory(str_file_name, lst_of_cd_objects)
except FileNotFoundError:
    FileIO.create_file(str_file_name)

# Start main loop
while True:
    # Display Menu to user, and get choice
    IO.print_menu(str_menu)
    str_choice = IO.menu_choice()

    # Exit
    if str_choice == 'x':
        break

    # Load Inventory.
    if str_choice == 'l':
        lst_of_cd_objects = FileIO.load_inventory(
            str_file_name, lst_of_cd_objects)
        continue  # start loop back at top.

    # Add a CD.
    elif str_choice == 'a':
        # Ask user for new ID, CD Title and Artist,
        lst_of_cd_objects = IO.add_cd(lst_of_cd_objects)
        continue  # start loop back at top.

    # Display current inventory.
    elif str_choice == 'i':
        IO.show_inventory(lst_of_cd_objects)
        continue  # start loop back at top.

    # Save inventory to file.
    elif str_choice == 's':
        FileIO.save_inventory(str_file_name, lst_of_cd_objects)
        continue  # start loop back at top.

    # A catch-all, which should not be possible, as user choice gets
    # vetted in IO, but to be safe.
    else:
        print("General Error!")
