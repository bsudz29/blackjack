import cards
import images
import streamlit as st
import time

def game(container): # if want to print in a container, pass one thorugh
    #game logic
    playerHand = st.session_state['playerHand']
    playerTotal = st.session_state['playerTotal']     
    dealerHand = st.session_state['dealerHand'] 
    dealerTotal = st.session_state['dealerTotal']
    dh = container.container(border=True, horizontal_alignment='center', horizontal=True, height=240)
    dh.subheader('Dealer Hand', width='content')
    dsubc = dh.container(horizontal_alignment='center', horizontal=True)
    if st.session_state['dealercard2image'] == "images/card_back.png":
        dsubc.image(dealerHand[0].getImage)
        dsubc.image(st.session_state['dealercard2image'])
    else:
        for card in dealerHand:
            dsubc.image(card.getImage)
        
    ph = container.container(border=True, horizontal_alignment='center', horizontal=True, height=240)
    ph.subheader('Player Hand', width='content')
    psubc = ph.container(horizontal_alignment='center', horizontal=True)
    for card in playerHand:
        psubc.image(card.getImage)

def hit():
    st.session_state['playerHand'].append(cards.Card())
    st.session_state['playerTotal'] = sum([card.value for card in st.session_state['playerHand']])
    st.write(st.session_state['playerHand'])
    determine_winner()
    
def stand():
    st.session_state['dealercard2image'] = st.session_state['dealerHand'][1].getImage
    while st.session_state['dealerTotal'] < 17:
        st.session_state['dealerHand'].append(cards.Card())
        st.session_state['dealerTotal'] = sum([card.value for card in st.session_state['dealerHand']])
    determine_winner()

def determine_winner():
    pt = st.session_state['playerTotal']
    dt = st.session_state['dealerTotal']
    winner = st.session_state['winner']
    if pt > 21:
        st.session_state['winner'] = "You busted. Dealer wins."
    elif dt > 21:
        st.session_state['winner'] = "Dealer busted. You win!"
    elif pt == 21:
        st.session_state['winner'] = "Blackjack! You win!"
    elif dt == 21:
        st.session_state['winner'] = "Dealer has Blackjack. Dealer wins."
    elif pt > dt:
        st.session_state['winner'] = "You win!"
    elif dt > pt:
        st.session_state['winner'] = "Dealer wins."
    
def reset_game():
    st.session_state.started = False
    st.session_state.winner = False
    st.session_state.playerHand = [cards.Card(), cards.Card()]
    st.session_state.dealerHand = [cards.Card(), cards.Card()]
    st.session_state.playerTotal = sum([card.value for card in st.session_state.playerHand])
    st.session_state.dealerTotal = sum([card.value for card in st.session_state.dealerHand])
    st.session_state['dealercard2image'] = "images/card_back.png"

#ui setup
if __name__ == "__main__":
    st.set_page_config(page_title="Blackjack", layout="wide")
    # CSS code is generated from AI as I do not know CSS. Prompt was "How can I have the heights of images be restrictive upon the container's height"
    st.html("""
            <style>
                [data-testid="stVerticalBlock"][data-testid="stVerticalBlock"] img {
                    max-height: 210px;
                    width: auto;
                    object-fit: contain;
                }
            </style>
            """)
    st.title("Blackjack", text_alignment="center")

    #define states to be tracked
    if "started" not in st.session_state:
        st.session_state.started = False
    if "winner" not in st.session_state:
        st.session_state.winner = False
    if "playerHand" not in st.session_state:
        st.session_state.playerHand = [cards.Card(), cards.Card()]
    if "dealerHand" not in st.session_state:
        st.session_state.dealerHand = [cards.Card(), cards.Card()]
    if "playerTotal" not in st.session_state:
        st.session_state.playerTotal = sum([card.value for card in st.session_state.playerHand])
    if "dealerTotal" not in st.session_state:
        st.session_state.dealerTotal = sum([card.value for card in st.session_state.dealerHand])
    if "dealercard2image" not in st.session_state:
        st.session_state['dealercard2image'] = "images/card_back.png"
   
    def disable():
        st.session_state.started = True

    #starting page -- when game hasn't been started (when the state; "started" isn't true)
    if not st.session_state.started and not st.session_state.winner:
        sc1 = st.container(border=True, width='stretch', horizontal_alignment='center')
        sc1.button("Start Game", disabled=st.session_state.started, on_click=disable)
        sc1.subheader("Rules of the Game", width='content')
        sc1.write("At the start you are given 2 cards and the dealer is given 2 cards, where one is face up and the other is face down")
        sc1.write("You can choose to hit or stand after your initial hand is dealt.")
        sc1.write("The goal is to get a hand value as close to 21 as possible without exceeding it.")
        sc1.write("The dealer must hit until their hand value is 17 or higher.")
        sc1.write("If both the player and dealer bust, the player loses.")
        sc1.write("If the player busts, the player loses immediately.")
        sc1.write("If the dealer busts, the player wins.")
        sc1.write("If neither busts, the hand closest to 21 wins.")
        sc1.write("A natural blackjack (an Ace and a 10-value card) pays out at 3:2.")
        sc1.write("The game ends when the player stands or busts, and the dealer completes their hand according to the rules.")
        sc1.write("Press 'Start Game' to begin. Good luck!")
    elif st.session_state.winner:
        con = st.container(border=True, width='stretch', horizontal_alignment='center')
        con.subheader(st.session_state.winner, text_alignment='center')
        con.button("Play Again", on_click=reset_game, width='content')

    else:
        #when the game has started

        c1, c2 = st.columns([0.2, 0.8])
        c1.subheader("Controls", text_alignment='center')
        @st.fragment
        def controls():
            if c1.button("Hit", width='stretch', disabled=len(st.session_state.dealerHand) != 2 or st.session_state['winner']):
                hit()
                st.rerun()
            if c1.button("Stand", width='stretch', disabled=st.session_state['winner']):
                stand()
                st.rerun()
        controls()
        gsc1 = c2.container(border=True, width='stretch', height=540, horizontal_alignment='center', vertical_alignment='center')
        game(gsc1)



