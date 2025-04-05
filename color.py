import random
import tkinter as tk

# List of colors
colors_name = ['red', 'white', 'yellow', 'pink', 'blue', 'black', 'brown', 'purple', 'green', 'cyan']
score = 0
time_left = 60

# Function to start the game
def startGame(event):
    global time_left
    if time_left == 60:
        countdown()  # Start the timer
    changecolor()  # Change color immediately when game starts

# Function to change color and check input
def changecolor():
    global score, time_left

    if time_left > 0:
        e.focus_set()
        if e.get().lower() == label.cget("fg").lower():  # Check entered text against color name
            score += 1
        
        e.delete(0, tk.END)  # Clear entry field
        random.shuffle(colors_name)  # Shuffle colors

        label.config(fg=colors_name[1], text=colors_name[0])  # Change displayed text and color
        scoreLabel.config(text="Score: " + str(score))  # Update score display

# Function for countdown timer
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timeLabel.config(text='Time Left: ' + str(time_left))
        root.after(1000, countdown)  # Call countdown every 1 second

# Create main window
root = tk.Tk()
root.title("Color Guessing Game")
root.geometry("600x400")

# Instructions Label
instruct = tk.Label(root, text="Type the COLOR of the word!", font=("sans-serif", 20))
instruct.pack()

# Score Label
scoreLabel = tk.Label(root, text="Press Enter to start", font=("sans-serif", 18))
scoreLabel.pack()

# Time Left Label
timeLabel = tk.Label(root, text="Time Left: " + str(time_left), font=("sans-serif", 16))
timeLabel.pack()

# Main Label for color words
label = tk.Label(root, font=("sans-serif", 40))
label.pack()

# Entry Field
e = tk.Entry(root)
e.pack()
e.focus_set()

# Bind Enter key to start game
root.bind('<Return>', startGame)

# Run the game loop
root.mainloop()
