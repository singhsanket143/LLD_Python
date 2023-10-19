from cricket_score_board import CricketScoreBoard 
import threading
import time

class ProjectedScoreBoard:
    def __init__(self, scoreboard: CricketScoreBoard):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.cricket_scoreboard = scoreboard
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        is_updated = False
        while True:
            if self.cricket_scoreboard.getRuns() != self.__runs:
                self.__runs = self.cricket_scoreboard.getRuns()
                is_updated = True
            if self.cricket_scoreboard.getWickets() != self.__wickets:
                self.__wickets = self.cricket_scoreboard.getWickets()
                is_updated = True
            if self.cricket_scoreboard.getOvers() != self.__overs:
                self.__overs = self.cricket_scoreboard.getOvers()
                is_updated = True

            if(is_updated): 
                # Execute algorithm to calculate projected score
                print("Some logic executed")
                
            time.sleep(0.1)  # Check every 100 milliseconds

    def display(self):
        print(f"Projected Runs: {self.__runs}")
        print(f"Projected Wickets: {self.__wickets}")
        print(f"Projected Overs: {self.__overs}")

# Example Usage
csb = CricketScoreBoard()
psb = ProjectedScoreBoard(csb)
time.sleep(1)  # Give some time for the thread to start
csb.updateScore(100, 2, 10.2)
time.sleep(1)  # Wait a bit to ensure the ProjectedScoreBoard had time to update
psb.display()