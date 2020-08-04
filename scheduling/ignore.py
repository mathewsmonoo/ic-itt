from sampledata import TEACHER_LIST, ROOM_LIST, COURSE_LIST, TIMES, WEEK


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

class Time:
    def __init__(self, id, time):
        self._id        = id
        self._time      = time
        self._isAvailable = True
        
    def get_time(self):  return self._time
    def get_class(self): return self._class
    
    def __str__(self):   return self._time
    
TIMES = [
   #[id,   start - finish]
    Time("1", "07:30 - 08:20"), # First Class
    Time("2", "08:20 - 09:10"),
    # 20min break
    Time("3", "09:30 - 10:20"), 
    Time("4", "10:20 - 11:10"),
     # 10min break
    Time("5", "11:20 - 12:10"), 
    Time("6", "12:10 - 13:00"), # Last Class
]

class Day: # Day Object
    def __init__(self, id, name, times = []):
        self._id     = id
        self._name   = name
        self._times  = []
        
        if len(self._times) <= 0:
            for i in range(0,len(TIMES)):
                self._times.append(TIMES[i])
            
    def get_day(self):
        return self._times
    
    def get_times(self): # Loop for getting values inside _times LIST
        holder = ''
        for time in self._times:
            holder += str(time) + "\n"
        return holder

    def __str__(self): 
        return f'ID: {self._id}\tNAME: {self._name}\n{self.get_times()}'

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


"""
    > Functions
"""

def create_week(): #Creates Week
    myWeek = []
    for i,j in enumerate(WEEK.keys()):
        d = Day(i,j)
        myWeek.append(d)
    return myWeek

def doit(): # Runner
    week    = create_week()
    myWeek  = allocate_rooms(week)
    for day in week:    print(day)
    #for day in myWeek:  print(day)

def allocate_rooms(myWeek):
    holderWeek = []
    
    # compare Courses with most students with rooms with less capacity
    sorted_courses  = sorted(COURSES,   key = lambda x: x._slots, reverse = True) 
    sorted_rooms    = sorted(ROOM_LIST, key = lambda y: y[1],     reverse = True)
    
    counter = -1
    for room in sorted_rooms:
        for course in sorted_courses:
            counter += 1
            if course.get_slots() <= room[1]:
                print(f'CourseID {course.get_id()} - {course.get_slots()} Students :: Goes to {room[0]} with {room[1]} capacity.')
                
                #myDay = Day(counter, 'FIX_DAY_NAME', TIMES[counter])
                
                #holderWeek.append(myDay)

                #TODO - Here we associate the course(class) with the room
                
                # Here we remove the room, so it doesn't get associated with another course.
    return holderWeek


# Additional Data

COURSES = [
    #       id,   teacher,     slots, times per week
    Course("C1", TEACHER_LIST[0], 20, 4),
    Course("C2", TEACHER_LIST[1], 25, 2),
    Course("C3", TEACHER_LIST[2], 45, 6),
    Course("C4", TEACHER_LIST[3], 30, 3),
    Course("C5", TEACHER_LIST[4], 35, 4),
    Course("C6", TEACHER_LIST[0], 25, 2),
]
