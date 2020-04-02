# Создать класс, описывающий группу студентов - `Group`.
# Данный класс хранит студентов в виде списка объектов `Student` также реализованного в виде соответствующего класса.
# В классах реализовать необходимай набор атрибутов
# (Например, класс `Student` должен иметь атрибуты `name`, `age`, `grades`), а также
# необходимый набор методов экземпляра для работы с этими экземплярами.

class Group:
    def __init__(self, gr_name, num_of_students, lst_of_students):
        self._gr_name = self.verify_gr_name(gr_name)
        self._num_of_students = self.verify_num_of_students(num_of_students)
        self._lst_of_students = self.verify_lst_of_students(lst_of_students)

    @property  # Getter <Name of Group>
    def gr_name(self):
        return self._gr_name
    
    @property  # Getter <Num of Students>
    def num_of_students(self):
        return self._num_of_students
    
    @property  # Getter <List of Students>
    def lst_of_students(self):
        return self._lst_of_students

    @gr_name.setter  # Setter <Group name>
    def gr_name(self, gr_name):
        self.verify_gr_name(gr_name)

    def verify_gr_name(self, gr_name):
        try:
            if len(gr_name) == 5 and gr_name.startswith(('AS', 'AM', 'AK', 'AE', 'AI', 'AV', 'AA', 'AT', 'AD')) == True and (isinstance(int(gr_name[2:]), int)) == True:
                self._gr_name = gr_name
                return self._gr_name
            else:
                print('Ввод группы должен начинаться с кода (AS, AM, AK, AE, AI, AV, AA, AT, AD) и заканчиваться трёмя числами.\n')
        except:
            print('Ошибка! Ввод группы должен начинаться с кода (AS, AM, AK, AE, AI, AV, AA, AT, AD) и заканчиваться трёмя числами.\n') 

    @num_of_students.setter  # Setter <Number of students>
    def num_of_students(self, num_of_students):
        self.verify_num_of_students(num_of_students)
        
    def verify_num_of_students(self, num_of_students):
        try:
            if 0 <= num_of_students <= 30:
                self._num_of_students = num_of_students
                return self._num_of_students
            else:
                print("Недопустимое количество студентвов. Введите число от 1 до 30.\n")
        except:
            print('Неправильный ввод данных. Введите число от 1 до 30.\n')
    
    @lst_of_students.setter  # Setter <list of students>
    def lst_of_students(self, lst_of_students):
        verify_lst_of_students(lst_of_students)
    
    def verify_lst_of_students(self, lst_of_students):
        try:
            if type(lst_of_students) == list:
                self._lst_of_students = lst_of_students
                return self._lst_of_students
            else:                
                print(r"Первоначальный список студентов должен подаваться в форме [<Имя_студента>, <Имя_студента>]")
        except:
            print(r"Ошибка! Первоначальный список студентов должен подаваться в форме [<Имя_студента>, <Имя_студента>]")
    
    def display_info(self):         
        lst_of_names = [i.name for i in self._lst_of_students]
        lst_of_names = [len(x) for x in lst_of_names]
        max_len_of_name = max(lst_of_names)        
        
        lst_of_numbers = [i.num_in_gr for i in self.lst_of_students]
        lst_of_numbers.sort()
        
        if self._num_of_students == 1:
            print("В группе под номером", self._gr_name, " один студент.")
            for i in self._lst_of_students:
                print('•', '{:>2}'.format(i.num_in_gr), '•', i.name + ' '*(max_len_of_name-len(i.name)), '• Оценки:', end = ' ')
                for x in range(len(i.grades)):
                    if x < len(i.grades)-1:
                        print(i.grades[x], end = ', ')
                    else:
                        print(i.grades[x], end = '.')
                
        elif 2 <= self._num_of_students <= 4:
            print("В группе под номером", self._gr_name, self._num_of_students, "студента.")
            print('Список студентов: ')
            for num in lst_of_numbers:
                for i in self.lst_of_students:
                    if num == i.num_in_gr:
                        print('•', '{:>2}'.format(i.num_in_gr), '•', i.name + ' '*(max_len_of_name-len(i.name)), '• Оценки:', end = ' ')
                        for x in range(len(i.grades)):
                            if x < len(i.grades)-1:
                                print(i.grades[x], end = ', ')
                            else:
                                print(i.grades[x], end = '.')
                        break
        
        else: 
            print("В группе под номером", self._gr_name, self._num_of_students, "студентов.")
            print('Список студентов: ')
            for num in lst_of_numbers:
                for i in self.lst_of_students:
                    if num == i.num_in_gr:
                        print('•', '{:>2}'.format(i.num_in_gr), '•', i.name + ' '*(max_len_of_name-len(i.name)), '• Оценки:', end = ' ')
                        for x in range(len(i.grades)):
                            if x < len(i.grades)-1:
                                print(i.grades[x], end = ', ')
                            else:
                                print(i.grades[x], end = '.')
                        break

class Student:
    def __init__(self, name, age, grades, num_in_gr, gr_num):
        self._name = self.verify_name(name)
        self._age = self.verify_age(age)
        self._grades = self.verify_grades(grades)
        self._num_in_gr = self.verify_num_in_gr(num_in_gr)
        self._gr_num = self.verify_gr_num(gr_num)

    @property  # Getter <Name>
    def name(self):
        return self._name
    
    @property  # Getter <Age>
    def age(self):
        return self._age

    @property  # Getter <Grades>
    def grades(self):
        return self._grades
    
    @property  # Getter <Num in group>
    def num_in_gr(self):
        return self._num_in_gr

    @property  # Getter <Group Number>
    def gr_num(self):
        return self._gr_num
    
    @name.setter  # Setter <Name>
    def name(self, name):
        verify_name(name)
    
    def verify_name(self, name):
        try:
            if name.isalpha() == True:
                self._name = name
                return self._name
            else:
                print("Недопустимое имя, возможно использовать лишь алфавит.")
        except:
            print("Ошибка! Недопустимое имя, возможно использовать лишь алфавит.")
    
    @age.setter  # Setter <Age>
    def age(self, age):
        self.verify_age(age)
    
    def verify_age(self, age):
        try:
            if 1 <= age <= 115:
                self._age = age
                return self._age
            else:
                print("Недопустимый возраст. Возможен возраст от 1 до 115.")
        except:
            print("Ошибка! Недопустимый возраст. Возможен возраст от 1 до 115.")

    @grades.setter  # Setter <Grades>
    def grades(self, grades):
        self.verify_grades(grades)

    def verify_grades(self, grades):
        try:
            lst = list(map(int, grades.split(' ')))
            if (all( 1 <= i <= 100 for i in lst)) == True:
                self._grades = lst
                return self._grades
            else:
                print('Возможен ввод лишь целых чисел от 1 до 100. Ввод в формате <94 71 63...>')
        except:
            print('Ошибка! Возможен ввод лишь целых чисел от 1 до 100. Ввод в формате <94 71 63...>')

    @num_in_gr.setter  # Setter <Number in group>
    def num_in_gr(self, num_in_gr):
        self.verify_num_in_gr(num_in_gr)
    
    def verify_num_in_gr(self, num_in_gr):
        try:
            if num_in_gr in range(1, 31):
                self._num_in_gr = num_in_gr
                return self._num_in_gr
            else:
                print("Введите номер от 1 до 30.")
        except:
            print("Ошибка! Введите номер от 1 до 30.")
    
    @gr_num.setter  # Setter <Group number>
    def gr_num(self, gr_num):
        self.verify_gr_num(gr_num)

    def verify_gr_num(self, gr_num):
        try:
            if len(gr_num) == 5 and gr_num.startswith(('AS', 'AM', 'AK', 'AE', 'AI', 'AV', 'AA', 'AT', 'AD')) == True and (isinstance(int(gr_num[2:]), int)) == True:
                self._gr_num = gr_num
                return self._gr_num
            else:
                print('Ввод группы должен начинаться с кода (AS, AM, AK, AE, AI, AV, AA, AT, AD) и заканчиваться трёмя числами.')
        except:
            print('Ошибка! Ввод группы должен начинаться с кода (AS, AM, AK, AE, AI, AV, AA, AT, AD) и заканчиваться трёмя числами.') 

    def display_info(self):
        print("Студент по имени", self._name, "возрастом в", self._age, "лет состоит в группе", self._gr_num, "под номером", self._num_in_gr, "имея следующие баллы: ", end = '')
        for x in range(len(self.grades)):
            if x < len(self.grades)-1:
                print(self.grades[x], end = ', ')
            else:
                print(self.grades[x], '\b.')

        
    def verify_input(self):
        if self.name == None or self.age == None or self.grades == None or self.num_in_gr == None or self.gr_num == None:
            print('Данные введены неверно, давайте попробуем ещё раз :с\n')
            return False  
        else:           
            print('Данные введены верно, поздравляем!')
            return True      

if __name__ == '__main__':
    
    print('\t')
    print('На данный момент у нас есть три студента. Давайте расскажем о них.')
    Alex = Student('Alexey', 20, '56 74 98 31 94', 4, 'AS193')
    Alex.display_info()
    Dan = Student('Daniil', 17, '75 86 79 64 97', 14, 'AS193')
    Dan.display_info()
    Bogdan = Student('Bogdan', 18, '61 79 80 76 84', 5, 'AS193')
    Bogdan.display_info()
    
    print('\t')
    print('Также у нас есть группа AS193, в которой они втроём состоят. Теперь о нашей группе.')
    as193 = Group('AS193', 3, [Dan, Alex, Bogdan])
    as193.display_info()
    
    print('\t')
    print('Недавно у Даниила был День Рождения. Теперь ему 18. Давайте обновим информацию и снова выведём её.')
    Dan.age = 18
    Dan.display_info()
    lst_of_all_groups = [as193]
    
    print('\t')
    print('Отлично, всё работает! А мы, поздравив Даниила с Днём Рождения, двигаемся дальше.')
    print('На данный момент у нас есть три студента и одна группа.')
    print('Давайте выберем, что будет делать дальше:')
    print('  Добавим новых студентов в группу AS193 (нажмите 1)\n  Создадим новую группу (нажмите 2) ?')    
    
    while (True):
        n = int(input('Ввод: '))        
        if n == 1 or n == 2:
            break
        else:  # неправильный ввод
            print('Читерить нельзя! Только 1 или 2 :3')

    if n == 1:  # добавляем студентов в AS193
        print('\nМы решили добавить студентов в группу AS193, отлично (это лучшая группа, отличный выбор).')
        print('Теперь решим, мы уже знаем, сколько студентов будем добавлять (1) или будем добавлять их по одному (2)?')
        
        while (True):
            x = int(input('Ваш выбор: '))
            if x == 1 or x == 2:
                break
            else:  # неправильный ввод
                print('Давайте введём данные правильно :с')            
                     
        if x == 1:  # знаем, сколько студентов будем добавлять
            
            while (True):
                num = int(input('В группу AS193 мы добавим столько студентов: '))
                if num >= 1:
                    break
                else:
                    print('Мы можем добавить только положительное число студентов :)')
                    
            print()
            for i in range(num):
                print('Добавляем {}-го студента в группу AS193.\n'.format(i + 4))
                
                while (True):
                    name = input('Имя студента (только буквы): ')
                    age = int(input('Возраст студента (1-115): '))
                    grades = input('Оценки студента в формате <65 78 92 ...>: ')
                    num_in_gr = int(input('Номер студента по журналу (1-30): '))                       
                    
                    student = Student(name, age, grades, num_in_gr, 'AS193')
                    if student.verify_input() == True:
                        print('\nМы добавили нового студента:')
                        student.display_info()
                        as193.num_of_students += 1
                        as193.lst_of_students.append(student)
                        break
            
            print('\nОтлично! Теперь у нас в группе AS193 {} студентов. Давайте посмотрим новый состав группы:'.format(num+3))
            as193.display_info()
        
        elif x == 2:  # добавлять в AS193 по одному
            while(True):  
                print('Добавляем {}-го студента в группу AS193.\n'.format(as193.num_of_students + 1))

                while (True):
                    name = input('Имя студента (только буквы): ')
                    age = int(input('Возраст студента (1-115): '))
                    grades = input('Оценки студента в формате <65 78 92 ...>: ')
                    num_in_gr = int(input('Номер студента по журналу (1-30): '))  
                    
                    student = Student(name, age, grades, num_in_gr, 'AS193')
                    if student.verify_input() == True:
                        print('\nМы добавили нового студента:')
                        student.display_info()
                        as193.num_of_students += 1
                        as193.lst_of_students.append(student)
                        break
                
                while (True):
                    m = int(input('Мы будем добавлять ещё одного студента? (0 - нет, 1 - да): '))
                    if m == 0:
                        print('\nХорошо, тогда с AS193 пока закончили! Вот как выглядит обновлённая группа:')
                        as193.display_info()
                        print()
                        break
                    elif m == 1:
                        break
                    else:
                        print('Ошибка :с, давайте попробуем ещё раз...')                    
                break
        
        while (True):  # будем ли создавать другие группы или закончим
            n = int(input('\nТеперь вопрос. Мы будем добавлять студентов в другие группы? Наш выбор (1 - да, 0 - нет): '))
            if n == 0:
                print('Конец программы! В итоге мы дополнили нашу группу AS193.\n')
                break
            elif n == 1:
                n = 2
                break
            else:
                print('Ввод не верен :"c')
    
    if n == 2:  # добавляем студентов в другие группы
        print('\nДавайте создадим новые группы из студентов.')
        
        while True:  # создаём новую группу
            
            print('Ввод группы должен начинаться с кода (AS, AM, AK, AE, AI, AV, AA, AT, AD) и заканчиваться трёмя числами.\n')
            while (True):
                name_gr = input('Имя группы: ')                    
                if len(name_gr) == 5 and name_gr.startswith(('AS', 'AM', 'AK', 'AE', 'AI', 'AV', 'AA', 'AT', 'AD')) == True and (isinstance(int(name_gr[2:]), int)) == True:
                    break
                else:
                    print('Неверный ввод.')
            
            name_gr = Group(name_gr, 0, [])               
            
            print('Теперь решим, мы уже знаем, сколько студентов будем добавлять (1) или будем добавлять их по одному (2)?')
            while (True):
                x = int(input('Ваш выбор: '))
                if x == 1 or x == 2:
                    break
                else:  # неправильный ввод
                    print('Давайте введём данные правильно :с')
                
                
            if x == 1:  # знаем, сколько студентов будем добавлять
                
                while (True):  
                    num = int(input('В группу {} мы добавим столько студентов: '.format(name_gr.gr_name)))
                    if num >= 1:
                        break
                    else:
                        print('Мы можем добавить только положительное число студентов :)')
                
                print()
                for i in range(num):  # добавляем студентов
                    print('Добавляем {}-го студента в группу {}.\n'.format(i+1, name_gr.gr_name))
                    
                    while (True):
                        name = input('Имя студента (только буквы): ')
                        age = int(input('Возраст студента (1-115): '))
                        grades = input('Оценки студента в формате <65 78 92 ...>: ')
                        num_in_gr = int(input('Номер студента по журналу (1-30): '))                       
                        
                        student = Student(name, age, grades, num_in_gr, name_gr.gr_name)
                        if student.verify_input() == True:
                            print('\nМы добавили нового студента:')
                            student.display_info()
                            name_gr.num_of_students += 1
                            name_gr.lst_of_students.append(student)
                            break
                
                print('\nОтлично! Теперь у нас в группе', name_gr.gr_name, num, 'студентов. Давайте посмотрим новый состав группы:')
                name_gr.display_info()
                lst_of_all_groups.append(name_gr)
                break
            
            elif x == 2:  # добавлять в группу по одному
                while(True):
                    print('Добавляем {}-го студента в группу {}.\n'.format(name_gr.num_of_students + 1, name_gr.gr_name))

                    while (True):
                        name = input('Имя студента (только буквы): ')
                        age = int(input('Возраст студента (1-115): '))
                        grades = input('Оценки студента в формате <65 78 92 ...>: ')
                        num_in_gr = int(input('Номер студента по журналу (1-30): '))  
                        
                        student = Student(name, age, grades, num_in_gr, name_gr.gr_name)
                        if student.verify_input() == True:
                            print('\nМы добавили нового студента:')
                            student.display_info()
                            name_gr.num_of_students += 1
                            name_gr.lst_of_students.append(student)
                            break
                    
                    while (True):
                        n = int(input('Мы будем добавлять ещё одного студента? (0 - нет, 1 - да): '))
                        if n == 0 or n == 1:
                            break
                        else:
                            print('Ошибка :с, давайте попробуем ещё раз...')                           

                    if n == 0:
                        print('\nХорошо, тогда с {} пока закончили! Вот как выглядит обновлённая группа:'.format(name_gr.gr_name))
                        name_gr.display_info()
                        lst_of_all_groups.append(name_gr)
                        break

            print('\nВиу, дела идут отлично. Будем создавать ещё одну группу (1 - да, 0 - нет)?')
            while(True):
                k = int(input('И мы...: '))
                if k == 1 or k == 0:
                    break
                else:
                    print('Ошибка, давайте попытаемся ещё раз.') 
                        
            if k == 0:
                print('Отлично, тогда закончили!\n')
                break

    
    print('\n\nВот и конец.')
    print('Вот какие группы у нас в итоге вышли:\n')
    for i in lst_of_all_groups:
        print(i.display_info())
        print()

    print("\nThat's the real end. Thank you very much for everything!")
