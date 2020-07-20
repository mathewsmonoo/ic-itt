import pandas as pd
import numpy as np

# Change this variable to change which file to load
file_path = './data/comp01.ctt'

def import_dataset(path_to_dataset = file_path ):
    loaded          = pd.read_csv(path_to_dataset)
    loaded_values   = loaded.values

    #This code separates properties and their values and appends them to a list.
    property_list = []
    for i in loaded_values[:6]:
        foo = str(i)
        foo = foo.strip("[]\'")
        bar = foo.split(': ')
        bar[1] = int(bar[1])
        property_list.append(bar)
    # Now we have a property list.

    # Now we delete the items from nparray
    loaded_values = np.delete(loaded_values,[0,1,2,3,4,5,6])
    
    #These are the vars that hold count of items:
    courses_count       = property_list[0][1]
    rooms_count         = property_list[1][1]
    days_count          = property_list[2][1]
    periods_count       = property_list[3][1]
    curricula_count     = property_list[4][1]
    constraint_count    = property_list[5][1]

    #This code separates the courses and their values and appends them to a list.
    course_list = []
    for i in (loaded_values[:courses_count]):
        foo = str(i)
        bar = foo.strip("[]\'")
        bar = bar.split(" ")
        course_list.append(bar)
    # Now we have a course list.
    
    # Now we delete the items from nparray
    for i in range(courses_count +1):
        loaded_values = np.delete(loaded_values,[0])
    
    #This code separates the rooms and their values and appends them to a list.
    rooms_list  = []
    for i in (loaded_values[:rooms_count]):
        foo = str(i)
        foo = foo.split("\t")
        foo[1] = int(foo[1])
        rooms_list.append(foo)
    # Now we have a room list.
    
    # Now we delete the items from nparray
    for i in range(rooms_count + 1):
        loaded_values = np.delete(loaded_values,[0])

    #This code separates the curricula and their values and appends them to a list.
    curricula_list  = []
    for i in (loaded_values[:curricula_count]):
        foo = str(i)
        bar = foo.split()
        curricula_list.append(bar)
    # Now we have a room list.
    
    # Now we delete the items from nparray
    for i in range(curricula_count + 1):
        loaded_values = np.delete(loaded_values,[0])

    #This code separates the constraints and their values and appends them to a list.
    constraint_list     = []
    for i in (loaded_values[:constraint_count]):
        foo = str(i)
        bar = foo.split()
        constraint_list.append(bar)
    # Now we have a constraint list.
    return CompModel(courses_count,course_list,rooms_count,rooms_list,days_count,periods_count,curricula_count,curricula_list,constraint_count,constraint_list)

#This is the class that will hold our values
class CompModel(object):
    def __init__(self,courses,courses_list,rooms,rooms_list,days,periods,curricula,curricula_list,constraints,constraints_list):
        self.courses        = courses
        self.COURSES_LIST   = courses_list
        self.rooms          = rooms
        self.ROOMS_LIST     = rooms_list
        self.days           = days
        self.periods        = periods
        self.curricula      = curricula
        self.CURRICULA_LIST = curricula_list
        self.constraints    = constraints
        self.CONSTRAINT_LIST= constraints_list

    # The following methods returns tuples of a certain count and list, whenever possible.
    # If not possible, returns only one value.
    def get_courses(self):
        return self.courses, self.COURSES_LIST
    def get_rooms(self):
        return self.rooms, self.ROOMS_LIST
    def get_days(self):
        return self.days
    def get_periods(self):
        return self.periods    
    def get_curricula(self):
        return self.curricula, self.CURRICULA_LIST
    def get_constraints(self):
        return self.constraints, self.CONSTRAINT_LIST

    # The following methods are used ONLY FOR printing.
    def print_courses(self):
        print(self.courses,' Courses:')
        for i in self.COURSES_LIST:
            print(i)
    def print_rooms(self):
        print(self.rooms,' Rooms:')
        for i in self.ROOMS_LIST:
            print(i)
    def print_days(self):
        print(self.days,' Days')
    def print_periods(self):
        print(self.periods,' Periods per day')
    def print_curricula(self):
        print(self.curricula,' Curricula:')
        for i in self.CURRICULA_LIST:
            print(i)
    def print_constraints(self):
        print(self.constraints,' Constraints')
        for i in self.CONSTRAINT_LIST:
            print(i)

    def details(self):
        self.print_courses()
        self.print_rooms()
        self.print_days()
        self.print_periods()
        self.print_curricula()
        self.print_constraints()
        
    def less_details(self):
       print('Courses:',    self.courses)
       print('Rooms: ',     self.rooms)
       print('Days: ',      self.days)
       print('Periods: ',   self.periods)
       print('Curricula: ', self.curricula)
       print('Constraints: ',self.constraints)
       
    # There is no __str__() method yet.