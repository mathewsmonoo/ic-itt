from datetime import datetime
from random import random, seed, shuffle, choice

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------
class Room:
    def __init__(self, id, capacity):
        self._id              = id
        self._capacity        = capacity
        self._occupied_times  = []
        self._available_times = self.set_all_times_available()

    def get_id(self):                     return self._id
    def get_capacity(self):               return self._capacity
    def get_occupied_times(self):         return self._occupied_times
    def get_available_times(self):        return self._available_times
    
    def add_occupied_time(self, time):    self._occupied_times.append(time.get_id())
    def remove_available_time(self,time): self._available_times.remove(time.get_id())
    
    def set_all_times_available(self , size= 20):
        holder = []
        for i in range(size):
            holder.append(i)
        return holder

    def __str__(self):
        return  f'ROOM: {self.get_id()}\t' \
                f'Capacity:{self.get_capacity()}\t' \
                f'Occupied at:{self.get_occupied_times()}\t' \
                f'\t\tAvailable at:{self.get_available_times()}\n'

ROOMS = [
    #    id , capacity
    Room("R1", 50),
    Room("R2", 40),
    Room("R3", 30),
    Room("R4", 35),
    Room("R5", 50),
    Room("R6", 45),
]


class Course:
    def __init__(self, id, name, qty_students, teacher, times_per_week):
        self._id                = id
        self._name              = name
        self._qty_students      = qty_students
        self._teacher           = teacher
        self._times_per_week    = times_per_week
        self._compatible_rooms  = self.set_compatible_rooms(ROOMS)
        self._rand_compatible_rooms  = self.set_rand_compatible_rooms()

    def get_id(self):               return self._id
    def get_name(self):             return self._name
    def get_qty_students(self):     return self._qty_students
    def get_teacher(self):          return self._teacher
    def get_times_per_week(self):   return self._times_per_week
    def get_compatible_rooms(self): return self._compatible_rooms
    def get_rand_compatible_rooms(self): return self._rand_compatible_rooms
    
    def set_compatible_rooms(self, room_list = ROOMS):
        holder = []
        for room in room_list:
            if room.get_capacity() >= self.get_qty_students():
                holder.append(room)
        return holder
    
    def set_rand_compatible_rooms(self):
        holder = self.get_compatible_rooms()
        shuffle(holder)
        return holder
            
        

    def __str__(self):
        return  f'Course:{self.get_id()}::{self.get_name()}'

class Department:
    def __init__(self, id, name, courses_list):
        self._id           = id
        self._name         = name
        self._courses_list = courses_list
        
    def get_id(self):           return self._id
    def get_name(self):         return self._name
    def get_courses_list(self): return self._courses_list

class Time:
    def __init__(self, id, day, time):
        self._id    = id
        self._day   = day
        self._time  = time
        self._isOccupied = False

    def get_id(self):           return self._id
    def get_day(self):          return self._day
    def get_time(self):         return self._time
    def get_isOccupied(self):   return self._isOccupied

    def set_occupied(self):     self._isOccupied = True

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
                       

class Schedule:
    def __init__(self, id, department):
        self._id             = id
        self._times          = create_times(DAYS_OF_WEEK, TIME_SLOTS)
        self._courses_list   = department.get_courses_list()
        self._classes_list   = []
        self._occupied_times = []
        self._conflicts      = 0
        
    def get_times(self):              return self._times
    def get_courses_list(self):       return self._courses_list
    def get_classes_list(self):       return self._classes_list
    def get_occupied_times(self):     return self._occupied_times
    def get_conflicts(self):          return self._conflicts
    def get_fitness(self):            return (1 / ((self.get_conflicts()) + 1)*10)
    def get_classes_num(self):        return (len(self.get_classes_list()))
    
    def add_conflict(self):                             self._conflicts += 1 
    def add_occupied_time(self,time):                   self._occupied_times.append(time.get_id()) 
    def add_class(self, new_class):                     self._classes_list.append(new_class)
    def overwrite_class(self, position, new_class) :   self._classes_list[position] = new_class
    
    def initialize(self):
        counter = 0
        for course in self.get_courses_list():                                      # Each course
                counter = 0                                                         # Reset counter
                for room in course.get_rand_compatible_rooms():
                    for time in self.get_times():                       
                        if time.get_isOccupied() == False:                          # This schedule time not occupied
                            if time.get_id() in room.get_available_times():         # Check if this time is in random room's list of available times
                                if time.get_id() not in self.get_occupied_times():  # Check if this time is not in local occupied times
                                    self.add_occupied_time(time)
                                    room.add_occupied_time(time)
                                    room.remove_available_time(time)
                                    time.set_occupied()
                                    new_class = Class(counter, course, time, room)
                                    self.add_class(new_class)
                                    counter += 1
                                else:
                                    self.add_conflict()
                            else:
                                self.add_conflict()
                        else:
                            self.add_conflict()   
                        if counter == course.get_times_per_week():
                            break
                    if counter == course.get_times_per_week():
                        break
        return self

    def print_grid(self):
        print('\n')
        print(end="\t\t")
        for day in DAYS_OF_WEEK:
            print(day,end="\t\t")
        print('\n')    
        for time_slot in TIME_SLOTS:
            print(time_slot, end="\t")
            for day in DAYS_OF_WEEK:
                for each_class in self._classes_list:
                    if each_class._time.get_time() == time_slot: 
                        if each_class._time.get_day() == day:
                            print(f'{each_class._course.get_name()}({each_class._room.get_id()})', end="\t")
            print('\n','-'*100)
        print(f'Conflicts: {self.get_conflicts()}')
        print(f'Fitness:   {self.get_fitness()}')
        
    def print_classes_list(self):
        for each_class in self.get_classes_list():
            print(each_class)
        print (len(self.get_classes_list()))

#------------------------------------------------------------------------------
# Sample Data
#------------------------------------------------------------------------------


DEPT1_COURSES = [
    Course(0, "ADCA1", 30, 'T0', 4),
    Course(1, "COEA1", 25, 'T1', 2),
    Course(2, "HCTA1", 30, 'T2', 2),
    Course(3, "INGA1", 45, 'T3', 4),
    Course(4, "LOPA1", 15, 'T4', 6),
    Course(5, "MD1A1", 15, 'T5', 2),
]

DEPT2_COURSES = [
    Course(6,  "ADMA2", 25, 'T6', 2),
    Course(7,  "AS1A2", 35, 'T7', 4),
    Course(8,  "LOGA2", 30, 'T8', 4),
    Course(9,  "MD1A2", 30, 'T9', 2),
    Course(10, "RC1A2", 20, 'T10', 4),
    Course(11, "SOPA2", 20, 'T11', 4),
]

DEPT3_COURSES = [
    Course(12,  'AS2A3', 25, 'T12', 4),
    Course(13,  "BD1A3", 35, 'T13', 4),
    Course(14,  "EDDA3", 30, 'T14', 4),
    Course(15,  "OSMA2", 35, 'T15', 2),
    Course(16,  "PEEA3", 20, 'T16', 2),
    Course(17,  "RC2A3", 20, 'T17', 4),
]

DEPT4_COURSES = [
    Course(18,  "BD2A4", 25, 'T18', 4),
    Course(19,  "GSIA4", 35, 'T19', 2),
    Course(20,  "IDSA4", 30, 'T20', 4),
    Course(21,  "LP2A4", 45, 'T21', 4),
    Course(22,  "MTPA4", 20, 'T22', 2),
    Course(23,  "PRSA4", 20, 'T23', 4),
]

DEPT5_COURSES = [
    Course(24, "SIGA5", 30, 'T24', 4),
    Course(25, "GTIA5", 25, 'T25', 4),
    Course(26, "DW1A5", 30, 'T26', 4),
    Course(27, "ENGA5", 45, 'T27', 4),
    Course(28, "PR1A5", 15, 'T28', 4),
]

DEPT6_COURSES = [
    Course(29, "PI2A6", 30, 'T29', 8),
    Course(30, "TPAA6", 25, 'T30', 4),
    Course(31, "DW2A6", 30, 'T31', 4),
    Course(32, "SEGA6", 45, 'T32', 4),
]

DEPARTMENTS = [
    Department(1,'DEPT1', DEPT1_COURSES),
    Department(2,'DEPT2', DEPT2_COURSES),
    Department(3,'DEPT3', DEPT3_COURSES),
    Department(4,'DEPT4', DEPT4_COURSES),
    Department(5,'DEPT5', DEPT5_COURSES),
    Department(6,'DEPT6', DEPT6_COURSES),
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

class Population:
    def __init__(self, schedules_list = []):
        self._schedules_list = schedules_list
        
    def get_schedules_list(self):               return self._schedules_list
    def get_schedule(self, position):           return self._schedules_list[position]
    def get_size(self):                         return len(self.get_schedules_list)
    def get_total_classes_num(self):
        counter = 0          
        for each in self.get_schedules_list():
            counter += each.get_classes_num()
        return counter

    def add_schedule(self, schedule):   self._schedules_list.append(schedule)

    def print_population(self):
        for i,schedule in enumerate(self.get_schedules_list()):
            print(f'\n---- #{i+1} -----',end = "")
            schedule.print_grid()
        print (self.get_total_classes_num())

    def print_classes_list(self):
        for schedule in self.get_schedules_list():
            schedule.print_classes_list()

class GeneticAlgorithm:
    def __init__(self, population):
        self._population = [i for i in population.get_schedules_list()]
        print(self._population)
        
    def get_population(self): return self._population
        
    def mutate_schedule(self, position = 0):
        new_schedule = self._population[position]
        for i in range(new_schedule.get_classes_num()):
            if i % 2 == 0 :
                new_schedule.overwrite_class(i,self._population[position].get_classes_list()[i])

    def __str__(self):
        return self.get_population()
    
    
    

#------------------------------------------------------------------------------
# Methods
#------------------------------------------------------------------------------
def create_times(DAYS_OF_WEEK = DAYS_OF_WEEK, TIME_SLOTS = TIME_SLOTS):
    counter = 0
    holder = []
    for i in DAYS_OF_WEEK:
        for j in TIME_SLOTS:
            holder.append(Time(counter,i,j))
            counter +=1 
    return holder

def check_compatible_rooms(qty_students):   # Returns a list with all rooms that fit that course students'
    holder = []
    for room in ROOMS:
        if room.get_capacity() >= qty_students:
            holder.append(room)
    return holder

def create_population(size):
    my_population = Population()
    for i in range(size):
        holder_schedule = Schedule(i,DEPARTMENTS[i])
        holder_schedule.initialize()
        my_population.add_schedule(holder_schedule)
    while True:
        if my_population.get_total_classes_num() != 120:
            if len(my_population.get_schedules_list()) != 6:
                print('passing')
                return create_population(size)
        break
    return my_population


#------------------------------------------------------------------------------
# Runner Code
#------------------------------------------------------------------------------
if __name__ == "__main__":
    my_population = Population()
    while True:
        if my_population.get_total_classes_num() != 120:
            my_population = create_population(size = 6)
        else:
            break

    my_population.print_population()
    my_population.get_total_classes_num()
    my_population.get_schedule(1)
    genetic_crossover = GeneticAlgorithm(my_population)
    genetic_crossover.mutate_schedule()