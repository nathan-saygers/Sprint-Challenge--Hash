#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Create new dictionary
    tickets_dict = {}
    route = []
    # loop through array
    for tic in tickets:
        # set source as key and dest as value for each ticket
        tickets_dict[tic.source] = tic.destination
    # from new dictionary, while destination != None,
    # push source to route array and make destination new source
    current = tickets_dict["NONE"]
    route.append(current)
    while tickets_dict[current] != "NONE":
        current = tickets_dict[current]
        route.append(current)
    route.append("NONE")

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]


reconstruct_trip(tickets, 3)
