from random import shuffle
from sampledata import DAYS_OF_WEEK as DOW
from sampledata import TIME_SLOTS as TL
from sampledata import ROOMS
from sampledata import COURSES as CRS


def print_anyList(anyList):
    for _ in anyList: print(_)
    
def rand_anyList(aList):
    randList = aList
    shuffle(randList)
    return randList

# Times Structure
# times = list
#   time[0] = id
#   time[1] = day
#   time[2] = time
#   time[3] = is_Occupied
# time = ['0','seg','0',True]
# times.append(timea)
# print(times[0][0]) --> 0 (id from times[0])
def create_times(days_of_week, time_slots):
    timeList = []
    counter =  0
    for day in days_of_week:
        for time in time_slots:
            new_time = [counter,day,time,False]
            timeList.append(new_time)
            counter += 1
    return timeList
def assign_time(counter,day,time):
    new_time = [counter,day,time,True]
    return new_time
def set_time_occupied(timeList,id):
    timeList[id][3] = True 

print('*'*20)
print("PRINTING TIMES")
times = create_times(DOW,TL)
times[0] = assign_time(0,'seg',0)
set_time_occupied(times,5)
print_anyList(times)
print('*'*20)

# Rooms Structure
# room[0]=id
# room[1]=capacity
# room[2]=[occupied_times]
def create_rooms(roomList):
    rooms = []
    for room in roomList:
        #new_room = [id,capacity,[occupied_times]]
        new_room = [room[0],room[1],[]]
        rooms.append(new_room)
    return rooms

def add_room_occ_time(room,time):
    room[2].append(time)
    
def get_occ_times(room):
    if room[2] is not None:
        return(room[2])
    else:
        return []

print("PRINTING ROOMS")
rooms = create_rooms(ROOMS)
print_anyList(rooms)
print('Occupied times for room 3', get_occ_times(rooms[2]))
print('*'*20)



# Course Structure
# course[0]=id
# course[1]=capacity
# course[2]=[occupied_times]
def create_courses(courseList, roomList):
    courses = []
    counter = 0
    compatible_rooms = []
    for course in courseList:
        compatible_rooms = []
        for room in roomList:
            #new_course = [id,name,qty_students,times_per_week,[compatible_rooms]]
            if course[1] <= room[1]:            # if qty students <= room slots
                compatible_rooms.append(room)
        new_course = [counter, course[0],course[1],course[2],compatible_rooms]
        courses.append(new_course)
        counter += 1
    return courses

def get_times_per_week(courseList,id):
    return courseList[id][3]

def get_compatible_rooms(course):
    return course[4]



print("PRINTING COURSES")
courses = create_courses(CRS,rooms)
print_anyList(courses)
print(get_compatible_rooms(courses[1]))
print(get_times_per_week(courses,0))
print('*'*20)


# Department Structure
def create_depts(deptList, roomList):
    depts = []
    counter = 0
    compatible_rooms = []
    for dept in deptList:
        compatible_rooms = []
        for room in roomList:
            #new_dept = [id,name,qty_students,times_per_week,[compatible_rooms]]
            if dept[1] <= room[1]:            # if qty students <= room slots
                compatible_rooms.append(room[0])
        new_dept = [counter, dept[0],dept[1],dept[2],compatible_rooms]
        depts.append(new_dept)
        counter += 1
    return depts

    return deptList[id][4]


# Class Structure
def create_class(counter, course, time, room):
    #new_class = [id,course,time,room]
    new_class = [counter, course, time, room]
    return new_class

print("PRINTING CLASSES TEST")

classes = []
for i in range(20):
    classes.append(create_class(i,i,i,i)) 
print_anyList(classes)
print('*'*20)

# Schedule Structure
def create_schedule(courseList,timeList):
    courses = courseList
    times = timeList
    schedule = []
    counter = 0
    for course in courses:
        counter = 0
        compatible_rooms = get_compatible_rooms(course)
        for room in compatible_rooms:
            for time in times:
                if time[3] != False: # if time is available
                    if str(time[0]) not in str(get_occ_times(room)):
                        set_time_occupied(times,time[0])
                        add_room_occ_time(room,[time])
                        new_class = [counter,course,time,room]
                        schedule.append(new_class)
                        counter += 1
                        print('counter',counter)
                if counter == course[3]:    
                    break
    return schedule

def print_schedule(schedule):
    for each in schedule:
        print('course-id', each[1][0])
        print('course-name',each[1][1])
        print('course-qty',each[1][2])
        print('course-tpw',each[1][3])
        #print('course-rooms',each[1][4])
        print('time-id',each[2][0])
        print('time-day',each[2][1])
        print('time-time',each[2][2])
        print('time-flag',each[2][3])
        print('room-id',each[3][0])
        print('room-capacity',each[3][1])
        print('room-occupied',each[3][2])
        print()

mysch = create_schedule(courses,times)
print_schedule(mysch)