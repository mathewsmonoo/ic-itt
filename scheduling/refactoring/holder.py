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

def assign_timeA(timeList,counter,day,time):
    new_time = [counter,day,time,True]
    timeList[counter] = new_time
    return new_time

def assign_time(timeList,time_counter,roomList,room_counter):
    timeList[time_counter][3] = True
    roomList[room_counter][2].append(timeList[time_counter][0])


def set_time_occupied(timeList,id):
    timeList[id][3] = True

print('*'*20)
print("PRINTING TIMES")
times = create_times(DOW,TL)
print_anyList(times)
print('*'*20)

# Rooms Structure
    #new_room = [id,capacity,[occupied_times]]
def create_rooms(roomList):
    rooms = []
    for room in roomList:
        new_room = [room[0],room[1],[]]
        rooms.append(new_room)
        print('ROOM0 ',new_room[0])
        print('ROOM1 ',new_room[1])
        print('ROOM1 ',new_room[2])
    return rooms

def add_room_occ_time(room,time):
    room[2].append(time)

def get_occ_times(room):
    try:
        holder = room[2]
        if holder != None:
            return(room[2])
    except:
        return

print("PRINTING ROOMS")
rooms = create_rooms(ROOMS)
for room in rooms:
    print(room)
#print_anyList(rooms)
print('*'*20)



# Course Structure
#  course = [id,name,qty_students,times_per_week,[compatible_rooms]]

def create_courses(courseList, roomList):
    courses = []
    counter = 0
    for course in courseList:
        compatible_rooms = []
        compatible_rooms = set_compatible_rooms(course,roomList)
        new_course = [counter, course[0],course[1],course[2],compatible_rooms]
        courses.append(new_course)
        counter += 1
    return courses

def get_times_per_week(courseList,id):
    return courseList[id][3]

def set_compatible_rooms(course,roomList):
    compatible_rooms = []
    for room in roomList:
        if course[1] <= room[1]:
            compatible_rooms.append(room[0])
    return compatible_rooms
        

def get_compatible_rooms(course):
    return course[4]


print("PRINTING COURSES")
courses = create_courses(CRS,rooms)
print_anyList(courses)
print(get_compatible_rooms(courses[1]))
print(get_times_per_week(courses,0))
print('*'*20)


# Class Structure
#  new_class = [id,course,time,room]
def create_class(counter, course, time, room):
    new_class = [counter, course, time, room]
    return new_class


# Schedule Structure
def create_schedule(courseList,timeList,roomList):
    rooms    = roomList
    courses  = courseList
    times    = timeList
    schedule = []
    id_counter = 0
    for course in courses:
        compatible_rooms = get_compatible_rooms(course)
        control_counter  = 0
        for room in compatible_rooms:
            #print('room:: ',room, ' ', type(room))
            #print('ROOMS', rooms)
            print('control_counter [',control_counter,']',end='\t')
            print('id_counter [',id_counter,']')
            #print('ROOM:: ', room, ' ', type(room) ,' !!')
            for time in times:
                #print('time :: ', time) gigantic print
                time_id = time[0]
                time_bool = time[3]
                # print('time_bool: ', time_bool,' ', type(time_bool))
                occ_times = get_occ_times(rooms[room])
                # print(occ_times) #gigantic print
                if not time_bool: # if time is available
                    if time_id not in occ_times:
                        # control_counter doesnt reach here
                        print('\n\n')
                        print('timeList1: ',times)
                        assign_time(times, control_counter, rooms, room) # list, control_counter,      id,    time
                        print("Test ", times[control_counter])
                        print("Test2", times[control_counter][3])
                        print('\n\n')
                        print('timeList2: ',times)
                        print('room',room)
                        rooms[3].append(time[0])                        # test this
                        print('roomList: ',rooms)
                        new_class = create_class(id_counter,course,time,rooms[room])
                        schedule.append(new_class)
                        id_counter += 1
                        control_counter += 1
                        print('id_counter',id_counter)
                        print('counter',id_counter)
                if control_counter == course[3]:
                    break
    return schedule

def print_schedule(schedule):
    for each in schedule:
        print('course-id',  each[1][0])
        print('course-name',each[1][1])
        print('course-qty', each[1][2])
        print('course-tpw', each[1][3])
        #print('course-rooms',each[1][4])
        print('time-id',  each[2][0])
        print('time-day', each[2][1])
        print('time-time',each[2][2])
        print('time-flag',each[2][3])
        print('room-id',  each[3][0])
        print('room-capacity',each[3][1])
        print('room-occupied',each[3][2])
        print()

if (__name__ == '__main__'):
    print('_________Running Script!_________')
    mysch = create_schedule(courses,times,rooms)
    print('*'*20,'\nschedule\n')
    for i in mysch:
        print('i0', i[0], 'i1', i[1], 'i2', i[2], 'i3', i[3])
    #print_schedule(mysch)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    -----------------------------
    
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

def assign_timeA(timeList,counter,day,time):
    new_time = [counter,day,time,True]
    timeList[counter] = new_time
    return new_time

def assign_time(timeList,time_counter,roomList,room_counter):
    timeList[time_counter][3] = True
    roomList[room_counter][2].append(timeList[time_counter][0])


def set_time_occupied(timeList,id):
    timeList[id][3] = True

print('*'*20)
print("PRINTING TIMES")
times = create_times(DOW,TL)
print_anyList(times)
print('*'*20)

# Rooms Structure
    #new_room = [id,capacity,[occupied_times]]
def create_rooms(roomList):
    rooms = []
    for room in roomList:
        new_room = [room[0],room[1],[]]
        rooms.append(new_room)
    return rooms

def add_room_occ_time(room,time):
    room[2].append(time)

def get_occ_times(room):
    try:
        holder = room[2]
        if holder != None:
            return(room[2])
    except:
        return []

print("PRINTING ROOMS")
rooms = create_rooms(ROOMS)
for room in rooms:
    print(room)
#print_anyList(rooms)
print('*'*20)



# Course Structure
#  course = [id,name,qty_students,times_per_week,[compatible_rooms]]

def create_courses(courseList, roomList):
    courses = []
    counter = 0
    for course in courseList:
        compatible_rooms = []
        compatible_rooms = set_compatible_rooms(course,roomList)
        new_course = [counter, course[0],course[1],course[2],compatible_rooms]
        courses.append(new_course)
        counter += 1
    return courses

def get_times_per_week(courseList,id):
    return courseList[id][3]

def set_compatible_rooms(course,roomList):
    compatible_rooms = []
    for room in roomList:
        if course[1] <= room[1]:
            compatible_rooms.append(room[0])
    return compatible_rooms
        

def get_compatible_rooms(course):
    return course[4]


print("PRINTING COURSES")
courses = create_courses(CRS,rooms)
print_anyList(courses)
print('*'*20)


# Class Structure
#  new_class = [id,course,time,room]
def create_class(counter, course, time, room):
    new_class = [counter, course, time, room]
    return new_class


# Schedule Structure
def create_schedule(courseList,timeList,roomList):
    rooms    = roomList
    courses  = courseList
    times    = timeList
    schedule = []
    for course in courses:
        id_counter    = 0
        compatible_rooms = get_compatible_rooms(course)
        times_counter = 0
        for room in compatible_rooms:
            print('times_counter [',times_counter,']','id_counter [',id_counter,']')
            for time in times:
                time_id   = time[0]
                occ_times = get_occ_times(rooms[room])
                if time[3] != True: # if time is available
                    if time_id not in occ_times:
                        print('\n\n')
                        print('timeList1: ',times)
                        print('alpha: ', times[id_counter])
                        times[id_counter][3] = True
                        print('betta: ', times[id_counter])
                        if rooms[room][2] is not None:
                            holder = rooms[room][2]
                            holder.append(time_id)
                            rooms[room][2] = holder
                        else:
                            rooms[room][2] = [time_id]
                        print('\nroom',room)
                        print('roomList: ',rooms)
                        new_class = create_class(id_counter,course,time,rooms[room])
                        schedule.append(new_class)
                        times_counter += 1  
                        print('id_counter',id_counter)
                        print('times_counter',times_counter)
                if times_counter >= course[2]:
                    times_counter += 1
                    break
    return schedule

def print_schedule(schedule):
    for each in schedule:
        print('course-id',  each[1][0])
        print('course-name',each[1][1])
        print('course-qty', each[1][2])
        print('course-tpw', each[1][3])
        #print('course-rooms',each[1][4])
        print('time-id',  each[2][0])
        print('time-day', each[2][1])
        print('time-time',each[2][2])
        print('time-flag',each[2][3])
        print('room-id',  each[3][0])
        print('room-capacity',each[3][1])
        print('room-occupied',each[3][2])
        print()

if (__name__ == '__main__'):
    print('_________Running Script!_________')
    mysch = create_schedule(courses,times,rooms)
    print('*'*20,'\nschedule\n')
    for i in mysch:
        print('i0', i[0], 'i1', i[1], 'i2', i[2], 'i3', i[3])
    #print_schedule(mysch)