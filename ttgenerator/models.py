class Data:
    """ """
    
class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._conflicts = 0
        self._fitness = -1
        self._classNum = 0
        self._isFitnessModified = True 
        
class Population:
    """ """
    
class GeneticAlg:
    """ """
    
class Course:
    def __init__(self, number, name, slots, teacher):
        self._number     = number
        self._name       = name
        self._slots      = slots
        self._teacher    = teacher
    
    def get_number(self):   return self._number
    def get_name(self):     return self._name
    def get_slots(self):    return self._slots
    def get_teacher(self):  return self._teacher
    def __str__(self):      return self._name
    

class Teacher:
    def __init__(self, id, name):
        self._id        = id
        self._name      = name
    
    def get_id(self):       return self._id
    def get_name(self):     return self._name
    def __str__(self):      return self._name
    
class Room:
    def __init__(self, number, capacity):
        self._number    = number
        self._capacity  = capacity
    
    def get_number(self):       return self._number
    def get_capacity(self):     return self._capacity
    def __str__(self):      return self._capacity

class Time:
    def __init__(self, id, time):
        self._id    = id
        self._time  = time
    
    def get_id(self):       return self._id
    def get_time(self):     return self._time
    def __str__(self):      return self._time
    
class Class:
    def __init__(self, id, course):
        self._id        = id
        self._course    = course
        self._teacher   = None
        self._time      = None
        self._room      = None
    
    def get_id(self):       return self._id
    def get_course(self):   return self._course
    def get_teacher(self):  return self._teacher
    def get_time(self):     return self._time
    def get_room(self):     return self._room
    
    def set_teacher(self, teacher): self._teacher = teacher
    def set_time(self, time):       self._time    = time
    def set_room(self, room):       self._room    = room
    
    def __str__(self):
        return  f'{self_course.get_number()},{self._room.get_number()},' \
                f'{self._teacher.get_id()},{self._time.get_id()}'
    










""" class Times(object):
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
 """