from tkinter import *  
from tkinter import messagebox 

Player1 = 'X'
stop_game = False

def reset_game():
    global states, stop_game, Player1

    Player1 = "X"
    stop_game = False

    for i in range(3):
        for j in range(3):
            states[i][j] = 0
            b[i][j].configure(text = "")

def minimax(states, igrac):

    r = winner(states)
    if r is not None:
        return r
    
    if igrac == "O":
        max_vrijednost = float('-inf')
        for i in range(3):
            for j in range(3):
                if states[i][j] == 0:
                    states[i][j] = "O"
                    trenutna = minimax(states,"X")
                    states[i][j] = 0
                    if trenutna > max_vrijednost:
                        max_vrijednost = trenutna
        return max_vrijednost
    
    else:
        min_vrijednost = float('inf')
        for i in range(3):
            for j in range(3):

                
                if states[i][j] == 0:
                    states[i][j] = "X"
                    trenutna = minimax(states,"O")
                    states[i][j] = 0
                    if trenutna < min_vrijednost:
                        min_vrijednost = trenutna
        return min_vrijednost

def best_move():

    best_score = -999
    best_pos = None

    for i in range(3):
        for j in range(3):

            if states[i][j] == 0:
                states[i][j] = "O"

                score = minimax(states, "X")   

                states[i][j] = 0

                if score > best_score:
                    best_score = score
                    best_pos = (i,j)
                    if best_score == 1: 
                        return best_pos
    return best_pos

def winner(states):
    for r in range(3):
        if states[r][0] == states[r][1] == states[r][2] == "X":
            return -1
        if states[0][r] == states[1][r] == states[2][r] == "X":
            return -1
        if states[r][0] == states[r][1] == states[r][2] == "O":
            return 1
        if states[0][r] == states[1][r] == states[2][r] == "O":
            return 1

    if states[0][0] == states[1][1] == states[2][2] == "X":
        return -1
    if states[0][0] == states[1][1] == states[2][2] == "O":
        return 1

    if states[0][2] == states[1][1] == states[2][0] == "X":
        return -1
    if states[0][2] == states[1][1] == states[2][0] == "O":
        return 1

    for i in range(3):
        for j in range(3):
            if states[i][j] == 0:
                return None

    return 0
    

def clicked(r,c):
    #row, column
    
    global Player1, stop_game

    if stop_game:
        return
    
    if Player1 != "X":
        return
    
    if states[r][c] != 0:
        return

    b[r][c].configure(text = "X")
    states[r][c] = 'X'
    Player1='O'

    if check_if_win():
        return
    
    pos = best_move()
    if pos is None:
        check_if_win()
        return
    
    i, j = pos
    b[i][j].configure(text="O")
    states[i][j] = "O"
    Player1 = "X"

    check_if_win()
   
def check_if_win():
    global stop_game
    r = winner(states)
    if r is None:
        return False

    stop_game = True
    if r == 1:
        messagebox.showinfo("Pobjednik", "O Pobijedio!")
    elif r == -1:
        messagebox.showinfo("Pobjednik", "X Pobijedio!")
    else:
        messagebox.showinfo("Neriješeno", "Neriješeno")

    reset_game()
    return True



root = Tk()
         
root.title("Križić-Kružić")  
root.resizable(0,0)

b = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

states = [
     [0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3): 
                                         
        b[i][j] = Button(
                        height = 4, width = 8, 
                        font = ("Helvetica","20"), 
                        command = lambda r = i, c = j : clicked(r,c))
        b[i][j].grid(row = i, column = j)


mainloop()