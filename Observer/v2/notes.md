Now this is converted to a push model.

Now here cricket_score_board is a publisher and all others will be subscribers. 
Now in future, if we introduce other score boards depending on push from cricket_score_board then it will violate the dependency inversion principle as everytime we will be just increasing dependencyin the cricket_score_board class. 

How can we solve it ?
instead of depending on concrete classes can we try to may be use an interface or abstract class called as subscribers and then depend on a list pf subscribers ?