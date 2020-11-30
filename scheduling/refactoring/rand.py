from random import shuffle
from sampledata import DAYS_OF_WEEK as DOW
from sampledata import TIME_SLOTS as TL
from sampledata import ROOMS
from sampledata import COURSES as CRS
#from sampledata import DEPT1_COURSES as CRS

def print_anyList(anyList):
    for _ in anyList: print(_)

def rand_anyList(aList):
    randList = aList
    shuffle(randList)
    return randList

#**********************************************************************************************
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

#**********************************************************************************************
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

#**********************************************************************************************
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

#**********************************************************************************************
# Class Structure
#  new_class = [id,course,time,room]
def create_class(counter, course, time, room):
    new_class = [counter, course, time, room]
    return new_class

#**********************************************************************************************
# Schedule Structure
def create_schedule(courseList,timeList,roomList):
    rooms    = roomList
    courses  = courseList
    shuffle(courses)                                       # Randomizing
    times    = timeList
    shuffle(times)                                         # Randomizing
    schedule = []
    counter  = 0
    for course in courses:
        repeat = 0
        compatible_rooms = get_compatible_rooms(course)    # Randomizing
        shuffle(compatible_rooms)
        for room in compatible_rooms:
            for time in times:
                if repeat == course[3]:
                    break
                else:
                    time_id = time[0]
                    if time[3] != True: # if time is available
                        if time_id not in rooms[room][2]:
                            holder = rooms[room][2]
                            holder.append(time_id)
                            rooms[room][2] = holder
                            new_class = create_class(counter,course,time,rooms[room])
                            schedule.append(new_class)
                            counter += 1
                            repeat  += 1
    return schedule

def organize_schedule(schedule):         # In order to work, Course Name must have last character set as semester id.
    semList = []                         # Ex: LOGA1 = 1st semester; SOPA2 = 2nd semester; DW2A6 = 6th semester.
    for each in schedule:
        holder = int((each[1][1])[-1])   # Covnert last char of CourseName to Int 
        semList.append(holder)
    semList = list(set(semList))         # Convert to SET to get unique items, convert back to LIST
    semList.sort()
    new_sched = []
    for item in semList:
        semester = []
        for course in schedule:
            beta = int((course[1][1])[-1])
            if beta == item:
                semester.append(course)
        new_sched.append(semester)
    return(new_sched)

def print_grid(schedule):
    print(end="\t\t")
    for day in DOW:
        print(day,end="\t\t")
    print('\n')    
    for time_slot in TL:
        print(time_slot, end="\t")
        for day in DOW:
            for each in schedule:
                if each[2][2] == time_slot: 
                    if each[2][1] == day:
                        print(f'{each[1][1]}(R{each[3][0]})', end="\t")
        print('\n','-'*100)
        
       
if (__name__ == '__main__'):
    #Defining VARS
    rooms = create_rooms(ROOMS)
    
    print('\n','*'*40,'\n TEST SCHEDULE:\n','*'*40)
    courses = create_courses(CRS,rooms)
    mysch   = create_schedule(courses,times,rooms)
    for i in mysch:
        print('SCHEDULE #', i)
        print('CLASSid', i[0], '\tCOURSE\t', i[1], '\t\tTIME', i[2], '\tROOMid', i[3][0])
        
    organized = organize_schedule(mysch)
    
    for i,j in enumerate(organized):
        print('*'*120)
        print('\t\t SCHEDULE # ', i)
        print('*'*120)
        print_grid(j)
