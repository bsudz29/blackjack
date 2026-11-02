import cards
import images
import streamlit as st

#! css files can be used to manipulate the images and the containers for no scrolling

def game(container): # if want to print in a container, pass one thorugh
    #game logic
    playerHand = st.session_state['playerHand']
    playerTotal = st.session_state['playerTotal']
    dealerHand = st.session_state['dealerHand'] 
    dealerTotal = st.session_state['dealerTotal']

    #game start       
    playerHand.append(cards.Card())
    playerHand.append(cards.Card())
    dealerHand.append(cards.Card())
    dealerHand.append(cards.Card())

    #for debugging and testing
    #container.write(cards.Card.chosen)
    #container.write(playerHand[0].value)
    #container.write(playerHand[1].value)
    
    dh = container.container(border=True, horizontal_alignment='center', horizontal=True)
    dh.subheader('Dealer Hand', width='content')
    dsubc = dh.container(horizontal_alignment='center', horizontal=True)
    dsubc.image(playerHand[0].getImage)
    dsubc.image(playerHand[1].getImage)
def hit():
    pass

def stand():
    pass

#ui setup
if __name__ == "__main__":
    st.set_page_config(page_title="Blackjack", layout="wide")
    
    st.title("Blackjack", text_alignment="center")

    #define states to be tracked
    if "started" not in st.session_state:
        st.session_state.started = False
    if "playerHand" not in st.session_state:
        st.session_state.playerHand = []
    if "dealerHand" not in st.session_state:
        st.session_state.dealerHand = []
    if "playerTotal" not in st.session_state:
        st.session_state.playerTotal = 0
    if "dealerTotal" not in st.session_state:
        st.session_state.dealerTotal = 0
    if "dealercard2image" not in st.session_state:
        st.session_state['dealercard2image'] = "images/card_back.png"
   
    def disable():
        st.session_state.started = True

    #starting page -- when game hasn't been started (when the state; "started" isn't true)
    if not st.session_state.started:
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
    else:
        #when the game has started

        c1, c2 = st.columns([0.2, 0.8])
        c1.subheader("Controls", text_alignment='center')
        @st.fragment
        def controls():
            c1.button("Hit", width='stretch', on_click=hit)
            c1.button("Stand", width='stretch', on_click=stand)
        controls()
        gsc1 = c2.container(border=True, width='stretch', height=500, horizontal_alignment='center')
        game(gsc1)



