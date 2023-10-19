do u think that the add_subscribe and ubsubcribe method should be callable from projected_score_board.py ?

i want that subscriber should be having control on what publisher it want to subscribe to, as there can be multiple publishers also

If subscribers need the flexibility to choose which publishers they want to subscribe or unsubscribe from, you can shift the responsibility to the subscribers. In this scenario, instead of the publisher managing its subscribers, each subscriber manages its own list of publishers.

can we introduce an interface publisher and then our subscribers will be depending on a list of publishers may be ?