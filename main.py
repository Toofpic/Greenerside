# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('it\'s Greenerside!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Item:
    def __init__(self, title, itemtype, itemstate, gradient):
        self.title = title
        self.itemtype = itemtype
        self.itemstate = itemstate
        self.gradient = gradient

# making test entity to see if the class works - remove later
Task1 = Item('Task1', 'project', 'active', 2)

print(Task1.title, Task1.itemtype, Task1.itemstate, Task1.gradient)
# end of making test entity to see if the class works - remove later