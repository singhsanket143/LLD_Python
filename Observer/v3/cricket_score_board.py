from typing import List
from subscriber import Subscriber

class CricketScoreBoard:

    def __init__(self):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.__subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber) -> None:
        """Add a subscriber."""
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber) -> None:
        """Remove a subscriber."""
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def updateScore(self, runs: int, wickets: int, overs: float) -> None:
        """Update the score and notify all subscribers."""
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs
        self.__notify()

    def __notify(self) -> None:
        """Notify all subscribers."""
        for subscriber in self.__subscribers:
            subscriber.update(self.__runs, self.__wickets, self.__overs)
