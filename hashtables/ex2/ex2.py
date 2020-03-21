#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for t in tickets:
        hash_table_insert(ht, t.source, t)

    next_t = 'NONE'
    for i in range(len(route)):
        ticket = hash_table_retrieve(ht, next_t)
        if ticket.destination != 'NONE':
            route[i] = ticket.destination
            next_t = ticket.destination

    route.pop()

    return route
