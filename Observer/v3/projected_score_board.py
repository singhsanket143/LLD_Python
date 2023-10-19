from subscriber import Subscriber

class ProjectedScoreBoard(Subscriber):

    def __init__(self):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0

    def update(self, runs: int, wickets: int, overs: float) -> None:
        """Update the projected scoreboard."""
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs
        # additional logic where we can may be average out a bunch

    def display(self):
        print(f"Projected Runs: {self.__runs}")
        print(f"Projected Wickets: {self.__wickets}")
        print(f"Projected Overs: {self.__overs}")
