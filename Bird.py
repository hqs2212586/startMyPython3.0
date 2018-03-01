class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print ('Aaaaah....')
            self.hungry = False
        else:
            print ('No, thanks!')


class Songbird(Bird):
    def __init__(self):
        super(Songbird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print (self.sound)


sb = Songbird()
sb.sing()
sb.eat()
sb.eat()