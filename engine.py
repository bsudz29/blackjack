import cards
import streamlit as st

def gameengine(container=st): # if want to print in a container, pass one thorugh
    dealerhalf = container.container(border=True)
    d1 = cards.Card()
    d2 = cards.Card()
    dc1, dc2 = dealerhalf.columns(2)
    dc1.image(d1.getImage)
    dc2.image(d2.getImage)


    playerhalf = container.container(border=True)
    p1 = cards.Card()
    p2 = cards.Card()
    pc1, pc2 = playerhalf.columns(2)
    pc1.image(p1.getImage)
    pc2.image(p2.getImage)

def hit():
    pass
def stand():
    pass