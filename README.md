# QR Code Generator

This is a simple Python application built using Tkinter for generating QR codes. The application allows users to enter a URL, choose a color for the QR code, generate the QR code, save it as a PNG file, copy the URL to clipboard, reset the input, and exit the application.

![GUI](https://github.com/mueezbaig/QR-Code-Generator/blob/main/GUI.png
)
## Features of QR Codes in Today's World

QR (Quick Response) codes have become ubiquitous in today's digital landscape. They offer various functionalities and benefits, including:

1. **Contactless Transactions**: QR codes enable contactless payments, ticketing, and transactions, reducing physical contact and enhancing convenience.

2. **Information Sharing**: They efficiently store a large amount of data such as URLs, text, contact information, Wi-Fi credentials, etc., allowing quick access to information with a simple scan.

3. **Marketing and Advertising**: QR codes are used extensively in marketing campaigns, product packaging, and advertising materials to provide additional information, promotional offers, and interactive experiences to consumers.

4. **Authentication and Security**: QR codes can be used for authentication purposes, secure access control, and verification processes, enhancing security measures in various industries.

5. **Offline to Online Engagement**: QR codes bridge the gap between offline and online experiences, allowing seamless transition from physical media to digital content, websites, or applications.

## Functionality Overview

### 1. Enter URL:

![Enter URL](https://github.com/mueezbaig/QR-Code-Generator/blob/main/Enter%20Url.png)

Allows users to input a url for the QR code. For which the the qr code is generated.

### 2. Choose Color

![Choose Color](https://github.com/mueezbaig/QR-Code-Generator/blob/main/Choosing%20color.png)

Allows users to pick a custom color for the QR code. The selected color is applied to the QR code before generation.

### 3. Generate QR Code

![Generate QR Code](https://github.com/mueezbaig/QR-Code-Generator/blob/main/generate%20qr%20code.png)

Allows users to input a URL and generate a corresponding QR code. It provides visual feedback of the generated QR code on the interface.

The Generated QR CODE:

![Generated QR Code](https://github.com/mueezbaig/QR-Code-Generator/blob/main/qr.png)

### 4. Copy URL

![Copy URL](https://github.com/mueezbaig/QR-Code-Generator/blob/main/url%20copeid%20to%20clipboard.png)

Copies the entered URL to the clipboard, facilitating easy sharing or pasting of the URL into other applications or platforms.

### 5. Save QR Code

![Save QR Code](https://github.com/mueezbaig/QR-Code-Generator/blob/main/save.png
)

Enables users to save the generated QR code as a PNG file to their local system. Users can specify the file name and location for saving.

---

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python (version 3.9 or above versions )
- Tkinter library (usually included with Python)

## Required Packages

Before running the application, ensure you have the following Python packages installed:

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyQRCode](https://pypi.org/project/PyQRCode/)
- [Pillow (Python Imaging Library)](https://pypi.org/project/Pillow/)

You can install these packages using pip:

```bash
pip install tkinter
pip install pyqrcode
pip install pillow
```

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/mueezbaig/QR-Code-Generator.git

```

2. Navigate to the project directory:
```bash
cd main.py
```

3. Run the application:
```bash
python3 main.py
```

This application provides a simple and user-friendly way to generate QR codes with customizable features, catering to various use cases and requirements in today's digital ecosystem.
