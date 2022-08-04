from abc import ABCMeta, abstractclassmethod

class MovingAverage(metaclass=ABCMeta):
    @abstractclassmethod
    def average(self):
        pass