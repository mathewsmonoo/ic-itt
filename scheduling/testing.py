#--------------------------------------------------------------------------------
# Classes
#--------------------------------------------------------------------------------
class Room:
    def __init__(self, id, capacity):
        self._id        = id
        self._capacity  = capacity
    
    def get_id(self):       return self._id
    def get_capacity(self): return self._capacity

class Course:
    def __init__(self, id, slots, timesPerWeek):
       self._id             = id
       self._slots          = slots
       self._timesPerWeek   = timesPerWeek

    def get_id(self):           return self._id
    def get_slots(self):        return self._slots
    def get_timesPerWeek(self): return self._timesPerWeek

class Time:
    def __init__(self, id, time):
        self._id         = id
        self._time       = time
        self._isOccupied = False
        
    def get_time(self):         return self._time
    def get_class(self):        return self._class
    def get_isOccupied(self):   return self._isOccupied
            
    #The following method is just for printing, not returning useful data
    def get_isOccupiedStr(self):
        if self._isOccupied:
            return f"Occupied"
        else:
            return f"Available"
    
    def change_isOccupied(self):  self._isOccupied = not(self._isOccupied)
    def __str__(self):   return f'{self.get_time()} - {self.get_isOccupiedStr()}'
    
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
    def __init__(self, id, name, times = [], classes = []):
        self._id     = id
        self._name   = name
        self._times  = times
        self._classes = classes
        
        if len(self._times) == 0:
            for i in range(0,len(TIMES)):
                self._times.append(TIMES[i])

    def get_day(self):
        holder = ''
        for time in self._times:
            holder += str(time.get_time()) + str(time.) 
        return holder
    
    def get_times(self):
        return self._times
    
    def get_classes(self): return self._classes
    
    def set_classes(self, classList):
        for each in classList:
            self._classes.append(each)
            
    def __str__(self): 
        return f'ID: {self._id}\tNAME: {self._name}\n{self.get_times()}\n{self.get_classes()}'

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


#--------------------------------------------------------------------------------
# Functions
#--------------------------------------------------------------------------------

def create_week(): #Creates Week
    myWeek = []
    for i,j in enumerate(WEEK.keys()):
        d = Day(i,j)
        myWeek.append(d)
    return myWeek


def generateClasses():
    classList = []            # To be returned in the end of the function
    counter = 0               # counter for generating Class Id 
    rejectedCounter = 0       # counter of rejected iterations
    myDay = Day(1,'XXX')      
    times = myDay.get_times() # list with all times in that day

    # Here we sort ROOMS and COURSES by most capacity and slots, respectively.
    sorted_rooms    = sorted(ROOMS,   key = lambda y: y[1],     reverse = True)
    sorted_courses  = sorted(COURSES, key = lambda x: x._slots, reverse = True) 

    occupied_rooms = {}       # Dictonary created to control which rooms are occupied
    for time in times:
        for course in sorted_courses:
            if (time.get_isOccupied() == False):       # If time is not occupied
                for room in sorted_rooms:
                  if room[0] not in occupied_rooms:    # If the room is not occupied 
                    course_slots  = course.get_slots() 
                    room_capacity = room[1]        # room is a list and [1] is the capacity
                    if (room_capacity >= course_slots):
                        counter += 1 
                        newClass = Class(counter, course, time, room)
                        classList.append(newClass)
                        occupied_rooms[room[0]] = room[1]
                        time.change_isOccupied()
                        break
            else:                                       # If time is occupied
                rejectedCounter += 1
    myDay.set_classes(classList)
    return myDay,rejectedCounter

def doit(): # Runner
    myDay,b = generateClasses()
    print(f'{len(myDay)} Time Slots per day')
    print(f'\t\tClasses:')
    for each in myDay:
        print(each.get_time(),' ',each.get_room())
    print(f'Rejected iterations: {b}')
    print(myDay)


def allocate_rooms(myWeek):
    holderWeek = []
    
    # compare Courses with most students with rooms with less capacity
    sorted_courses  = sorted(COURSES,   key = lambda x: x._slots, reverse = True) 
    sorted_rooms    = sorted(ROOMS, key = lambda y: y[1],     reverse = True)
    
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

#--------------------------------------------------------------------------------
# Sample Data
#--------------------------------------------------------------------------------

COURSES = [
    #     (id, slots, times per week),
    Course("C1", 20, 4),
    Course("C2", 25, 2),
    Course("C3", 45, 6),
    Course("C4", 30, 3),
    Course("C5", 35, 4),
    Course("C6", 25, 2),
]

ROOMS = [
    ["R1", 25],
    ["R2", 30],
    ["R3", 45],
    ["R4", 40],
    ["R5", 35],
    ["R6", 45],
]

WEEK = {
   #'DAY':ListOFClasses,
    'MON':None,
    'TUE':None,
    'WED':None,
    'THU':None,
    'FRI':None,
}

if __name__=="__main__":
  doit()
