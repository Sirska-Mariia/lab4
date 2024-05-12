"""
automaton
"""
from collections import deque
import random
class STATE:
    """
    state
    """
    STUDY = "studying"
    EAT = "eating"
    SLEEP = "sleeping"
    REST = "resting"
    GO = "going"
    def __init__(self) -> None:
        pass

class DAY:
    """
    day
    """
    STATE = None
    TIME = deque()
    for i in range(0,24):
        TIME.append(i)
    def __init__(self) -> None:
        self.state = STATE.SLEEP
        self.weekday = random.randint(1,7)
    def change_state(self):
        """
        changes current state
        """
        weekday = self.weekday
        hour = DAY.TIME.popleft()
       # print(hour)
        if self.state == STATE.SLEEP and 0<=hour<7:
            print('sleeping')
        elif self.state == STATE.SLEEP and 9>=hour>= 7:
            if weekday <=5:
                print("now it's time to go to university")
                if random.randint(0,1)== 0:
                    print("I am not hungry")
                    self.state = STATE.GO
                else:
                    print('eating')
                    self.state = STATE.EAT
            else:
                print("It's weekend, no need to wake up yet")
        elif weekday <=5 and self.state == STATE.EAT and (hour == 8 or hour == 7):
            print('go')
            self.state = STATE.GO
        elif weekday <=5  and self.state == STATE.GO and (hour == 8 or hour == 9):
            print('arrived to the university')
            self.state = STATE.STUDY
        elif weekday <=5 and self.state == STATE.GO and hour == 17:
            print('arrived home, time to eat')
            self.state = STATE.EAT
        elif weekday <=5 and self.state == STATE.STUDY and hour == 13:
            print('eating lunch')
            self.state = STATE.EAT
       # elif self.state == self.STUDY and hour == 13:
       #     self.STATE = STATE.EAT
        elif  weekday <=5 and self.state == STATE.EAT and hour == 14:
            self.state = STATE.STUDY
        elif  weekday <=5 and self.state == STATE.STUDY and hour == 16:
            self.state = STATE.GO
            print('returnung home')
        elif  weekday <=5 and hour == 0 and random.randint(1,10)>6:
            print('already sleepy')
            self.state = STATE.SLEEP
        elif weekday <=5 and self.state== STATE.EAT or self.state == STATE.STUDY and 23 >= hour >= 18 or hour == 0:
            if random.randint(0,10) < 5:
                print('free time')
                self.state = STATE.REST
            else:
                print("need to study")
                self.state = STATE.STUDY
            if hour == 0 and self.state == STATE.STUDY :
                print('still need to study')
            elif hour == 0 and self.STATE == STATE.REST:
                print('not sleepy yet')
        elif weekday <=5 and 3>= hour >=1 and self.state != STATE.SLEEP:
            print("time to sleep")
            self.state = STATE.SLEEP
        elif self.state == STATE.SLEEP and weekday > 5 and hour == 10 and random.randint(1,5) <= 2:
            print("time to wake up")
            self.state = STATE.EAT
            print("eating")
        elif self.state == STATE.SLEEP and weekday > 5 and hour == 11:
            print("time to wake up and eat")
            self.state = STATE.EAT
        elif self.state == STATE.EAT and weekday > 5:
            self.state = STATE.REST
        elif (self.state == STATE.REST or self.state == STATE.STUDY)  and weekday > 5 and random.randint(1,6) > 3:
            self.state = STATE.STUDY
            print("need to do the task, the deadline is soon")
        elif self.state == STATE.STUDY  and weekday > 5 and random.randint(1,6) > 3:
            self.state = STATE.REST
            print("already tired, need some break")
        elif weekday > 5 and hour == 15:
            self.state= STATE.EAT
            print('time for dinner')
        elif weekday > 5 and hour == 16 and random.randint(1,3) == 3:
            print('good weather, time to go for a walk')
            self.state = STATE.GO
        elif weekday > 5 and  self.STATE == STATE.GO:
            print("returned home")
            self.state = STATE.REST
        elif weekday > 5 and hour == 1:
            print("felling sleepy")
            self.state = STATE.SLEEP
        #print(self.STATE, 'STATE')
    def create_day(self):
        """
        saves all states during the day
        """
        model = []
        while len(self.TIME) > 0:
            self.change_state()
            model.append(self.state)
            #print(self.weekday, self.state, 'ffffffff')
        return model
   # def create_diagrahm(self):
   #     pass

day = DAY()
print(day.create_day())
