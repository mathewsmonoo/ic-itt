from random import random
from random import seed
from random import choice
from random import randint
from datetime import datetime
#--------------------------------------------------------------------------------
# Classes
#--------------------------------------------------------------------------------
class Room:
    def __init__(self, id, capacity):
        self._id        = id
        self._capacity  = capacity

    def get_id(self):           return self._id
    def get_capacity(self):     return self._capacity

    def __str__(self): 
        return  f'ROOM: {self.get_id()}\t' \
                f'Capacity:{self.get_capacity()}\n\n'

class Course:
    def __init__(self, id, students, timesPerWeek):
        self._id                = id
        self._students          = students
        self._timesPerWeek      = timesPerWeek

    def get_id(self):               return self._id
    def get_students(self):         return self._students
    def get_timesPerWeek(self):     return self._timesPerWeek

    def __str__(self): 
        return  f'\nCourseID:{self.get_id()}\t' \
                f'Students:{self.get_students()}\t' \
                f'Times Per Week:{self.get_timesPerWeek()}\n'

class Time:
    def __init__(self, id, time, isOccupied = False):
        self._id                = id
        self._time              = time
        self._isOccupied        = isOccupied

    def get_id(self):               return self._id
    def get_time(self):             return self._time
    def get_isOccupied(self):       return self._isOccupied
    
    def change_isOccupied(self):    self._isOccupied = not(self._isOccupied)


    def __str__(self): 
        return  f'TimeID:{self.get_id()}\n' \
                f'{self.get_time()}\t' \
                f'Occupied:{self.get_isOccupied()}'

class Class:
    def __init__(self, id, course, time = '', room = ''):
        self._id                = id
        self._course            = course
        self._time              = time
        self._room              = room

    def get_id(self):         return self._id
    def get_course(self):     return self._course
    def get_time(self):       return self._time  
    def get_room(self):       return self._room  

    def set_course(self, course):   self._course  = course
    def set_time(self, time):       self._time    = time
    def set_room(self, room):       self._room    = room

    def __str__(self): 
        return  f'ClassID:{self.get_id()}\n' \
                f'Course:{self.get_course()}\n' \
                f'Time:{self.get_time()}\n' \
                f'Room:{self.get_room()}'

class Schedule:
    def __init__(self, id):
        self._id                 = id
        self._times              = []
        self._listOfClasses      = []
        self._rejectedIterations = 0
        
        for i in (TIMES):
            self._times.append(i)

    def get_id(self):   return self._id    
    
    def get_listOfClasses(self):
        holder = ""
        for each in self._listOfClasses:
            holder += str(each.get_time()) + str(each.get_course()) + str(each.get_room())
        return holder
    
    def add_class(self, myClass):
        self._listOfClasses.append(myClass)
       
    # This method perform checks looping over Courses(times per week), Times (availability) and Rooms (capacity) 
    # and appends a new class to the Schedule if everything is ok.
    def initialize(self):
        counter         = 0
        roomList        = sorted(ROOMS,   key = lambda y: y._capacity,  reverse = True)
        coursesList     = sorted(COURSES, key = lambda x: x._students,  reverse = True)
        for course in coursesList:                                  # loop over courses
            for i in range(course.get_timesPerWeek()):              # how many classes per week
                for time in self._times:                            # loop and verify each time
                    if (time.get_isOccupied() == False):                     # for availability
                        for room in roomList:                       
                            if (course.get_students() <= room.get_capacity()): # check capacity for each room
                                time.change_isOccupied() 
                                myClass = Class(counter,course,time,room)
                                counter += 1                        #id counter
                                self._listOfClasses.append(myClass)
                            else:
                                self._rejectedIterations += 1
                            break
                        break
        return self

    def __str__(self): 
        return  f'ScheduleID:{self.get_id()}\n' \
                f'Classes:\n{self.get_listOfClasses()}'

#--------------------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------------------
def create_times():
    # generates time list from TIMESSTR
    times   = []
    counter = 0
    for i in range(5):     # 5 days
        for j in range(6): # 6 times per day
            counter += 1
            times.append(Time(counter,TIMESSTR[j]))
    return times
#--------------------------------------------------------------------------------
# Sample Data
#--------------------------------------------------------------------------------

TIMESSTR = [
    "07:30 - 08:20",
    "08:20 - 09:10",
    "09:30 - 10:20",
    "10:20 - 11:10",
    "11:20 - 12:10",
    "12:10 - 13:00"
]

TIMES = create_times()

COURSES = [
    #     (id, students, times per week),
    Course("C1", 20, 4),
    Course("C2", 25, 2),
    Course("C3", 45, 6),
    Course("C4", 30, 3),
    Course("C5", 35, 4),
    Course("C6", 25, 2),
    Course("C7", 45, 2),
]

ROOMS = [
    #    id , capacity
    Room("R1", 25),
    Room("R2", 30),
    Room("R3", 45),
    Room("R4", 40),
    Room("R5", 35),
    Room("R6", 45),
]

#--------------------------------------------------------------------------------
#   Runner Code
#--------------------------------------------------------------------------------

if __name__=="__main__":
    sampleSchedule = Schedule(1)  #create Schedule
    sampleSchedule.initialize()   #init schedule
    print(sampleSchedule)