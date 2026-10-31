import streamlit as st
import engine
c1 = st.container(border=True)
c1.title("Welcome to the Blackjack game!")

if c1.button("Start Game"):
    engine.gameengine()