**Keystroke Logger with ESC Stop Feature**

This project is a simple keystroke logger built using Python and the pynput library. It captures and logs user keystrokes into a text file (log.txt). Additionally, the program includes a feature to stop logging by pressing the ESC key.

**Features**

Real-time Keystroke Logging: Captures all keystrokes and appends them to a text file.

Escape Key Functionality: Stops the program gracefully when the ESC key is pressed.

Filter Mechanism: Removes unnecessary or special characters (e.g., shift, ctrl) from the log for cleaner output.

**How It Works**

The Listener from the pynput library monitors keyboard input.

All pressed keys are processed by the write_in_file function, which:

Converts the key to a string.

Filters out specific special keys or replaces them with human-readable characters (e.g., space, enter).

If the ESC key is detected, the program stops running.

**Important Notes**

This program is intended for educational purposes. Please ensure you use it ethically and responsibly.

Unauthorized use of this script to record keystrokes is prohibited and may violate laws or regulations.
