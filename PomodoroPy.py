import time
import platform
import winsound
import tkinter as tk
from threading import Thread

def beep():
    """Produce sound when the countdown finishes."""
    if platform.system() == "Windows":
        duration = 500  # milliseconds
        freq = 1000  # Hz
        winsound.Beep(freq, duration)
    else:
        print('\a', end='', flush=True)  # For Linux/MacOS, try terminal bell

def countdown(minutes, label, label_var):
    seconds = minutes * 60
    while seconds > 0:
        minutes_left = seconds // 60
        seconds_left = seconds % 60
        time_str = f"{minutes_left:02d}:{seconds_left:02d}"
        label_var.set(time_str)
        time.sleep(1)
        seconds -= 1
    label_var.set("Time's ready!")
    beep()

def start_timer(minutes, label_var):
    """Start the countdown"""
    Thread(target=countdown, args=(minutes, "Pomodoro", label_var)).start()

def main():
     #main window
    root = tk.Tk()
    root.title("Pomodoro Timer")

    # label to display the countdown
    label_var = tk.StringVar()
    label_var.set("10:00")  # Default time
    label = tk.Label(root, textvariable=label_var, font=("Helvetica", 48))
    label.pack(pady=20)

    # start button
    start_button = tk.Button(root, text="Start Pomodoro!", command=lambda: start_timer(1, label_var))
    start_button.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
