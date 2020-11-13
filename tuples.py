#tuples are immutable (i.e they can't be changed.)

coordinates = (4, 5)
# coordinates[1] = 10 ---> This can't happen because tuples are immutable.
print(coordinates[1])

#Difference between tuple and list
#tuple: (), list: []. 
#tuple:immutable, list: Can be changed. Tuples are used for data that are never going to be changed.
 #a list of tuples can be made though.
 #E.g coordinates = [(4, 5), (6, 7), (80, 34)]