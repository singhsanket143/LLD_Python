from cricket_score_board import CricketScoreBoard
from projected_score_board import ProjectedScoreBoard

if __name__ == "__main__":
    csb = CricketScoreBoard()
    psb = ProjectedScoreBoard()

    psb.subscribe_to(csb)
    csb.updateScore(100, 2, 10.2)
    psb.display()

    csb.updateScore(150, 3, 20.3)
    psb.display()

    psb.unsubscribe_from(csb)
    csb.updateScore(200, 5, 30.0)
    # This won't reflect the latest score as we unsubscribed.
    psb.display()
