# -*- coding: utf-8 -*-

import time
import threading

class Clock(threading.Thread):
    def __init__(self, aNumberOfHits=-1, aDelayInSeconds=1):
        threading.Thread.__init__(self)
        self.numberOfHits= aNumberOfHits
        self.delayInSeconds= aDelayInSeconds
        self.listeners = []

    def run(self):
        currentHit = 1
        while (self.numberOfHits < 0 or self.numberOfHits >= currentHit):
            currentHit = currentHit + 1
            time.sleep(self.delayInSeconds)
            self.notify()

    def register(self, listener):
        self.listeners.append(listener)

    def notify(self):
        for listener in self.listeners :
            listener()
'''

class MockClockListener() :

    def __init__(self):
        self.numberOfCalls = 0

    def execute(self):
        self.numberOfCalls = self.numberOfCalls + 1
        print(self.numberOfCalls)



mockClockListener = MockClockListener()
clock = Clock()
clock.register(mockClockListener.execute)
clock.start()

time.sleep(5)

print(mockClockListener.numberOfCalls)

'''
