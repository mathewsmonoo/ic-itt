import sampledata as mydata

from classes import Time, Room, Department, Course, Individual, Schedule

days_of_week = mydata.DAYS_OF_WEEK
time_slots   = mydata.TIME_SLOTS 
room_list    = mydata.ROOMS
dept_list    = mydata.DEPARTMENTS

def generate_times(daysOfWeek, timeSlots):   # This method returns a list of Times for a week.
    counter = 0                              # Confirmed to be working.
    myList = []
    for i in daysOfWeek:
        for j in timeSlots:
            holder = Time(counter,i,j)
            myList.append(holder)
            counter +=1
    for _ in myList:
        print(_)
    return myList

def generate_rooms(roomList):
    myList = []
    for each in roomList:
        myList.append(Room(each[0],each[1]))
    for _ in myList:
        print(_)
    return myList

def generate_depts(deptList):
    counter = 0
    myList = []
    for each in deptList:
        dept_courses = generate_courses(each[0])
        myList.append(Department(counter,dept_courses))
        counter += 1
    for _ in myList:
        print(_)
    return myList

def generate_courses(courseList):
    myList  = []
    counter = 0
    for each in courseList:
        myList.append(Course(counter,each[0],each[1],each[2]))
        counter += 1
    for _ in myList:
        print(_)
    return myList

def create_individual(size):
    dados = Dados()
    counter = 0
    my_individual = Individual()
    while counter < 120 :
        for i in range(size):
            holder_schedule = Schedule(dados,i)
            holder_schedule.initialize()
            print('\n\n',holder_schedule.get_classes_num(),'\n\n')
            if holder_schedule.get_classes_num() == 20:
                my_individual.add_schedule(holder_schedule)
                counter += holder_schedule.get_classes_num()
    return my_individual
        
    """
def create_individual(dados, size):
    while True:
        my_individual = Individual()
        for i in range(size):
            holder_schedule = Schedule(dados,i)
            holder_schedule.initialize()
            if holder_schedule.get_classes_num() != 20:
                continue
            else:
                my_individual.add_schedule(holder_schedule)
        print('\n\n\n', my_individual.get_total_classes_num(),'\n\n')
        if my_individual.get_total_classes_num() == 120:
            return my_individual
    """        

class Dados:
    def __init__(self):
        self._times = generate_times(days_of_week, time_slots)
        self._depts = generate_depts(dept_list)
        self._rooms = generate_rooms(room_list)
        self._time_slots = time_slots
        self._days_of_week = days_of_week

    def get_times(self): return self._times
    def get_depts(self): return self._depts
    def get_rooms(self): return self._rooms
    def get_dept_courses(self, deptnum):
        return self._depts[deptnum].get_courses_list()

    def print_rooms(self):
        for i in self._rooms:
            print(i)
    def print_depts(self):    
        for i in self._depts:
            print(i)
    def print_times(self):    
        for i in self._times:
            print(i)
            
    def print_all(self):
        self.print_rooms()
        self.print_depts()
        self.print_times()

    def __str__(self):
        return f'{self.get_depts()}'
