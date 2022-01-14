# Tic Tac Toe API - Python + Flask
### What is this?
A tic tac toe API written on Python + Flask that plays against you. *For the win.*

---
### How to run it?
1. Create a virtual environment

    `python3 -m venv venv/`

2. Activate it

    `source venv/bin/activate`

3. Install flask and gunicorn

    `pip3 install flask gunicorn`

4. Run the script

    `python3 tictactoe.py`

---
### What are the rules?
https://docs.google.com/document/d/1Oynv2mqS74Skvp-UPFOtV7JZH-kcVxMQ4w8ng0DqcgE/edit?usp=sharing

---
### How to play it?
You can send a `curl` request to get with your current board and the script will return a new board to you.

The bot always plays `o` and the human always plays `x`.

So, for instance, if you send the board `curl http://127.0.0.1:5000/?board=oo+xx++++`, that means it's the bot's turn and it will play for the win, returning you the value `oooxx++++` as a result, and therefore winning.

To see the console logs with the visual 3x3 board and detailed messages, please check the terminal on your virtual environment.

You can either send a `curl` request from the terminal or directly type the board on your browser, such as `http://127.0.0.1:5000/?board=oo+xx++++`.

---
### What's next?
The bot is not invincible, since I wrote the script using traditional strategies (https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy) and not minimax.

So feel free to contribute and improve the algorithm so we can a *nearly-invincible* bot!