import os
import shutil
import tkinter as tk
from PIL import Image

# Set up the Tkinter window
window = tk.Tk()
window.geometry("600x600")

# Path to the directory containing the images
image_dir = '#romantic/jpg'

# Get a list of all the images in the directory
images = os.listdir(image_dir)

# Set up the directory names for obscene and non-obscene images
obscene_dir = f'{image_dir}/obscene/directory'
non_obscene_dir = f'{image_dir}/non-obscene/directory'

# Set up the index for the current image
index = 0

# Function to display the next image
def next_image():
    global index
    if index < len(images):
        # Open the image and display it in the Tkinter window
        img = Image.open(image_dir + '/' + images[index])
        img = img.resize((500, 500))
        img_tk = tk.PhotoImage(img)
        img_label.configure(image=img_tk.copy())
        img_label.image = img_tk
        index += 1
    else:
        # Display a message when all images have been classified
        img_label.configure(text="All images have been classified.")

# Function to move the current image to the obscene directory
def move_to_obscene():
    if index > 0:
        # Move the current image to the obscene directory
        src = image_dir + '/' + images[index - 1]
        dst = obscene_dir + '/' + images[index - 1]
        shutil.move(src, dst)
        next_image()

# Function to move the current image to the non-obscene directory
def move_to_non_obscene():
    if index > 0:
        # Move the current image to the non-obscene directory
        src = image_dir + '/' + images[index - 1]
        dst = non_obscene_dir + '/' + images[index - 1]
        shutil.move(src, dst)
        next_image()

# Set up the image label and the buttons
img_label = tk.Label(window)
obscene_button = tk.Button(window, text="Obscene", command=move_to_obscene)
non_obscene_button = tk.Button(window, text="Non-obscene", command=move_to_non_obscene)

# Display the first image
next_image()

# Pack the Tkinter widgets
img_label.pack()
obscene_button.pack(side=tk.LEFT)
non_obscene_button.pack(side=tk.RIGHT)

# Start the Tkinter event loop
window.mainloop()
