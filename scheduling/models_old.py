class Course:
    def __init__(self, id, teacher, slots, timesPerWeek):
       self._id             = id
       self._teacher        = teacher
       self._slots          = slots
       self._timesPerWeek   = timesPerWeek

    def get_id(self):       return self._id
    def get_teacher(self):  return self._teacher
    def get_slots(self):    return self._slots
    def get_timesPerWeek(self):  return self._timesPerWeek

WEEK = {
   #'DAY':ListOFClasses,
    'MON':None,
    'TUE':None,
    'WED':None,
    'THU':None,
    'FRI':None,
}

TIMES = [
    #[id, start - finish , class.default = None]
    ["1", "07:30 - 08:20", None], # First Class
    ["2", "08:20 - 09:10", None],
    # 20min break
    ["3", "09:30 - 10:20", None], 
    ["4", "10:20 - 11:10", None],
     # 10min break
    ["5", "11:20 - 12:10", None], 
    ["6", "12:10 - 13:00", None], # Last Class
]
ROOMS = [
        ["R1", 25],
        ["R2", 30],
        ["R3", 45],
        ["R4", 40],
        ["R5", 35],
        ["R6", 45],
]
TEACHERS = [
    ["001", "Alberto"],
    ["002", "Bruna"],
    ["003", "Caio"],
    ["004", "Duda"],
    ["005", "Eder"]
]

COURSES = [
    Course("C1", TEACHERS[0], 20, 4),
    Course("C2", TEACHERS[1], 25, 2),
    Course("C3", TEACHERS[2], 45, 6),
    Course("C4", TEACHERS[3], 30, 3),
    Course("C5", TEACHERS[4], 35, 4),
    Course("C6", TEACHERS[0], 25, 2),
]

# This is sample data for testing
class Data:
    def __init__(self):
        self._rooms     = []
        self._times     = []
        self._courses   = []
        self._teachers  = []
        # Rooms Loop
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0],self.ROOMS[i][1]))
            
        # Times Loop
        for i in range(0, len(self.TIMES)):
            self._times.append(Time(self.TIMES[i][0],self.TIMES[i][1]))
                    
        #Courses Loop
        for i in range(0, len(self.COURSES)):
            self._courses.append(self.COURSES[i])
            
        # Teachers Loop
        for i in range(0, len(self.TEACHERS)):
            self._teachers.append(Teacher(self.TEACHERS[i][0],self.TEACHERS[i][1]))

    def get_all_rooms(self):
        holder = ""
        for i in self._rooms:
            holder +=  str(i._id) + " " + str(i._capacity)   
        return holder
    
    def get_rooms(self):     return self._rooms
    def get_times(self):     return self._times
    def get_courses(self):   return self._courses
    def get_teachers(self):  return self._teachers
    
    def __str__(self):
        return  f"{self.get_rooms()},\t{self.get_times()}\n"  \
                f"{self.get_courses()},\t{self.get_teachers()}" 

# This class creates ONE day with 6 "times" and 1 slot for the CLASS
class Day:
    def __init__(self, dayName):
        self._times = []
        for i in range(0, len(TIMES)):
            self._times.append(Time(TIMES[i][0],TIMES[i][1],TIMES[i][2]))

        self._dayName = dayName    
        
        
    def get_times(self): return self._times
    
    def __str__(self):
        return str(self.get_times())


class Teacher:
    def __init__(self, id, name):
        self._id   = id
        self._name = name
        
    def get_id(self):   return self._id
    def get_name(self): return self._name


class Room:
    def __init__(self, id, capacity):
        self._id        = id
        self._capacity  = capacity
    
    def get_id(self):       return self._id
    def get_capacity(self): return self._capacity
    
class Time:
    def __init__(self, id, time, myClass):
        self._id    = id
        self._time  = time
        self._class = myClass

    def get_id(self):       return self._id
    def get_time(self):     return self._time
    def get_class(self):    return self._class


class Class:
    def __init__(self, id, course, time, room):
       self._id         = id
       self._course     = course
       self._time       = time
       self._room       = room
    
    def get_id(self):       return self._id
    def get_course(self):   return self._course
    def get_time(self):     return self._time
    def get_room(self):     return self._room
    
    def set_time(self, time):       self._time    = time
    def set_room(self, room):       self._room    = room

def designate_times():
    """"""

# \/ this must be done after associating the class time    
def count_capacity(): 
    # compare Courses with most students with rooms with less capacity
    sorted_courses  = sorted(COURSES, key=lambda x: x._slots, reverse = True) 
    sorted_rooms    = sorted(ROOMS,   key=lambda y: y[1],     reverse = True)
    counter = 0
    for i in sorted_courses:
        counter -= 1
        for j in sorted_rooms:
            if j[1] >= i._slots:
                print(f'Course {i._id}  - Slots(students) {i._slots} :: Goes in {j[0]} with {j[1]} capacity')
                
                #TODO - Here we associate the course(class) with the room
                
                sorted_rooms.remove(j) # Here we remove the room, so it doesn't get associated with another course.
                counter += 1 #
    print(f'Courses without rooms { -1 * counter}')

def check_occupied(someDay):
    
    
    pass

def create_week():
    myWeek = {}
    for i in WEEK.keys():
        d = Day(i)
        myWeek[d._dayName] = d._times
    return myWeek

def print_week(myWeek):
    _myWeek = myWeek
    for key in _myWeek.keys():
        if (_myWeek.get(key) is None):
            print(f'{day} is empty')
        else:
            holder = _myWeek.get(key)
            for each in holder:
                print(each)
