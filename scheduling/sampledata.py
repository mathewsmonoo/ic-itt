TEACHERS = [
    ["001", "Alberto"],
    ["002", "Bruna"],
    ["003", "Caio"],
    ["004", "Duda"],
    ["005", "Eder"],
]
TEACHER_LIST = [i for i in TEACHERS]

ROOMS = [
    ["R1", 25],
    ["R2", 30],
    ["R3", 45],
    ["R4", 40],
    ["R5", 35],
    ["R6", 45],
]
ROOM_LIST = [i for i in ROOMS]

COURSES = [
     
    ["C1", TEACHER_LIST[0], 20, 4],
    ["C2", TEACHER_LIST[1], 25, 2],
    ["C3", TEACHER_LIST[2], 45, 6],
    ["C4", TEACHER_LIST[3], 30, 3],
    ["C5", TEACHER_LIST[4], 35, 4],
    ["C6", TEACHER_LIST[0], 25, 2],
]
COURSE_LIST = [i for i in COURSES]

TIMES = [
   #[id,   start - finish]
    ["1", "07:30 - 08:20"], # First Class
    ["2", "08:20 - 09:10"],
    # 20min break
    ["3", "09:30 - 10:20"], 
    ["4", "10:20 - 11:10"],
     # 10min break
    ["5", "11:20 - 12:10"], 
    ["6", "12:10 - 13:00"], # Last Class
]

WEEK = {
   #'DAY':ListOFClasses,
    'MON':None,
    'TUE':None,
    'WED':None,
    'THU':None,
    'FRI':None,
}

