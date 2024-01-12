# OCR Tool

This is a simple Optical Character Recognition (OCR) tool built with Python. It uses the `pytesseract` library to extract text from images. The tool provides a simple GUI using `tkinter` for user interaction.

## Features

- Select an image file (supports .png, .jpg, .jpeg formats)
- Display the selected image in the application
- Extract text from the selected image
- Display the extracted text in the application

## Dependencies

- Python 3
- tkinter
- PIL (Pillow)
- pytesseract

## Installation

1. Install Python 3 and pip if not already installed.
2. Clone this repository.
3. Navigate to the cloned repository.
4. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:

```bash
python OCR.py
```

2. Click on the "Select Image" button to choose an image.
3. The selected image will be displayed and the extracted text will appear in the text box.

## Note

This tool uses Tesseract OCR which needs to be installed and the path to the `tesseract.exe` should be correctly specified in the script. In this script, it is specified as `C:\Program Files\Tesseract-OCR\tesseract.exe`. Please update this path if your Tesseract OCR installation is in a different location.