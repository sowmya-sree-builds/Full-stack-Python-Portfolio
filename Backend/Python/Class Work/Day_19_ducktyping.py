# if it walks like a duck, quacks like a duck then it is a duck

class dog:
    def walk(self):
        print('dog can walk')

    def speak(self):
        print('it barks')

class Horse:
    def walk(self):
        print('Horse can walk')

    def speak(self):
        print('It whines')

class kavys:
    def walk(self):
        print('walks like a sloth')

    def speak(Self):
        print('speaks like a crow')


def checking(being):
    being.walk()
    being.speak()
    print('yes, it is an animal')

dog1=dog()

horse1=Horse()

kavys1=kavys()

checking(dog1)
print(' ')
checking(horse1)
print(' ')
checking(kavys1)



class demon_slayer:
    def lang(self):
        print('It is in japanese language')
    def subtitles(self):
        print('It contains subtitles')

class stranger_things:
    def lang(self):
        print('It is in English language')
    def subtitles(self):
        print('It contains subtitles')

class Squid_game:
    def lang(self):
        print('It is in korean language')
    def subtitles(self):
        print('It contains subtitles')

def can_watch(info):
    info.lang()
    info.subtitles()
    print('----- yes Can watch the series ----')
print(' ')
demon=demon_slayer()
death_note1=stranger_things()
goblin1=Squid_game()

can_watch(demon)
print(' ')
can_watch(death_note1)
print(' ')
can_watch(goblin1)
