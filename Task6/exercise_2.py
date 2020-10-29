from CustomList import CustomList, Node

if __name__ == '__main__':
    lst = CustomList()
    print('\n===== List of the attributes and methods of any object constructed using CustomList class =====\n')
    print(dir(lst))
    custom_methods = ['__init__', '__repr__', '__iter__', '__getitem__', '__setitem__', 'add', 'clear', 'find',
                      'remove_by_value', 'remove_by_index']
    print('\n===== Custom methods =====\n')
    for method in custom_methods:
        print(method)
