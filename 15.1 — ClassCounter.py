class Counter:
    def __init__(self, min_, max_ , num):
        self.min_ = min_
        self.max_ = max_
        self.num = num

    def getMin(self):
        return self.min_

    def getMax(self):
        return self.max_

    def getNum(self):
        return self.num    

    def setMin(self): 
        while(True):
            inp = int(input('Введите минимальное значение счётчика: '))
            if 0 < inp < 999999999:
                self.min_ = inp
                break
            else:
                print('Недопустимое значение, попытайтесь ещё.')

    def setMax(self):
        while(True):
            inp = int(input('Введите максимально возможное значение счётчика: '))
            if self.min_ < inp < 999999999:
                self.max_ = inp
                break
            else:
                print('Недопустимое значение, попытайтесь ещё.')

    def setNum(self):
        while(True):
            inp = int(input('Введите текущее значение: '))
            if self.min_ <= inp <= self.max_:
                self.num = inp
                break
            else:
                print('Недопустимое значение, попытайтесь ещё.')

    def plus_one(self):
        if self.num < self.max_:
            self.num += 1
            print('Значение счётника была повышено на один.')
            if self.num == self.max_:
                print('Счетчик достиг своего максимального значения.')
        else:
            print('Счетчик достиг своего максимального значения.')

    def show(self):
        print('На данный момент значение счетчика — {} из {} возможных.'.format(self.num, self.max_))         

print('Счетчик номер 1:')
counter_1 = Counter(1, 15, 12)

counter_1.show()
counter_1.plus_one()
counter_1.show()

counter_2 = Counter(0, 0, 0)
print('\nСчетчик номер 2:')
counter_2.setMin()
counter_2.setMax()
counter_2.setNum()

times_plus_one = int(input('Введите, на сколько единиц вы хотите повысить значение счётчика.\nВведите 0, если хотите повысить значение до максимума: '))
if times_plus_one == 0 or counter_2.max_ - counter_2.num < times_plus_one:
    for _ in range(counter_2.max_ - counter_2.num):
        counter_2.plus_one()
        counter_2.show()
else:
    for _ in range(times_plus_one):
        counter_2.plus_one()
        counter_2.show()

print('\n\nThe end.')
