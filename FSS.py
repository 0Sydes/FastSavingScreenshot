# -*- coding: utf-8 -*-
"""
Outil permettant de prendre un screenshot instantannément
Dépendances:
    - Python
    - pyautogui (pip install pyautogui)
    - keyboard (pip install keyboard)
    - Pillow (pip install Pillow)
"""

import pyautogui 
import keyboard 
import datetime
import os
import time

width, height = pyautogui.size()
if not os.path.exists("./Screens"):
    os.makedirs("./Screens")
    print("Création d'un dossier Screens...")

print("Faites ALT pour prendre un screenshot instantanné et ALT GR pour fermer l'exécuteur.")
while True:
    key = keyboard.read_key()
    # Appuyer sur alt pour prendre un screenshot
    if key == "alt":
        im1 = pyautogui.screenshot(region=(0,0,width,height))
        im1.save(r"./Screens/" + datetime.datetime.now().strftime("%d %b %Y - %Hh, %Mm, %Ss (%fms)") + ".png")
        print("Screenshot effectué et sauvegardé.")
    # Appuyer sur alt gr pour fermer l'exécuteur
    if key == "alt gr":
        print("Fermeture...")
        quit()
    time.sleep(0.1)