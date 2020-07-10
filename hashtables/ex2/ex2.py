#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    mapping = {ticket.source: ticket.destination for ticket in tickets}
    prev_source = 'NONE'
    
    for i in range(length):
        route.append(mapping[prev_source])
        prev_source = mapping[prev_source]



    return route