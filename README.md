
Code python pour prendre un screenshot instantannément

fichier FSS.py lance avec la console      (FastSavingScreenshot)
fichier FSSh.pyw lance sans console       (FastSavingScreenshotHidden)

ALT : Prend un screenshot de l'écran et l'enregistre directement dans le dossier Screens (qui est créé automatiquement dans le dossier de FSS si il n'existe pas)
ALT GR : Ferme l'exécution du code (permet notamment de l'éliminer facilement lorsqu'on exécute un fichier .pyw qui n'a pas de console pour fermer)

Dépendances:
    - Python
    - pyautogui (pip install pyautogui)
    - keyboard (pip install keyboard)
    - Pillow (pip install Pillow)
    
Pour lancer le code directement au démarage sur Windows:
1) Créer un raccourci du fichier .py ou .pyw
2) Appuyer simultanément sur Windows + R
3) Ecrivez "shell:startup" et faites entrer
4) Déplacez le raccourci du fichier .py ou .pyw dans le dossier ouvert grâce à shell:startup
