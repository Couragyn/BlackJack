from Gui import *
import random

## Declare all global variables as the minimum values (initialize them)
pics = []
dpics = []
money = 100
bet_placed = 5
hand = []
dealer = []
all_cards = []
deck = []
total = 0
dtotal = 0
numace = 0


class Cards (object):
    """ stores attributes of suit and rank """
    suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    rank = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    def __init__ (self, rank = 0, suit = 0):
        self.rank = rank
        self.suit = suit            
    def __str__ (self):
        return '%s%s%s' % (Cards.rank[self.rank], ' of ', Cards.suit[self.suit])
    def dealt_cards (self, other, g):       #The following cards were provided by Norm's internet connection
        if self.suit == 0:  # Look through hearts
            if self.rank == 1:
                h1 = PhotoImage (file = "cards/AoH.gif")
                other.append (h1)
            elif self.rank == 2:
                h2 = PhotoImage (file = "cards/2oH.gif")
                other.append (h2)
            elif self.rank == 3:
                h3 = PhotoImage (file = "cards/3oH.gif")
                other.append (h3)
            elif self.rank == 4:
                h4 = PhotoImage (file = "cards/4oH.gif")
                other.append (h4)
            elif self.rank == 5:
                h5 = PhotoImage (file = "cards/5oH.gif")
                other.append (h5)
            elif self.rank == 6:
                h6 = PhotoImage (file = "cards/6oH.gif")
                other.append (h6)
            elif self.rank == 7:
                h7 = PhotoImage (file = "cards/7oH.gif")
                other.append (h7)
            elif self.rank == 8:
                h8 = PhotoImage (file = "cards/8oH.gif")
                other.append (h8)
            elif self.rank == 9:
                h9 = PhotoImage (file = "cards/9oH.gif")
                other.append (h9)
            elif self.rank == 10:
                h10 = PhotoImage (file = "cards/10oH.gif")
                other.append (h10)
            elif self.rank == 11:
                h11 = PhotoImage (file = "cards/JoH.gif")
                other.append (h11)
            elif self.rank == 12:
                h12 = PhotoImage (file = "cards/QoH.gif")
                other.append (h12)
            elif self.rank == 13:
                h13 = PhotoImage (file = "cards/KoH.gif")
                other.append (h13)
        elif self.suit == 1:    # Look through diamonds
            if self.rank == 1:
                d1 = PhotoImage (file = "cards/AoD.gif")
                other.append (d1)
            elif self.rank == 2:
                d2 = PhotoImage (file = "cards/2oD.gif")
                other.append (d2)
            elif self.rank == 3:
                d3 = PhotoImage (file = "cards/3oD.gif")
                other.append (d3)
            elif self.rank == 4:
                d4 = PhotoImage (file = "cards/4oD.gif")
                other.append (d4)
            elif self.rank == 5:
                d5 = PhotoImage (file = "cards/5oD.gif")
                other.append (d5)
            elif self.rank == 6:
                d6 = PhotoImage (file = "cards/6oD.gif")
                other.append (d6)
            elif self.rank == 7:
                d7 = PhotoImage (file = "cards/7oD.gif")
                other.append (d7)
            elif self.rank == 8:
                d8 = PhotoImage (file = "cards/8oD.gif")
                other.append (d8)
            elif self.rank == 9:
                d9 = PhotoImage (file = "cards/9oD.gif")
                other.append (d9)
            elif self.rank == 10:
                d10 = PhotoImage (file = "cards/10oD.gif")
                other.append (d10)
            elif self.rank == 11:
                d11 = PhotoImage (file = "cards/JoD.gif")
                other.append (d11)
            elif self.rank == 12:
                d12 = PhotoImage (file = "cards/QoD.gif")
                other.append (d12)
            elif self.rank == 13:
                d13 = PhotoImage (file = "cards/KoD.gif")
                other.append (d13)
        elif self.suit == 2:    # Look through the spades
            if self.rank == 1:
                s1 = PhotoImage (file = "cards/AoS.gif")
                other.append (s1)
            elif self.rank == 2:
                s2 = PhotoImage (file = "cards/2oS.gif")
                other.append (s2)
            elif self.rank == 3:
                s3 = PhotoImage (file = "cards/3oS.gif")
                other.append (s3)
            elif self.rank == 4:
                s4 = PhotoImage (file = "cards/4oS.gif")
                other.append (s4)
            elif self.rank == 5:
                s5 = PhotoImage (file = "cards/5oS.gif")
                other.append (s5)
            elif self.rank == 6:
                s6 = PhotoImage (file = "cards/6oS.gif")
                other.append (s6)
            elif self.rank == 7:
                s7 = PhotoImage (file = "cards/7oS.gif")
                other.append (s7)
            elif self.rank == 8:
                s8 = PhotoImage (file = "cards/8oS.gif")
                other.append (s8)
            elif self.rank == 9:
                s9 = PhotoImage (file = "cards/9oS.gif")
                other.append (s9)
            elif self.rank == 10:
                s10 = PhotoImage (file = "cards/10oS.gif")
                other.append (s10)
            elif self.rank == 11:
                s11 = PhotoImage (file = "cards/JoS.gif")
                other.append (s11)
            elif self.rank == 12:
                s12 = PhotoImage (file = "cards/QoS.gif")
                other.append (s12)
            elif self.rank == 13:
                s13 = PhotoImage (file = "cards/KoS.gif")
                other.append (s13)
        elif self.suit == 3:    # Look through the clubs
            if self.rank == 1:
                c1 = PhotoImage (file = "cards/AoC.gif")
                other.append (c1)
            elif self.rank == 2:
                c2 = PhotoImage (file = "cards/2oC.gif")
                other.append (c2)
            elif self.rank == 3:
                c3 = PhotoImage (file = "cards/3oC.gif")
                other.append (c3)
            elif self.rank == 4:
                c4 = PhotoImage (file = "cards/4oC.gif")
                other.append (c4)
            elif self.rank == 5:
                c5 = PhotoImage (file = "cards/5oC.gif")
                other.append (c5)
            elif self.rank == 6:
                c6 = PhotoImage (file = "cards/6oC.gif")
                other.append (c6)
            elif self.rank == 7:
                c7 = PhotoImage (file = "cards/7oC.gif")
                other.append (c7)
            elif self.rank == 8:
                c8 = PhotoImage (file = "cards/8oC.gif")
                other.append (c8)
            elif self.rank == 9:
                c9 = PhotoImage (file = "cards/9oC.gif")
                other.append (c9)
            elif self.rank == 10:
                c10 = PhotoImage (file = "cards/10oC.gif")
                other.append (c10)
            elif self.rank == 11:
                c11 = PhotoImage (file = "cards/JoC.gif")
                other.append (c11)
            elif self.rank == 12:
                c12 = PhotoImage (file = "cards/QoC.gif")
                other.append (c12)
            elif self.rank == 13:
                c13 = PhotoImage (file = "cards/KoC.gif")
                other.append (c13)
            return other    

def play_again():       ## Starts the game
    global pics, dpics, bet_placed, hand, dealer, all_cards, deck, total, dtotal, numace, money     # Call all the global variables
    replay.config (state = DISABLED)
    bet.config (state = NORMAL)
    howto.config (text = "Type in your wager then click 'Place Bet!' to continue.")     # Change the instruction label
    betlabel.config (text = "Your Wager: $ ____")

    pics = []
    dpics = []
    bet_placed = 5
    hand = []
    dealer = []
    all_cards = []
    deck = []
    total = 0
    dtotal = 0
    numace = 0

    ## Put the cards in the deck
    for r in range (1, 14):
        for s in range (0, 4):
            deck.append (Cards(r, s))
    all_cards = deck      

    money = int(money)
    if money <= 4:      # If you are out of money, display game over and instruct user to restart the game
        howto.config (text = "GAME OVER!")
        betlabel.config (text = "You are out of money. You lose. ")
        moneylabel.config (text = "GAME OVER! Click 'Play Again to reset the game.", fg = 'yellow')
        replay.config (state = NORMAL)
        bet.config (state = DISABLED)
        temp = money
        money = 100
        temp = str(money)
        moneylabel.config (text = "Your Money: $ " + temp)    
    
    return pics, dpics, bet_placed, hand, dealer, all_cards, deck, total, dtotal, numace, money         # Return the values back to the main program


    
def instructions():     # Display Instructions in a new window
    i = Gui()
    i.title ("Instructions")
    text = i.te (height = 42, width = 150, fg = 'darkblue')
    text.insert (END, "                                               ************************************\n")
    text.insert (END, "                                               ****   Black Jack Instructions  ****\n")
    text.insert (END, "                                               ************************************\n\n")
    text.insert (END, "Objective: The objective of the game is beat the dealer. In order to win, you must have the most points\n without going over 21\n\n")
    text.insert (END, "Terms:\n")
    text.insert (END, "         Hit - Get dealt another card\n")
    text.insert (END, "         Stay - Stop with the amount of cards you have\n")
    text.insert (END, "         Bust - To go over 21\n")
    text.insert (END, "\n\n")
    text.insert (END, "First thing you do is place a bet. The minimum accepted is $5. The maximum is limited to how much $ you\n have.\n")
    text.insert (END, "You and the dealer are then given two cards each. You can draw cards with the 'Hit me!' button. If you\n bust you cannot draw more cards.\n")
    text.insert (END, "When you are happy with your cards press the 'Stay!' button. Once this happens it's the dealers turn.\n")
    text.insert (END, "\n\n")
    text.insert (END, "The Rules:\n")
    text.insert (END, "         Whoever is closest to 21 with going over wins.\n")
    text.insert (END, "         If you both have the same amount, the dealer wins.\n")
    text.insert (END, "         If you bust and the dealer doesn't you lose.\n")
    text.insert (END, "         If the dealer busts and you don't, you win.\n")
    text.insert (END, "         If both you and the dealer bust, you win\n")
    text.insert (END, "\n\n")
    text.insert (END, "       Cards Values:")
    text.insert (END, "           2 -> 2 pts\n")
    text.insert (END, "           3 -> 3 pts\n")
    text.insert (END, "           4 -> 4 pts\n")
    text.insert (END, "           5 -> 5 pts\n")
    text.insert (END, "           6 -> 6 pts\n")
    text.insert (END, "           7 -> 7 pts\n")
    text.insert (END, "           8 -> 8 pts\n")
    text.insert (END, "           9 -> 9 pts\n")
    text.insert (END, "          10 -> 10 pts\n")
    text.insert (END, "        Jack -> 10 pts\n")
    text.insert (END, "       Queen -> 10 pts\n")
    text.insert (END, "        King -> 10 pts\n")
    text.insert (END, "         Ace -> 1 pt or 11 pts\n")
    text.insert (END, "\n\n")


def kill():     # Close the entire game
        sys.exit()
########################
        #####################
        ##################
        ##### Matt, this is the function to close the game. This is where you would put the function that brings you to the waiting room.
        #####################
        #################
########################


def place_bet (event = None):
    global pics, dpics, bet_placed, hand, dealer, all_cards, numace, money

    play_again()
    
    x = text.get (0.0, END) # Grab the input in the text box
    x = int(x)
    money = int(money)
    text.delete (0.0, END)      # Delete everything in the text box.

    
    if (x >= 5) and (x <= money):       # Check if your bet is greater the 5$ and less than the amount of money you have (or as much as your money)
        bet.config (state = DISABLED)
        hit.config (state = NORMAL)
        stay.config (state = NORMAL)
        howto.config (text = "Press 'Hit Me!' to gain a card. Press 'Stay!' to compare your hand with the dealer's.")
        bet_placed = str(x)
        betlabel.config (text = 'Your Wager: $' + bet_placed)
            
        dcards = PhotoImage (file = "cards/back.gif")     # Declare the back of a card (for the dealer's cards)

        count = 0           # Keep track of how many times the loop has been looped through
        for i in range (1, 3):      # Deal cards to user and dealer (2 each)
            count += 1      # Increase the number of times the program has looped
            x = random.choice (all_cards)   # Grab a random card
            if x.rank == 1: # Decide how many of the initial cards given was an ace
                numace += 1
            x.dealt_cards(pics, g)      # Search for pictures with the class method
            draw_cards (canvas)         # Draw the cards on the screen
            hand.append (x)             # Add the card dealt to your hand
            all_cards.remove (x)        # Remove that card from the deck

            if count == 2:  # check if its dealing the second card
                y = random.choice (all_cards)       # Grab a random card
                y.dealt_cards(dpics, g)             # Put the picture in the list of dealer's card pictures
                draw_dcards(canvas)                 # Draw the dealer's hand
                dealer.append(y)                    # Add the card to the dealer's hand
                all_cards.remove (y)                # Remove the card from the deck
            else:
                y = random.choice (all_cards)   # Grab a random card
                dpics.append(dcards)    # Put card back in list to print cards on screen
                draw_dcards(canvas)     # Draw the back of a card for the dealer 
                dealer.append(y)        # Add the dealers card to his hand
                all_cards.remove (y)    # Remove that card from the deck

        if numace == 1:     # If there is only 1 ace dealt to you, change it to the rank of 11
            for cards in hand:
                if cards.rank == 1:
                    cards.rank = 14
                    
        return bet_placed

def draw_cards (canvas):        # Draw the cards in your hand
    global pics
    xc = 81

    for pictures in pics:
        canvas.create_image (xc, 475, image = pictures)
        xc += 30
        
def draw_dcards (canvas):       # Draw the dealer's cards
    global dpics
    xc = 81

    for dpictures in dpics:
        canvas.create_image (xc, 80, image = dpictures)
        xc += 30

def hit():      # Hit yourself (gets you another card)
    global pics, hand, all_cards, total 
    total = 0
    
    x = random.choice (all_cards)   # Choose a random card
    x.dealt_cards(pics, g)          # Find the picture for that card
    draw_cards (canvas)             # Draw the card
    
    if x.rank == 1:         # Check if the card dealt is an ace
        for cards in hand:
            if cards.rank > 10:
                cards.rank = 10
            total += cards.rank     # Find the total of your hand
        if total + 11 > 21:     # check if you can take an ace as a high value without busting (+ 21 pts)
            x.rank = 1
            total = 0
        elif total + 11 <= 21:  # If you can take the ace as a high value. change the rank to 11 pts
            x.rank = 14
            total = 0
    hand.append(x)  # add the card to your hand
    all_cards.remove(x)     # remove the cards from the deck

    for cards in hand:
        if cards.rank > 10 and cards.rank < 14:
            cards.rank = 10
        elif cards.rank == 14:
            cards.rank = 11
        total += cards.rank     # Calculate the total
        
    if total > 21:      # If the total is greater than 21 points. Disabled the hit button.
        hit.config (state = DISABLED)
    total = 0
        

            
def compare (total, dtotal):        # This compares you hand to the dealers hand. Here we pick the winner and decide where the money goes.
    global bet_placed, money

    if total > dtotal and total <= 21:   #You beat the dealer without going over, win
        bet_placed = int(bet_placed)
        money = int(money)
        money += bet_placed
        money = str(money)
        howto.config (text = 'Winner! You beat the dealer. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)

    elif dtotal > total and dtotal <= 21:    #The dealer beats you without going over, lose
        bet_placed = int(bet_placed)
        money = int(money)
        money -= bet_placed
        money = str(money)
        howto.config (text = 'Loser! The dealer beat you. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)

    elif total > 21 and dtotal <= 21:     #You bust, lose
        bet_placed = int(bet_placed)
        money = int(money)
        money -= bet_placed
        money = str(money)
        howto.config (text = 'Loser! You busted. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)

    elif dtotal > 21 and total <= 21:     #Dealer busts, win
        bet_placed = int(bet_placed)
        money = int(money)
        money += bet_placed
        money = str(money)
        howto.config (text = 'Winner! The dealer busted. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)
        
    elif total == dtotal:                  #you tie, lose
        bet_placed = int(bet_placed)
        money = int(money)
        money -= bet_placed
        money = str(money)
        howto.config (text = 'Loser! You tied. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)

    elif total > 21 and dtotal > 21:       #both bust, win
        bet_placed = int(bet_placed)
        money = int(money)
        money += bet_placed
        money = str(money)
        howto.config (text = 'Winner! You both busted. Press "Play Again!" to play again.')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)
    
def stay ():
    global dpics, hand, dealer, all_cards, total, dtotal, level         # Call the global variables

    dpics = []      # Reset the pics the dealer has to a blank list
    
    total = 0       # Make sure the total and dealer's total are set to 0
    dtotal = 0

    # Disable the hit button and stay button and activate the play again button
    hit.config (state = DISABLED)       
    stay.config (state = DISABLED)
    replay.config (state = NORMAL)

    for cards in hand:      # Calculate the points in your hand
        if cards.rank > 10 and cards.rank < 14:
            cards.rank = 10
        elif cards.rank == 14:
            cards.rank = 11
        total += cards.rank
    

    switch = 'on'               #Switch to find value of cards
    
    if switch == 'on':
        numd = 0
        dpics = []
        for dcards in dealer:       # Calculate total
            if dcards.rank == 1:
                numd += 1
            dcards.dealt_cards (dpics, g)
            draw_dcards (canvas)
            if dcards.rank > 10:
                dcards.rank = 10
            dtotal += dcards.rank

        if numd == 1:       # Decide whether ace should be high or low.
            for dcards in dealer:
                if dcards.rank == 1:
                    dcards.rank = 14
                    
        while dtotal < 17:
            y = random.choice(all_cards)
            y.dealt_cards (dpics, g)
            draw_dcards (canvas)

            if y.rank > 10:
                y.rank = 10

            dtotal += y.rank
            
            dealer.append (y)
            all_cards.remove (y)


    if len(hand)-1 >= 5 and total <= 21:        # If you have more than 5 cards in your hand and aren't over 21 points, you win. (1x your bet)
        bet_placed = int(bet_placed)
        money = int(money)
        money += bet_placed
        money = str(money)
        howto.config (text = 'WINNER!!!!!! Press "Play Again!" to play again, or "Back To Lobby"')
        betlabel.config (text = 'Your Wager: $ ___')
        moneylabel.config (text = 'Your Money: $ ' + money)
    else:       # Other wise, call the compare function and compare your total to your dealers
        compare (total, dtotal)
    
def destroy ():      # Close the main window
    g.destroy()


g = Gui()   # Make a main "g" window
g.title ("Black Jack")   # Title the window
g.row([1,1,1,25])
mb_file = g.mb (text = "File", borderwidth = 0, bg = 'black', fg = 'red')       # Create a File drop menu
g.mi (mb_file, text = "Return to Arcade", command = kill)

mb_help = g.mb (text = "Help", borderwidth = 0, bg = 'black', fg = 'yellow')    # Create a Help drop menu
g.mi (mb_help, text = "Instructions", command = instructions)   #call the instruction function

g.la ("", bg = 'black')
g.endrow()

canvas = g.ca (width = 600, height = 550, bg = "darkgreen")       # Create a canvas and draw the background of the main game


g.row ([1, 1])
hit = g.bu (text = "Hit Me!", border = 5, command = hit, state = DISABLED)      # Put a Hit Me button
stay = g.bu (text = "Stay!", border = 5, command = stay, state = DISABLED)      # Put a Stay button
replay = g.bu (text = "Play Again!", border = 5, command = play_again, state = DISABLED)    # Put a Play Again button
g.endrow()

g.row ([1,25])
bet = g.bu (text = "Place Bet!", border = 5, command = place_bet)       # Put in a place bet button
text = g.te (height = 1, width = 25, fg = 'darkgreen')                  # Create a text box to type the bet in
text.bind ('<Return>', place_bet)       # Bind the enter key with the place bet function
g.endrow()

howto = g.la ('Enter the amount you wish to bet and click "Place Bet!".', bg = 'black', fg = 'yellow')      # Make a label at the bottom to instruct the user on how to play
betlabel = g.la ('Your Wager: $ ___', bg = 'black', fg = 'green')   # Make a label that displays your wager
money = str(money)
moneylabel = g.la ('Your Money: $ ' + money, bg = 'black', fg = 'green')        # Make a label that displays 

play_again() # Initialize the game

g.mainloop()    # Loop the window
