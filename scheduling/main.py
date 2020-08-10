from random import random
from random import seed
from random import choice
from random import randint
from random import sample
from random import shuffle
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
    def __init__(self, id, time, day, isAvailable= True):
        self._id                = id
        self._time              = time
        self._day               = day
        self._isAvailable       = isAvailable

    def get_id(self):               return self._id
    def get_time(self):             return self._time
    def get_day(self):              return self._day
    def get_isAvailable(self):      return self._isAvailable
    
    def set_Available(self):         self._isAvailable = True
    def set_Occupied(self):          self._isAvailable = False
    


    def __str__(self): 
        return  f'TimeID:{self.get_id()}\n' \
                f'{self.get_time()}\t' \
                f'Occupied:{self.get_isAvailable()}'

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

    def get_id(self):       return self._id    
    def get_times(self):    return self._times 
    
    def get_listOfClasses(self):
        return self._listOfClasses
    
    def get_listOfClassesStr(self):
        holder = ""
        for each in self._listOfClasses:
            holder += str(each.get_time()) + str(each.get_course()) + str(each.get_room())
        return holder
    
    def add_class(self, myClass):
        self._listOfClasses.append(myClass)
        self._classCounter += 1
       
    # This method perform checks looping over Courses(times per week), Times (availability) and Rooms (capacity) 
    # and appends a new class to the Schedule if everything is ok.
    def initialize(self):
        counter         = 0
        roomList        = sorted(ROOMS,   key = lambda y: y._capacity,  reverse = True)
        coursesList     = sorted(COURSES, key = lambda x: x._students,  reverse = True)
        for course in coursesList:                                  # loop over courses
            for i in range(course.get_timesPerWeek()):              # how many classes per week
                for time in self._times:                            # loop and verify each time
                    if (time.get_isAvailable()):                     # for availability
                        for room in roomList:                       
                            if (course.get_students() <= room.get_capacity()): # check capacity for each room
                                time.set_Occupied()
                                myClass = Class(counter,course,time,room)
                                counter += 1                        #id counter
                                self.add_class(myClass)
                            else:
                                self._rejectedIterations += 1
                            break
                        break
        return self
    
    def sort_classes(self):
        self._listOfClasses.sort(key = lambda x : x._time.get_id())
        
    def print_grid(self):
        for day in DAYS:
            print("\t\t  ",day,end = "")
        print("\n")
        for time in TIMESSTR:
            print(time,end = "\t")
            for day in DAYS:
                for eachClass in self._listOfClasses:
                    if eachClass._time.get_time() == time:
                        if eachClass._time.get_day() == day:
                            print(f'{eachClass._course.get_id()} = '\
                                  f'{eachClass._room.get_id()}',
                                  end = "\t\t ")
            print('\n','-'*150)

    def print_grid_with_allocation(self):
        for day in DAYS:
            print("\t\t  ",day,end = "")
        print("\n")
        for time in TIMESSTR:
            print(time,end = "\t")
            for day in DAYS:
                for eachClass in self._listOfClasses:
                    if eachClass._time.get_time() == time:
                        if eachClass._time.get_day() == day:
                            print(f'{eachClass._course.get_id()}:'\
                                  f'{eachClass._course.get_students()} '\
                                  f'{eachClass._room.get_id()}:'\
                                  f'{eachClass._room.get_capacity()}',
                                  end = "  \t")
            print('\n','-'*150)

    
    
    def __str__(self): 
        return str(self.print_grid())
                
                
class AllRndSchedule(Schedule):
    def initialize(self):
        counter         = 0
        roomList        = generate_rand_room_list()
        coursesList     = generate_rand_courses_list()
        self._times     = generate_rand_times_list()

        for course in coursesList:
            for i in range(course.get_timesPerWeek()):             #4x
                for time in self._times:        #30x                # loop and verify each time
                    if (time.get_isAvailable()):         # for availability
                        for room in roomList:   #6x
                            if (course.get_students() <= room.get_capacity()): # check capacity for each room
                                time.set_Occupied()
                                myClass = Class(counter,course,time,room)
                                counter += 1                        #id counter
                                self._listOfClasses.append(myClass)
                                break   # breaks room loop by the next time availability check
                        break           # breaks range(loop)
        return self

#--------------------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------------------
def create_times(DAYS,TIMESSTR):
    # generates time list from TIMESSTR
    times   = []
    counter = 0
    for i in range(len(DAYS)):     # 5 days
        for j in range(len(TIMESSTR)): # 6 times per day
            counter += 1
            times.append(Time(counter,TIMESSTR[j], DAYS[i]))
    return times

def generate_rand_room_list():
    rndRoomList = ROOMS
    shuffle(rndRoomList)
    return rndRoomList

def generate_rand_courses_list():
    rndCoursesList = COURSES
    shuffle(rndCoursesList)
    return rndCoursesList

def generate_rand_times_list():
    rndTimesList = TIMES
    shuffle(rndTimesList)
    return rndTimesList

#--------------------------------------------------------------------------------
# Sample Data
#--------------------------------------------------------------------------------
DAYS = [
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY',
    'THURSDAY',
    'FRIDAY'
]

TIMESSTR = [
    "19:00-19:50",
    "19:50-20:40",
    "21:00-21:50",
    "21:50-22:40",
]

TIMES = create_times(DAYS,TIMESSTR)

COURSES = [
    #(id, students, times per week),
    Course("SIGA5", 30, 4),
    Course("GTIA5", 25, 4),
    Course("DW1A5", 30, 4),
    Course("ENGA5", 45, 4),
    Course("PR1A5", 45, 4),
]

ROOMS = [
    #    id , capacity
    Room("ROOM 1", 25),
    Room("ROOM 2", 30),
    Room("ROOM 3", 40),
    Room("ROOM 4", 45),
]

#--------------------------------------------------------------------------------
#   Runner Code
#--------------------------------------------------------------------------------

if __name__=="__main__":
    allRndSchedule = AllRndSchedule(1)
    allRndSchedule.initialize()
    print("Created and Initialized Schedule.")
    allRndSchedule.sort_classes()
    print()
    print("*"*150, "\n\t\tSchedule\n","*"*150)
    allRndSchedule.print_grid()
    print()
    print("*"*150, "\n\t\tSchedule with Allocation Info\n","*"*150)
    allRndSchedule.print_grid_with_allocation()
    print(f'\nTotal Number of classes:{len(allRndSchedule.get_listOfClasses())}')
