# This program creates a QR code from user input
# Docs to qrcode: https://pypi.org/project/qrcode/

# Make sure you have your virtual environment (venv) activated
# -----------------------------
# Windows: venv/Scripts/activate
# MacOS:   source venv/bin/activate
# -----------------------------

# Practice installing the "qrcode" dependency
# First install the qrcode dependency
# ------------------------
# pip install qrcode[pil]
# ------------------------
# qrcode: This is the main package for generating QR codes.
# [pil]: This specifies an extra dependency group. In this case, pil stands for Pillow, which is a library used for image processing in Python.

# Make sure to add your newly added dependency onto a=your requirements.txt file, so you/other developers can come back and run the program
# -----------------------------
# pip freeze > requirements.txt
# -----------------------------
# This command outputs a list of all installed Python packages in the current environment along with their exact versions. 
# The output is formatted in a way that is compatible with pip install, so you can recreate the same environment elsewhere.

# You can check your current dependencies by doing 
# --------
# pip list
# --------

# Now run the program
# -----------------------------
# python qr_code_generator.py
# -----------------------------

import qrcode

def generate_qr_code(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code object
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code object
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
data_to_encode = input("Enter the data to encode into QR code: ")
file_name = input("Enter the filename to save the QR code image (e.g., 'qrcode.png'): ")
generate_qr_code(data_to_encode, file_name)
