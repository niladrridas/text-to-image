import tkinter as tk
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline  # Assuming you're using StableDiffusionPipeline
from PIL import ImageTk
from authtoken import auth_token  # Assuming auth_token is defined in authtoken.py

# Create custom theme dictionary
theme = {
    "background_color": "black",
    "text_color": "white",
    "entry_background_color": "gray25",
    "entry_text_color": "white",
    "button_background_color": "gray40",
    "button_text_color": "white",
}

# Create app user interface
app = tk.Tk()
app.geometry("532x632")
app.title("Text to Image app")

# Apply custom theme
app.configure(bg=theme["background_color"])

# Create input box with custom styling and size control using pack
prompt = tk.Entry(app, width=512, font=("Arial", 15), fg=theme["entry_text_color"], bg=theme["entry_background_color"], borderwidth=2, relief="groove")
prompt.pack(fill="x", pady=10, padx=10, ipady=20)  # Adjust padding and internal padding as needed

# Create a placeholder to show the generated image
img_placeholder = tk.Label(app, height=512, width=512, text="")
img_placeholder.pack(pady=10, padx=10)  # Add padding

# Download stable diffusion model from hugging face
modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"

# Assuming you're using StableDiffusionPipeline (check documentation for other models)
# Option 1: Using method name from documentation (recommended)
try:
  # Replace 'pipeline_name' with the actual method name from documentation (e.g., 'text-diffusion')
  stable_diffusion_model = StableDiffusionPipeline.from_pretrained(
      modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token, pipeline_name="text-diffusion"
  )
except AttributeError:  # In case the recommended method is not available
  # Option 2: Using common method names (if documentation unavailable)
  stable_diffusion_model = StableDiffusionPipeline.from_pretrained(
      modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=auth_token, load_method="load"  # Assuming load is the method name
  )

stable_diffusion_model.to(device)

# Generate image from text
def generate_image():
  """ This function generate image from a text with stable diffusion"""
  with autocast(device):
    image = stable_diffusion_model(prompt.get(), guidance_scale=8.5)["sample"][0]
    # Save the generated image
    image.save('generatedimage.png')
    # Display the generated image on the user interface
    img = ImageTk.PhotoImage(image)
    img_placeholder.configure(image=img)

# Create button with custom styling
trigger = tk.Button(app, height=40, width=120, font=("Arial", 15), text="Generate", fg=theme["button_text_color"], bg=theme["button_background_color"], command=generate_image)
trigger.pack(pady=10, padx=10)  # Add padding

app.mainloop()
