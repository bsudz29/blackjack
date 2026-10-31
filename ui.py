import streamlit as st
import cards
import engine

st.set_page_config(page_title="Blackjack", layout="wide") #layout is needed to for game to span entire chrome tab

st.title('Blackjack')
ui = st.container(border=True, horizontal_alignment='center')
hc, sc = ui.columns(2)
hc.button('Hit', width='stretch')
sc.button('Stand', width='stretch')
c1 = st.container()


if c1.button("Start Game"):
    cards.Card.chosen = set() #resets the tracker of chosen cards 
    engine.gameengine(c1)
    