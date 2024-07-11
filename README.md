# Clipboard Saver

## Overview

Clipboard Saver is a simple Python application that monitors your clipboard and saves copied text. It features a GUI built with Tkinter, allowing users to view, copy, and clear saved clipboard texts. The application also supports keyboard shortcuts for convenience.

## Features

1. **Clipboard Monitoring**: Automatically detects and saves copied text.
2. **Text Display**: Displays saved texts in a scrollable textbox.
3. **Copy All**: Copies all saved texts to the clipboard.
4. **Copy Selected**: Copies only the selected text from the textbox to the clipboard.
5. **Clear All**: Clears all saved texts and the clipboard.
6. **Keyboard Shortcuts**: 
   - `Ctrl+G` to show the application.
   - `Esc` to exit the application.

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required packages using `pip`:

```bash
   pip install pyperclip keyboard
```
## Usage
Run the application as a root using the following command:

```bash
sudo python clipboard_saver.py
```

   - Press Ctrl+G to show the Clipboard Saver window.
   - Use the buttons in the GUI to manage the saved texts.