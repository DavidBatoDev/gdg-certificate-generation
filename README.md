# Certificate Generator

This project is a Python-based certificate generator that automatically adds names to a certificate template and saves them as individual images.

![image](https://github.com/user-attachments/assets/e0f02c39-b5dd-436c-bf2c-3458f00b6d63)

## Features
- Uses a predefined certificate template.
- Adds names dynamically at a specified position.
- Uses a custom font for text rendering.
- Automatically saves the generated certificates in an output folder.

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- [Pillow (PIL)](https://pypi.org/project/Pillow/)
- Google fonts (Inter)

To install Pillow, run:
```bash
pip install pillow
```
## Project Structure
```bash
certificate_generator/
│── certificate_templates/
│   ├── certificate_template.png  # Certificate template image
│── Inter/static/
│   ├── Inter_24pt-SemiBold.ttf   # Font file
│── generated_certificates/       # Output folder (auto-created)
│── generate_certificates.py      # Main script
```

## Usage

1. Place your certificate template inside the `certificate_templates/` folder.
2. Ensure the font file is located in `Inter/static/`.
3. Modify the `names` list in `generate_certificates.py` with the names you want to generate certificates for.
4. Run the script:
```bash
python generate_certificates.py
```
5. Generated certificates will be saved in the `generated_certificates/` folder.

## Usage

1. Place your certificate template inside the `certificate_templates/` folder.
2. Ensure the font file is located in `Inter/static/`.
3. Modify the `names` list in `generate_certificates.py` with the names you want to generate certificates for.
4. Run the script:

```bash
python generate_certificates.py
```
