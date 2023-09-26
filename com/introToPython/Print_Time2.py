from Time_Lesson6_Assignment import Time

myTime1 = Time()
print(myTime1._Time__second)
myTime1.set_time(1,2,3)
print(myTime1.get_second())
print("Time is: " + str(myTime1.get_time()))

print(myTime1.__class__)

print(Time.__class__)