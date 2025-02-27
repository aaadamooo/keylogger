# Python Keylogger

![Windows](https://img.shields.io/badge/OS-Windows-blue) ![Python](https://img.shields.io/badge/Python-3.x-green)

A background keyboard activity monitor with window context tracking.

## Features
- ⌨️ Keystroke recording with timestamps
- 🖥️ Active window title detection
- 🕶️ Hidden execution (no console visible)
- 🔑 Modifier key state tracking (Shift/Caps Lock)
- 📝 Special key translation (Enter, Tab, Backspace, etc.)
- 💾 Local file logging (`keystrokes.log`)


### Core Components
- `keyboard` module for low-level input capture
- Win32 API for window title detection
- Ctypes for console manipulation



## Ethical Considerations
**⚠️ Important Notice**  
This tool is intended for educational purposes only. Always:
- Obtain proper authorization before use
- Comply with local privacy laws
- Disclose monitoring in appropriate contexts

## Roadmap
- [ ] Network transmission module
- [ ] Data encryption
- [ ] Cross-platform support
- [ ] Configuration file
- [ ] Package as Windows service

## Disclaimer
This project is provided "as-is" for research purposes. The developers assume no responsibility for misuse of this software. Users must ensure proper legal authorization before deploying any form of activity monitoring.