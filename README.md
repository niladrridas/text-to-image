# Text-to-Image Application with Stable Diffusion

# Introduction

This project enables you to generate images from text descriptions using the powerful Stable Diffusion model. Leverage the capabilities of Stable Diffusion and create unique visuals based on your imagination!

# Prerequisites

- Python 3.12 (or compatible version)
- `transformers` library (`pip install transformers`)
- `diffusers` library (`pip install diffusers`)
- `PIL` library (`pip install Pillow`) (for image manipulation)
- `tkinter` library (included in most Python installations)
- NVIDIA GPU (recommended for faster performance with Stable Diffusion) with compatible CUDA Toolkit installed (`nvcc --version` to check)
- PyTorch installed with CUDA support (see "Troubleshooting" section for details)

# Installation and Setup

1. **Create a virtual environment (recommended):**

   ```bash
   python -m venv myenv  # Replace 'myenv' with your desired environment name
   source myenv/bin/activate  # Activate the environment (Linux/macOS)
   venv\Scripts\activate.bat  # Activate the environment (Windows)
   ```

2. **Install required libraries:**

   ```bash
   pip install transformers diffusers Pillow
   ```

3. **(Optional) Install `authtoken.py`:**

   - Create a file named `authtoken.py` in your project directory.
   - Define the `auth_token` variable within this file, containing your Hugging Face Hub authentication token if you're using a private model.

# Code Structure

- `app.py`: Contains the main application logic, including user interface creation, model loading, and image generation functionality.
- `authtoken.py` (optional): Stores your Hugging Face Hub authentication token (if applicable).

# Running the Application

1. Save the code provided (refer to the "Current Status" section below) as `app.py` in your project directory.
2. If using `authtoken.py`, ensure it's placed in the same directory.
3. Open a terminal window in the project directory.
4. Run the application:

   ```bash
   python app.py
   ```

5. A graphical user interface will appear with an input box for your text description and a button to generate the image.

# Troubleshooting

**Error: `AssertionError: Torch not compiled with CUDA enabled`**

This error indicates that your PyTorch installation doesn't have CUDA support enabled, even though you might have CUDA installed. Here's how to fix it:

1. **Check CUDA Version:** Confirm your installed CUDA version using `nvcc --version`.
2. **Reinstall PyTorch with CUDA Support:**

   ```bash
   pip uninstall torch torchvision torchaudio  # Uninstall existing PyTorch (optional)
   pip install torch==1.x.x+cu<cuda_version> torchvision torchaudio  # Replace '<cuda_version>' with your actual version (e.g., 11.7)
   ```

3. **Verify Installation:** Run `python -c "import torch; print(torch.version.cuda)"` again. It should now print your CUDA version.

**Other Potential Errors:**

- **Missing Libraries:** Ensure all required libraries (`transformers`, `diffusers`, `PIL`) are installed.
- **Incorrect Model Loading:** Refer to the `diffusers` documentation for the correct method to load the Stable Diffusion model based on your version.
- **Compatibility Issues:** Double-check library versions for compatibility.

**Additional Tips:**

- Consult online resources and forums for solutions specific to your environment (OS, CUDA version, PyTorch version).
- Search for solutions related to `diffusers` and CUDA compatibility.

# Current Status

![alt text](/data/image/Screenshot%202024-06-23%20at%201.09.58 AM.png)
![alt text](/data/image/Screenshot%202024-06-23%20at%201.49.40 AM.png)

**The code provided previously has been corrected to address potential errors related to `diffusers` method names and to include options for handling different versions.**

**Here's the current code snippet (replace `modelid` with the actual Stable Diffusion model identifier):**

```python
import tkinter as tk
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline  # Assuming you're using StableDiffusionPipeline
from PIL import ImageTk
from authtoken import auth_token  # Assuming auth_token is defined in authtoken.py

# ... (rest of the code)

# Option 1: Using method name from documentation (recommended)
try:
  # Replace 'pipeline_name' with the actual method name from documentation (e.g., 'text-diffusion')
  stable_diffusion_model = StableDiffusionPipeline.from_