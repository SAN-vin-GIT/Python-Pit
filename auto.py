import pyautogui
import time

# Define message and delay
message = "Your Message Here"
delay = 0.5  # Time between each message
running = True  # Flag to control the loop

def start_typing():
    global running
    time.sleep(5)  # Gives you 5 seconds to switch to the chat window

    while running:
        pyautogui.typewrite(message)  # Types the message
        pyautogui.press("enter")  # Press Enter to send
        time.sleep(delay)  # Wait before sending the next message

def stop_typing():
    global running
    running = False

# Start the typing function
try:
    start_typing()
except KeyboardInterrupt:
    stop_typing()
    print("Stopped by user.")


# Open WhatsApp Web, Messenger, or any chat app.
# Click on the chat where you want to send messages.
# Run the script.
# You have 5 seconds to switch to the chat window before the script starts typing.
# To stop, press Ctrl + C in the terminal.
