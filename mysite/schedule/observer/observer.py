import schedule
import time
from mysite.schedule.models import Client, Appointment
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

def job():
    print (Appointment.objects)
    print (Client.objects)

schedule.every().day.at("13:53").do(job)

# if __name__ == '__main__':
#     while True:
#         schedule.run_pending()
#         time.sleep(1)  # wait one minute



class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:

        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()

# from datetime import datetime
# from threading import Timer
# x=datetime.today()
# y=x.replace(day=x.day, hour=0, minute=0, second=5, microsecond=0)
# delta_t=y-x
# secs=delta_t.seconds
# def hello_world():
#     print ("hello world")
#     #...
#
#
# if __name__ == '__main__':
#     t = Timer(secs, hello_world)
#     t.start()

