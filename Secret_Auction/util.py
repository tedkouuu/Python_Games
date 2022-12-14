from os import system, name


def clear():
    """ Clears the terminal after is has been called"""
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def find_highest_bidder(bidding_record):
    """ Returns the person with the biggest bid"""
    max_bid = 0
    person_name = ''
    for bidder in bidding_record:
        if bidding_record[bidder] > max_bid:
            max_bid = bidding_record[bidder]
            person_name = bidder

    return [person_name, max_bid]
