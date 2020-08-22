# Most 'succesful' code ; STANDALONE code.
# But contains gaps in some times
    # To fix this we need to randomize the rooms for each COURSE iteration
from datetime import datetime
from random import random, seed, shuffle, choice

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------
class Room:
    def __init__(self, id, capacity):
        self._id              = id
        self._capacity        = capacity

    def get_id(self):              return self._id
    def get_capacity(self):        return self._capacity

    def __str__(self):
        return  f'ROOM: {self.get_id()}\t' \
                f'Capacity:{self.get_capacity()}\n'

class Course:
    def __init__(self, id, name, students, teacher, times_per_week):
        self._id                = id
        self._name              = name
        self._students          = students
        self._teacher           = teacher
        self._times_per_week    = times_per_week
        self._compatible_rooms  = self.check_compatible_rooms()

    def get_id(self):               return self._id
    def get_name(self):             return self._name
    def get_students(self):         return self._students
    def get_teacher(self):          return self._teacher
    def get_times_per_week(self):   return self._times_per_week
    def get_compatible_rooms(self): return self._compatible_rooms
    
    def check_compatible_rooms(self):
        compatible_rooms = []
        for room in ROOMS:
            if room.get_capacity() >= self.get_students():
                compatible_rooms.append(room)
        return compatible_rooms

    def __str__(self):
        return  f'Course:{self.get_id()}-{self.get_name()}'

class Department:
    def __init__(self, id, name, courses_list = []):
        self._id           = id
        self._name         = name
        self._courses_list = courses_list
        
    def set_courses_list(self, courses_list) : self._courses_list = courses_list 

    def get_id(self):           return self._id
    def get_name(self):         return self._name
    def get_courses_list(self): return self._courses_list

class Time:
    def __init__(self, id, day, time):
        self._id    = id
        self._day   = day
        self._time  = time

    def get_id(self):    return self._id
    def get_day(self):   return self._day
    def get_time(self):  return self._time


    def __str__(self):
        return  f'Time:{self.get_id()} {self.get_day()} {self.get_time()}\n'

class Class:
    def __init__(self, id, course, time = '', room = ''):
        self._id      = id
        self._course  = course
        self._time    = time
        self._room    = room

    def get_id(self):      return self._id
    def get_course(self):  return self._course
    def get_time(self):    return self._time
    def get_room(self):    return self._room

    def set_course(self, course):  self._course  = course
    def set_time(self, time):      self._time    = time
    def set_room(self, room):      self._room    = room

    def __str__(self): 
        return  f'ClassID:{self.get_id()}\n' \
                f'Course:{self.get_course()}\n' \
                f'Time:{self.get_time()}\n' \
                f'Room:{self.get_room()}'
                       
ROOMS = [
    #    id , capacity
    Room("R1", 25),
    Room("R2", 30),
    Room("R3", 25),
    Room("R4", 45),
    Room("R5", 40),
]

DEPT1_COURSES = [
    Course(1, "SIGA5", 30, 'T1', 4),
    Course(2, "GTIA5", 25, 'T2', 4),
    Course(3, "DW1A5", 30, 'T3', 4),
    Course(4, "ENGA5", 45, 'T4', 4),
    Course(5, "PR1A5", 15, 'T5', 4),
]

DEPT2_COURSES = [
    Course(6,  "11111", 25, 'T6', 4),
    Course(7,  "22222", 35, 'T7', 4),
    Course(8,  "33333", 30, 'T8', 4),
    Course(9,  "44444", 45, 'T9', 4),
    Course(10, "55555", 20, 'T0', 4),
]

DEPARTMENTS = [
    Department(1,'DEPT1', DEPT1_COURSES),
    Department(2,'DEPT1', DEPT2_COURSES),
]

DAYS_OF_WEEK = [
    'SEG',
    'TER',
    'QUA',
    'QUI',
    'SEX',
]

TIME_SLOTS = [
    '19:00-19:50',
    '19:50-20:40',
    '21:00-21:50',
    '21:50-22:40',
]


class SingleRandomSchedule:
    def __init__(self, id, courses_list, occupied_room_times):
        self._id                  = id
        self._times               = []
        self._courses_list        = courses_list
        self._list_of_classes     = []
        self._occupied_room_times = occupied_room_times
        self._conflicts           = 0
        self._fitness             = -1

    def get_times(self):                return self._times
    def get_occupied_rooms_times(self): return self._occupied_room_times
    def get_courses_list(self):         return self._courses_list
    def get_list_of_classes(self):      return self._list_of_classes
    def get_conflicts(self):            return self._conflicts
    def get_fitness(self):              return self._fitness
    
    def add_class(self, new_class):
        self._list_of_classes.append(new_class)
    
    def add_occupied_room_time(self, room, time):
        room_id = room.get_id()
        time_id = time.get_id()
        holder  = []
        if room_id in self._occupied_room_times.keys():
            holder += self.get_occupied_rooms_times().get(room_id)
            holder.append(time_id)
        else:
            holder.append(time_id)
        self._occupied_room_times[room_id] = holder


    def add_conflict(self):
        self._conflicts += 1

    def calculate_fitness(self):
        self._fitness = (1 / ((self.get_conflicts()) + 1)*100)

    def init_times(self, days, time_slots):
        counter = 0
        for day in days:
            for time in time_slots:
                counter += 1
                self._times.append(Time(counter, day, time))

    def initialize(self):
        seed = (datetime.now())
        self.init_times(DAYS_OF_WEEK, TIME_SLOTS)
        counter      = 0
        courses_list = self._courses_list
        shuffle(courses_list)
        times_list   = self._times
        shuffle(times_list)
        for course in courses_list:
            compatible_rooms = course.check_compatible_rooms()
            for j in range(course.get_times_per_week()):    # How many classes per week
                allocated = False
                while allocated == False:
                    room = choice(compatible_rooms)
                    time = choice(times_list)
                    if check_available_room(room, time, self.get_occupied_rooms_times()):
                        new_class = Class(counter, course, time, room)
                        counter  += 1
                        self.add_class(new_class)
                        self.add_occupied_room_time(room, time)
                    allocated = True

                        
        self.calculate_fitness()
        return self

    def print_grid(self):
        print(end="\t\t")
        for day in DAYS_OF_WEEK:
            print(day,end="\t\t")
        print('\n')    
        for time_slot in TIME_SLOTS:
            print(time_slot, end="\t")
            for day in DAYS_OF_WEEK:
                for each_class in self.get_list_of_classes():
                    if ((each_class._time.get_day() == day) and (each_class._time.get_time() == time_slot)):
                        print(f'{each_class._course.get_name()}('\
                              f'{each_class._room.get_id()})',
                              end = "\t")
            print('\n','-'*100)
        print(f'Conflicts: {self.get_conflicts()}')                        
        print(f'Fitness:   {self.get_fitness()}')                        

    def try_print(self):
        for i in self.get_list_of_classes():
            print(i._course.get_name(),'-',i._room.get_id())

#------------------------------------------------------------------------------
# Check Functions
#------------------------------------------------------------------------------

# *** Hard constraints ***
def check_available_room(room, time, occupied_room_times):
    room_id  = room.get_id()
    time_id  = time.get_id()
    keys     = occupied_room_times.keys()
    occupied = occupied_room_times.get(room_id)
    if (room_id not in keys):
        return True
    else:
        if time_id not in occupied:
            return True
        else:
            return False

#------------------------------------------------------------------------------
# Runner Function
#------------------------------------------------------------------------------
def create_rand_schedule(i, courses_list, occupied_rooms_times):
    random_schedule = SingleRandomSchedule(i, courses_list, occupied_rooms_times)
    random_schedule.initialize()
    return random_schedule

if __name__=="__main__":
    OCCUPIED_ROOMS_TIMES  = {}
    
    sing_sched            = create_rand_schedule(1, DEPT1_COURSES, OCCUPIED_ROOMS_TIMES)
    OCCUPIED_ROOMS_TIMES.update(sing_sched.get_occupied_rooms_times())
    
    singl_sched           = create_rand_schedule(2, DEPT2_COURSES, OCCUPIED_ROOMS_TIMES)
    OCCUPIED_ROOMS_TIMES.update(singl_sched.get_occupied_rooms_times())
    
    sing_sched.print_grid()
    singl_sched.print_grid()
    
    all_available = {}
    for room in ROOMS:
        for i in range(len(TIME_SLOTS)*len(DAYS_OF_WEEK)):
            holder = {}
            holder.add(i)
        all_available[room.get_id()] = holder
    print(all_available)
