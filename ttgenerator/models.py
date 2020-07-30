class Times(object):
    def __init__(self):
        self.nrWeeks     = nrWeeks
        self.days        = days
        self.periods     = periods
    
class Room(object):
    def __init__(self):
        self.roomId      = roomId
        self.capacity    = capacity
class Teacher(object):
    def __init__(self):
        self.teacherId = teacherId
        self.name      = name
        
class Course(object):
    def __init__(self):
        self.courseId   = courseId
        self.name       = name
        self.teacher    = teacher
        #self.time = time....
        self.slots      = slots

class Curricula(object):
    def __init__(self):
        self.curriculaId     = curriculaId
        self.numberOfCourses = numberOfCourses
        self.listOfCourses   = listOfCourses
        
class Student(object):
    def __init__(self):
        self.studentId     = studentId
        self.name          = name
        self.listOfCourses = listOfCourses
