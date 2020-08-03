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

MORNING_CLASSES = [
    [1,"07:30"], #"08:20"], # First Class
    [2,"08:20"], #"09:10"],
        # 20min #break 
    [3,"09:30"], #"10:20"], 
    [4,"10:20"], #"11:10"],
        # 10min #break 
    [5,"11:20"], #"12:10"], 
    [6,"12:10"], #"13:00"], # Last Class
]
ROOMS = [
        ["R1", 25],
        ["R2", 30],
        ["R3", 45],
        ["R4", 40],
        ["R5", 35],
]
TEACHERS = [
    ["001", "Alberto"],
    ["002", "Bruna"],
    ["003", "Caio"],
    ["004", "Duda"],
    ["005", "Eder"]
]
TIMES = [
    ["TIME1", "07:00 - 07:50"],
    ["TIME2", "07:50 - 08:40"],
    ["TIME3", "08:40 - 09:30"],
    ["TIME4", "10:20 - 11:10"],
    ["TIME5", "11:30 - 12:20"],
]
COURSES = [
    Course("C1", TEACHERS[0], 20, 4),
    Course("C2", TEACHERS[1], 25, 2),
    Course("C3", TEACHERS[2], 45, 6),
    Course("C4", TEACHERS[3], 30, 3),
    Course("C5", TEACHERS[4], 35, 4),
    Course("C6", TEACHERS[0], 25, 2),
    Course("C7", TEACHERS[1], 45, 4),
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
            holder +=  str(i._id) + " " + str(i._capacity) + "\n"     
        return holder
    
    def get_rooms(self):     return self._rooms
    def get_times(self):     return self._times
    def get_courses(self):   return self._courses
    def get_teachers(self):  return self._teachers
    
    def __str__(self):
        return  f"{self.get_rooms()},\t{self.get_times()}\n"  \
                f"{self.get_courses()},\t{self.get_teachers()}\n" 

class Schedule:    
    def __init__(self,id ,MORNING_CLASSES):
        self._id = id
        self._morning_classes = MORNING_CLASSES
    
    
    
    
    def __str__(self):
        """"""    



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
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self):       return self._id
    def get_time(self):     return self._time

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
    
    
def designate_rooms(COURSES = COURSES, ROOMS = ROOMS): 
    # compare Courses with most students with rooms with less capacity
    sorted_courses  = sorted(COURSES, key=lambda x: x._slots, reverse = True) 
    sorted_rooms    = sorted(ROOMS,   key=lambda y: y[1],     reverse = True)

    for i in sorted_courses:
        for j in sorted_rooms:
            if i._slots <= j[1]:
                print(f'Course {i._id}  - Slots(students) {i._slots} :: Goes in {j[0]} with {j[1]} capacity')
                #TODO - Here we associate the course(class) with the room    
    
    


    