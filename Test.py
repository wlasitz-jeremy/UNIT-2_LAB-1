def show_welcome():
    """ Function to show welcome message """
    print("Hello to the library!")
def display_books():
    """ Function to display books """
    print("Here are our books...")
def issue_books():
    """ Function to issue books """
    print("This book is for you!")
def return_books():
    """ Function to return books """
    print("Thank-you for returning the books!")
print(f"{show_welcome.__doc__}\n"
      f"{display_books.__doc__}\n"
      f"{issue_books.__doc__}\n"
      f"{return_books.__doc__}\n")
show_welcome()
display_books()
issue_books()
return_books()


