"""
10 students per hour
2 printings per student
==> 10 * 2 = 20 tasks per hour
==> 1 task per 180 seconds

1 - 20 pages per task

normal: 10 pages per min
good: 5 pages per min

==> 
"""

import random
from queue import Queue

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagePerMinute):
    printer = Printer(pagePerMinute)
    printerQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask() == True:
            task = Task(currentSecond)
            printerQueue.put(task)
        
        if (printer.busy() == False) and (printerQueue.empty() == False):
            nextTask = printerQueue.get()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            printer.startNext(nextTask)
        
        printer.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("* Average Wait {:.2f} seconds, {} tasks remaining".format(averageWait, printerQueue.qsize()))


if __name__ == "__main__":
    for i in range(100):
        simulation(3600, 5)
    
    print("\n-----\n")
    for i in range(10):
        simulation(3600, 10)