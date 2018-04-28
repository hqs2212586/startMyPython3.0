"""
软件重用的重要方式除了继承之外还有另外一种方式，即：组合

组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合

当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好
"""

class People:
    school = 'Luffycity'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Teacher(People):
    def __init__(self, name, age, sex, level, salary):
        super().__init__(name, age, sex)
        self.level = level
        self.salary = salary

    def teach(self):
        print('%s is teaching' % self.name)


class Student(People):
    def __init__(self, name, age, sex, class_time):
        super(Student, self).__init__(name, age, sex)

        self.class_time = class_time

    def learn(self):
        print('%s is learning' % self.name)


class Course:  # 课程和老师的关系，是有没有（组合）的关系，不是是不是（继承）的关系
    def __init__(self, course_name, course_price, course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period

    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' % (self.course_name, self.course_price, self.course_period))


class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_info(self):
        print('%s-%s-%s' % (self.year, self.mon, self.day))

teacher1 = Teacher('alex', 18, 'male', 10, 3000)

python = Course('python', 3000, '3mons')
linux = Course('linux', 4000, '4mons')
student1 = Student('张三', 28, 'female', '08:30:00')
teacher1.course = python  # 老师对象增加一个课程属性，赋值是课程对象

# print(python)
# print(teacher1.course)
# print(teacher1.course.course_name)  # 输出：python
"""
<__main__.Course object at 0x104037198>
<__main__.Course object at 0x104037198>
python
"""

teacher1.course.tell_info()
"""
课程名<python> 课程价钱<3000> 课程周期<3mons>
"""
student1.course1 = python  # 对象增加一个属性，指向了一个课程对象
student1.course2 = linux

student1.course1.tell_info()
student1.course2.tell_info()

student1.courses = []
student1.courses.append(python)
student1.courses.append(linux)

# student1 = Student('张三', 28, 'female', '08:30:00')
# d = Date(1988, 4, 20)
# python = Course('Python', 3000, '3mons')
#
# student1.birth = d
# student1.birth.tell_info()   # 1988-4-20
# student1.course = python
# student1.course.tell_info()   # 课程名<Python> 课程价钱<3000> 课程周期<3mons>
"""
1988-4-20
课程名<Python> 课程价钱<3000> 课程周期<3mons>
"""