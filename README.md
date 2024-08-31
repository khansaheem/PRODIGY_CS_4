Simple Keylogger 📄 Project Overview This project is a Simple Keylogger built using Python and the Pynput library.
The keylogger captures all keystrokes pressed by the user and logs them into a text file. It handles special keys such as spaces,
enters, backspaces, and more, ensuring that all types of inputs are recorded correctly.

🛠️ Tech Stack Language: Python Library: Pynput ⚙️ How It Works The keylogger operates by
listening for keyboard events and writing the corresponding keys to a log file (keylog.txt).

The program handles:
Alphanumeric characters: Captured and logged directly. 
Special keys: Like spaces, enters, and backspaces, which are logged with specific markers (e.g., [BACKSPACE], [ENTER]).
Escape key: Stops the keylogger when pressed.
🔍 Key Features Event Listener: Uses Pynput’s Listener to monitor key presses and releases.
Log Handling: Efficiently writes to the log file, appending each keypress. Cross-Platform: Works on Windows, macOS, and Linux.
