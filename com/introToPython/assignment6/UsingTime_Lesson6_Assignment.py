from Time_Lesson6_Assignment_v2 import Time

myTime = Time()
print("Blue Print is: " + myTime.__doc__)
print('Time before setting')
myTime.print_time()
print('Now set time to 20:30:30')
myTime.set_hour(20)
myTime.set_minute(30)
myTime.set_second(30)
print('This is Time Now')
myTime.print_time()
# myTime.tick()

print('Now let\'s increment by 1 second now.')
for i in range(myTime.get_second(), 60, 1):
    myTime.tick()
    myTime.print_time()



