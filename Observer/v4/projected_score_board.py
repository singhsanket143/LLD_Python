from typing import List
from subscriber import Subscriber
from publisher import Publisher

class ProjectedScoreBoard(Subscriber):

    def __init__(self):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.publishers: List[Publisher] = []

    def update(self, runs: int, wickets: int, overs: float) -> None:
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs

    def subscribe_to(self, publisher: Publisher) -> None:
        if publisher not in self.publishers:
            publisher.register(self)
            self.publishers.append(publisher)

    def unsubscribe_from(self, publisher: Publisher) -> None:
        if publisher in self.publishers:
            publisher.deregister(self)
            self.publishers.remove(publisher)

    def display(self):
        print(f"Projected Runs: {self.__runs}")
        print(f"Projected Wickets: {self.__wickets}")
        print(f"Projected Overs: {self.__overs}")
