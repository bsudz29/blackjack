import streamlit as st
import engine
st.set_page_config(page_title="Blackjack", layout="wide") #layout is needed to for game to span entire chrome tab

c1 = st.container(border=True)
c1.title("Welcome to the Blackjack game!")

if c1.button("Start Game"):
    engine.gameengine(c1)
    