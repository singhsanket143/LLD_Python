from cricket_score_board import CricketScoreBoard 
import threading
import time

class ProjectedScoreBoard:
    def __init__(self, scoreboard: CricketScoreBoard):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self, runs, wickets, overs):
        # algorithm to calculate projected runs
        # for now i am just assigning it directly
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs
        

    def display(self):
        print(f"Projected Runs: {self.__runs}")
        print(f"Projected Wickets: {self.__wickets}")
        print(f"Projected Overs: {self.__overs}")

# Example Usage
