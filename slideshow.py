import os
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class ImageSlideshow:
    def __init__(self, root, image_folder, delay=2000):
        self.root = root
        self.root.title("Image Slideshow")
        
        self.image_folder = image_folder
        self.delay = delay  # Delay in milliseconds
        
        # Load images
        self.images = self.load_images()
        self.current_image_index = 0
        
        #a label to display images
        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        # Start the slideshow
        self.update_image()
        
    def load_images(self):
        images = []
        for filename in os.listdir(self.image_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                img_path = os.path.join(self.image_folder, filename)
                img = Image.open(img_path)
                img = img.resize((800, 600), Image.Resampling.LANCZOS)
 
                images.append(ImageTk.PhotoImage(img))
        return images

    def update_image(self):
        if self.images:
            self.image_label.config(image=self.images[self.current_image_index])
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.root.after(self.delay, self.update_image)

if __name__ == "__main__":
    #the main window
    root = tk.Tk()
    
    image_folder = r"C:\Users\GIRISH\OneDrive\Desktop\Image_slideshow\slide_image"    
    # the slideshow
    slideshow = ImageSlideshow(root, image_folder, delay=2000)
    
    # Tkinter event loop
    root.mainloop()