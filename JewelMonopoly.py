import os
import json
import time

def getGameBoard():
    with open(os.getcwd() + "\gameBoard.json", 'r') as f:     
        return json.load(f)

def saveGameBoard(gameBoard):
    with open(os.getcwd() + "\gameBoard.json", 'w') as output:
        json.dump(gameBoard, output)
    output.close()
        

def getPrize(t, gameBoard):
    for idx, row in enumerate(gameBoard['gameBoard']): 
        if row['prize'] == t:
            return row
    return None

def addTicket(prize, index, gameBoard):
    for idx, row in enumerate(gameBoard['gameBoard']): 
        if row['prize'] == prize:
            row['have'][index] += 1

            # is this the winning ticket? (all have are >0)
            return 0 not in row['have']
    return False
    
def addGamePiece(ticket_in):
    # The gamBoard is a list of the prizes and the tickets already have
    gameBoard = getGameBoard()
    result = {'success': False, 'gamepiece': ticket_in }

    if len(ticket_in) < 2:
        result['msg'] = 'The game piece entered is not on the gameBoard. Sorry!'
        return json.dumps(result)


    ticket_prize = ticket_in[:2].lower() # first two Characters
    ticket_num = ticket_in[-1:].lower() # Last character

    prize_row = getPrize(ticket_prize, gameBoard)
    if prize_row == None:
        result['msg'] = 'The game piece entered is not on the gameBoard. Sorry!'
        return json.dumps(result)

    ticket_index = None
    ticket_index = prize_row['tickets'].index(ticket_num)

    prize = getPrize(ticket_prize, gameBoard)
    if prize == None:
        result['msg']=  "Umm, I can't find a prize for " + ticket_prize
        return json.dumps(result)
                
    try:
        ticket_index = None
        ticket_index = prize['tickets'].index(ticket_num)
    except ValueError:
        result['msg'] = "Umm, that ticket number isn't in the game Board?"
        return json.dumps(result)


    # Determine if we have a winner!
    Winner = "You would win "+ prize['win'] + "\n"

    # Do we need that ticket for the board?
    ticket_count = prize['have'][ticket_index]
    if  ticket_count > 0:
        Winner = Winner + "Nice try, we already have that seen that ticket " + str(ticket_count) + " times."
    else:
        Winner = Winner + ("Oh, we need that one! ")
        
    # Add ticket to the tickets we have 
    if addTicket(prize['prize'],ticket_index, gameBoard):
        Winner = Winner + "\n WINNER !!! WooHoo! We have all of the tickets for " + prize['prize']
        Winner = Winner + ("\n We get a " + prize['win'])
        result['prize'] = prize['win']

    # Write the ticket to a log of tickets
    filename = os.getcwd() + "\monopoly_tickets.txt"
    target = open(filename, 'a')
    target.write("\n" + ticket_prize + ticket_num + ',' + str(time.time()))  # CHanged this to have the newline character before the ticket number

    saveGameBoard(gameBoard)
    result['success'] = True
    result['msg'] = Winner
    return json.dumps(result)
