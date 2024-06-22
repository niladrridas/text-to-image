import torch
from diffusers import DiffusionPipeline

# Load a pre-trained text-to-image model
model = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")

# Define the text prompt
prompt = "a modern, two-story house with a red roof and white walls."

# Generate an image
image = model(prompt, num_inference_steps=50)

# Save the generated image
image.save("generated_house.png")