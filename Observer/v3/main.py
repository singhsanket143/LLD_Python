from cricket_score_board import CricketScoreBoard
from projected_score_board import ProjectedScoreBoard

csb = CricketScoreBoard()
psb = ProjectedScoreBoard()
csb.add_subscriber(psb)

csb.updateScore(100, 2, 10.2)
psb.display()
