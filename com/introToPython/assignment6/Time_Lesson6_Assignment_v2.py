class Time:
   """Blueprint for a Time object"""
   def __init__(self):
      self.__hour = 0
      self.__minute = 0
      self.__second = 0

   # def set_time(self, hour, minute, second):
   #    self.__hour = hour
   #    self.__minute = minute
   #    self.__second = second
   #
   # def get_time(self):
   #    return self.__hour, self.__minute, self.__second

   def print_time(self):
      print (self.__hour, ":", self.__minute, ":", self.__second)

   def set_hour(self, hour):
      if (hour > 23):
         print('Hour cannot be larger than 23')
      else:
         self.__hour = hour

   def get_hour(self):
      return self.__hour

   def set_minute(self, minute):
      if (minute > 59):
         print('Minute cannot be larger than 59')
      else:
         self.__minute = minute

   def get_minute(self):
      return self.__minute

   def set_second(self, second):
      if (second > 59):
         print('Second cannot be larger than 59')
      else:
         self.__second = second

   def get_second(self):
      return self.__second


   def tick(self):
      if (self.__second < 59):
         self.__second += 1
      else:
         print('Incrementation should not move time to the next minute or hour. Incrementation will stop here')
         print('Final Time is: ' + str(self.__hour) + ":" + str(self.__minute) + ":" +str(self.__second))
         exit()





