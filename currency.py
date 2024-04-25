import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageEnhance

# Create a Tkinter window
root = tk.Tk()
root.title("Currency Detection")


bg_image = Image.open("C:/Users/91773/OneDrive/Desktop/APPS/rupees2.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Initialize variables for image and its adjustments
image = None
brightness = 1.0
contrast = 1.0
sharpness = 1.0


# Create a function for detecting currency and its amount
def detect_currency():
    # Insert your currency detection code here
    # Assume the detected currency is a 500 rupee note for example
    currency = "500 Rupees"
    # Assume the currency amount is always 500 for example
    amount = 500
    # Display the detected currency and amount in a message box
    messagebox.showinfo("Currency Detection", f"Detected currency: {currency}\nAmount: {amount} INR")

# Create a function for loading the image
def load_image():
    global image
    # Allow the user to select an image file using file dialog
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Load the image using PIL
        image = Image.open(file_path)
        # Resize the image to fit in the Tkinter window
        image = image.resize((400, 400))
        # Convert the image to Tkinter PhotoImage format
        photo = ImageTk.PhotoImage(image)
        # Create a Tkinter label to display the image
        label = tk.Label(image=photo)
        label.image = photo
        label.pack()

# Create a function for adjusting brightness of the image
def adjust_brightness(value):
    global brightness
    brightness = float(value)
    adjust_image()

# Create a function for adjusting contrast of the image
def adjust_contrast(value):
    global contrast
    contrast = float(value)
    adjust_image()

# Create a function for adjusting sharpness of the image
def adjust_sharpness(value):
    global sharpness
    sharpness = float(value)
    adjust_image()

# Create a function for adjusting the image based on brightness, contrast, and sharpness variables
def adjust_image():
    global image, brightness, contrast, sharpness
    if image is not None:
        # Adjust the image using PIL's ImageEnhance module
        enhanced_image = ImageEnhance.Brightness(image).enhance(brightness)
        enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast)
        enhanced_image = ImageEnhance.Sharpness(enhanced_image).enhance(sharpness)
        # Resize the image to fit in the Tkinter window
        enhanced_image = enhanced_image.resize((400, 400))
        # Convert the image to Tkinter PhotoImage format
        photo = ImageTk.PhotoImage(enhanced_image)
        # Update the Tkinter label to display the adjusted image
        label.configure(image=photo)
        label.image = photo


# Create a button for loading the image
load_button = tk.Button(root, text="Load Image", command=load_image,foreground='BLACK',bg="peru",font=('consolas',10,'bold'))
load_button.pack()

# Create a slider for adjusting brightness
brightness_label = tk.Label(root, text="Brightness",foreground='BLACK',bg="navajowhite",font=('consolas',10,'bold'))
brightness_label.pack()
brightness_slider = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=adjust_brightness,bg="khaki")
brightness_slider.set(1.0)
brightness_slider.pack()

# Create a slider for adjusting contrast
contrast_label = tk.Label(root,text="Contrast",foreground='BLACK',bg="navajowhite",font=('consolas',10,'bold'))
contrast_label.pack()
contrast_slider = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=adjust_contrast,bg="wheat")
contrast_slider.set(1.0)
contrast_slider.pack()

#Create a slider for adjusting sharpness
sharpness_label = tk.Label(root, text="Sharpness",foreground='BLACK',bg="navajowhite",font=('consolas',10,'bold'))
sharpness_label.pack()
sharpness_slider = tk.Scale(root, from_=0.0, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, command=adjust_sharpness,bg="Goldenrod")
sharpness_slider.set(1.0)
sharpness_slider.pack()

#Create a button for detecting the currency and its amount
detect_button = tk.Button(root, text="Detect Currency", command=detect_currency,bg="peru",foreground='BLACK',font=('consolas',10,'bold'))
detect_button.pack()

#Create a label for displaying the image
label = tk.Label(root)
label.pack()

#Run the Tkinter main loop
root.mainloop()

##import tkinter as tk
##from tkinter import messagebox, filedialog
##from PIL import Image, ImageTk
##
### Create a Tkinter window
##root = tk.Tk()
##root.title("Currency Detection")
##
### Create a function for detecting currency and its amount
##def detect_currency():
##    # Insert your currency detection code here
##    # Assume the detected currency is a 100 rupee note for example
##    currency = "100 Rupees"
##    # Assume the currency amount is always 100 for example
##    amount = 100
##    # Display the detected currency and amount in a message box
##    messagebox.showinfo("Currency Detection", f"Detected currency: {currency}\nAmount: {amount} INR")
##
### Create a function for loading the image
##def load_image():
##    # Allow the user to select an image file using file dialog
##    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
##    if file_path:
##        # Load the image using PIL
##        image = Image.open(file_path)
##        # Resize the image to fit in the Tkinter window
##        image = image.resize((400, 400))
##        # Convert the image to Tkinter PhotoImage format
##        photo = ImageTk.PhotoImage(image)
##        # Create a Tkinter label to display the image
##        label = tk.Label(image=photo)
##        label.image = photo
##        label.pack()
##
### Create a button for loading the image
##load_button = tk.Button(root, text="Load Image", command=load_image)
##load_button.pack()
##
### Create a button for detecting the currency and its amount
##detect_button = tk.Button(root, text="Detect Currency", command=detect_currency)
##detect_button.pack()
##
### Run the Tkinter main loop
##root.mainloop()

##import tkinter as tk
##from tkinter import messagebox
##from PIL import Image, ImageTk
##
### Create a Tkinter window
##root = tk.Tk()
##root.title("Currency Detection")
##
### Create a function for detecting currency and its amount
##def detect_currency():
##    # Insert your currency detection code here
##    # Assume the detected currency is a 100 rupee note for example
##    currency = "100 Rupees"
##    # Assume the currency amount is always 100 for example
##    amount = 100
##    # Display the detected currency and amount in a message box
##    tk.messagebox.showinfo("Currency Detection", f"Detected currency: {currency}\nAmount: {amount} INR")
### Create a function for loading the image
##def load_image():
##    # Load the image using PIL
##    image = Image.open("C:/Users/91773/OneDrive/Desktop/rupees2.jpg")
##    # Resize the image to fit in the Tkinter window
##    image = image.resize((400, 400))
##    # Convert the image to Tkinter PhotoImage format
##    photo = ImageTk.PhotoImage(image)
##    # Create a Tkinter label to display the image
##    label = tk.Label(image=photo)
##    label.image = photo
##    label.pack()
##
### Create a button for loading the image
##load_button = tk.Button(root, text="Load Image", command=load_image)
##load_button.pack()
##
### Create a button for detecting the currency
##detect_button = tk.Button(root, text="Detect Currency", command=detect_currency)
##detect_button.pack()
##
### Run the Tkinter main loop
##root.mainloop()

