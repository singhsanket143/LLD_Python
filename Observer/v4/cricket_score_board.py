from typing import List
from subscriber import Subscriber
from publisher import Publisher

class CricketScoreBoard(Publisher):

    def __init__(self):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.__subscribers: List[Subscriber] = []

    def register(self, subscriber: Subscriber) -> None:
        self.__subscribers.append(subscriber)

    def deregister(self, subscriber: Subscriber) -> None:
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def notify(self) -> None:
        for subscriber in self.__subscribers:
            subscriber.update(self.__runs, self.__wickets, self.__overs)

    def updateScore(self, runs: int, wickets: int, overs: float) -> None:
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs
        self.notify()
