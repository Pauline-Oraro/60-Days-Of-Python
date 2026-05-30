# QR Code Generator

A simple desktop GUI application for generating and saving QR codes from text or URLs, built with Python.

## Features

- Enter any text or URL to generate a QR code instantly
- Save generated QR codes as PNG images to your local machine
- Minimal, easy-to-use graphical interface

## Requirements

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) library
- [tkinter](https://docs.python.org/3/library/tkinter.html) (usually bundled with Python)

## Installation

1. **Clone or download** this repository.

2. **Install dependencies:**

   ```bash
   pip install qrcode[pil]
   ```

   > `tkinter` comes pre-installed with most Python distributions. If it's missing, install it via your system's package manager (e.g., `sudo apt install python3-tk` on Ubuntu).

## Usage

1. Run the application:

   ```bash
   python qr_generator.py
   ```

2. Enter any **text or URL** in the input field.

3. Click **"Generate QR Code"** to create the QR code.

4. Click **"Save QR Code"** to save it as a `.png` file to a location of your choice.

## Project Structure

```
.
└── qr_generator.py   # Main application file
```

## How It Works

The app is built around a single `QRCodeGenerator` class that manages the GUI and logic:

| Method | Description |
|---|---|
| `__init__` | Sets up the tkinter window, labels, input field, and buttons |
| `generate_qr_code` | Reads input and uses the `qrcode` library to generate a QR code image |
| `save_qr_code` | Opens a file dialog to let the user save the QR code as a PNG |

The **Save** button is disabled until a QR code has been successfully generated, preventing empty saves.

## License

This project is open source and free to use.
