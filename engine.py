import cards
import images
import streamlit as st

#! css files can be used to manipulate the images and the containers for no scrolling

def gameengine(container=st): # if want to print in a container, pass one thorugh
    dealertotal = 0
    playertotal = 0
    
    dealerhalf = container.container(border=True)
    d1 = cards.Card()
    d2 = cards.Card()
    dealertotal += d1.value + d2.value

    dealerhalf.title(f'Dealer Value: {dealertotal}')
    dc1, dc2 = dealerhalf.columns(2)
    dc1.image(d1.getImage)
    dc2.image("images/card_back.png")


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