'''
    The open function enables us open a file from an external source.
    The path of the file is put as a parameter in the function.
    It could be relative/absolute path. or just typing
    file name if the .py file and
    the file to be opened are in the same folder.
    The open() should be inside a variable.
'''
'''
    The different things an open function might perform (i.e modes of the function)
    "w" = write. It allows you delete and add info.
    "r" = read. You can only read the file.
    "r+" = read and write.
    "a" = append. You can't delete or modify previous stuff, but you can definitely add.
                    You can only append.

'''
employee_file = open("employees.txt", "w")

print(employee_file.readable())#how to check if a file is readable
print()

employee_file.close() #It is important to close a file after opening it.