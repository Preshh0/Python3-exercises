
# import time
# time.time()
# seconds = time.time()
# local_time = time.ctime(seconds)
    
# name = input("Please input your name: ")
# print("Hello %r, what's the time?" %name)
# print("Please input time in 24-hour format. E.g: 12:00.")
# print ("Local time is:", local_time)

# if local_time >= "00:00" and local_time <= "11:59":
#     print("Hey %r, Good Morning." %name)
# elif local_time >= "12:00" and local_time <= "15:59":
#     print("Hey %r, Good Afternoon." %name)
# elif local_time >= "16:00" and local_time <= "20:59":
#     print("Hey %r, Good Evening." %name)
# elif local_time >= "21:00" and local_time <= "23:59":
#     print("Hey %r, Good Morning." %name)
# else: 
#     print("Hey %r, The number is invalid." %name)

name = input("Please input your name: ")
print("Hello %r, what's the time?" %name)
print("Please input time in 24-hour format. E.g: 12:00.")
time = input("Time is: ")

if time >= "00:00" and time <= "11:59":
    print("Hey %r, Good Morning." %name)
elif time >= "12:00" and time <= "15:59":
    print("Hey %r, Good Afternoon." %name)
elif time >= "16:00" and time <= "20:59":
    print("Hey %r, Good Evening." %name)
elif time >= "21:00" and time <= "23:59":
    print("Hey %r, Good Morning." %name)
else: 
    print("Hey %r, The number is invalid." %name)



  