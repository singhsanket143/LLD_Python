from projected_score_board import ProjectedScoreBoard
class CricketScoreBoard:
    def __init__(self, projected_score_board: ProjectedScoreBoard):
        self.__runs = 0
        self.__wickets = 0
        self.__overs = 0
        self.__projected_score_board = projected_score_board

    def updateScore(self, runs: int, wickets: int, overs: float) -> None:
        """Update the score on the scoreboard. Some api automatically calls this api """
        self.__runs = runs
        self.__wickets = wickets
        self.__overs = overs
        self.__projected_score_board.update(runs, wickets, overs)

    def getRuns(self) -> int:
        """Return the current runs."""
        return self.__runs

    def getWickets(self) -> int:
        """Return the current number of wickets."""
        return self.__wickets

    def getOvers(self) -> float:
        """Return the current number of overs."""
        return self.__overs

# Usage
scoreboard = CricketScoreBoard()
scoreboard.updateScore(150, 3, 25.2)
print(f"Runs: {scoreboard.getRuns()}")
print(f"Wickets: {scoreboard.getWickets()}")
print(f"Overs: {scoreboard.getOvers()}")
