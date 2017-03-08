import datetime
class PersonTypeError(TypeError):
    pass
class PersonValueError(ValueError):
    pass

class Person:
    _num = 0
    def __init__(self, name, sex, birthday, ident):
        if not(isinstance(name, str) and sex in ('女', '男')):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date:', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1
    def id(self): return self._id
    def name(self): return self._name
    def sex(self): return self._sex
    def birthday(self): return self._birthday
    def age(self): return (datetime.date.today().year - self._birthday.year)
    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError('set_name', name)
        self._name = name
    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError(other)
        return self._id < other._id
    @classmethod
    def num(cls): return cls._num
    def __str__(self):
        return ' '.join((self._id, self._name, self._sex, str(self._birthday)))
    def details(self):
        return ','.join(('编号： '+ self._id, "姓名： " + self._name, '性别： ' + self._sex, '出生日期' + str(self._birthday)))


class Student(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}
    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('No this course selected:', course_name)
        self._courses[course_name] = score
    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]
    def details(self):
        return ','.join((Person.details(self),'入学日期： ' + str(self._enroll_date), '院系： ' + self._department,'课程记录： ' + str(self.scores())))
class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)
    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError('Wrong date:', entry_date)
        else :
            self._entry_date = datetime.date.today()
        self._salary = 120
        self._department = "未定"
        self._position = '未定'
    def set_salary(self, amount):
        assert type(amount) is int
        self._salary = amount
    def set_position(self,position):
        self._position = position
    def set_department(self, department):
        self._department = department
    def details(self):
        return ','.join((super().details(),'入职日期： ' + str(self._entry_date),
                         '院系： ' + self._department, '职位： ' + self._position, '工资： ' + str(self._salary)))

class Time:
    def __init__(self, hours, minutes, seconds):
        assert all((isinstance(i, int) and i >=0 for i in (hours, minutes, seconds)))
        self._total = hours * 3600 + minutes * 60 + seconds
        dm, self._seconds = divmod(seconds, 60)
        minutes += dm
        dh, self._minutes = divmod(minutes, 60)
        self._hours = hours + dh
    def hours(self):
        return self._hours
    def minutes(self):
        return self._minutes
    def seconds(self):
        return self._seconds
    def __eq__(self, other):
        assert isinstance(other, Time)
        return self._total == other._total
    def __lt__(self, other):
        assert isinstance(other, Time)
        return self._total < other._total
    def __ge__(self, other):
        assert isinstance(other, Time)
        return self._total >= other._total
    def __add__(self, other):
        assert isinstance(other, Time)
        return Time(self._hours + other.hours, self._minutes + other.minutes, self._seconds + other.seconds())
    def __sub__(self, other):
        assert isinstance(other, Time)
        assert self >= other
        return Time(0,0,self._total - other._total)
    def __str__(self):
        return '{}:{:02}:{:02}'.format(self._hours, self._minutes, self._seconds)



