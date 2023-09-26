class Time:
    """The blueprint for a Time Class Object"""
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def print_time(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)

import pickle
# from pickle import dumps
# from time import time
myTime1 = Time(1,2,3)
# pickled_time = pickle.dumps(myTime1)
# print(pickled_time)

out_file = open('data.txt', 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()