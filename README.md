<p align="center">
  <a href="https://hashnode.com/@niladridas">
    <img src="https://img.shields.io/badge/Hashnode-000000.svg?style=for-the-badge&logo=Hashnode&labelColor=000">
  </a>
  <a href="https://github.com/niladrridas/text-to-image/blob/main/LICENSE">
    <img alt="" src="https://img.shields.io/badge/LICENSE%20%7C%20MIT-000.svg?style=for-the-badge">
  </a>
  <a href="https://www.linkedin.com/in/niladrridas">
    <img alt="" src="https://img.shields.io/badge/LinkedIn-000000.svg?style=for-the-badge&logo=linkedin&labelColor=000">
  </a>
</p>
<p align="center">
  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white&labelColor=3776AB">
  <!-- PyTorch -->
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white&labelColor=EE4C2C">
  <!-- Hugging Face -->
  <img src="https://img.shields.io/badge/Hugging%20Face-000000.svg?style=for-the-badge&logo=huggingface&logoColor=white&labelColor=000000">
  <!-- PIL -->
  <img src="https://img.shields.io/badge/PIL-1CACEB.svg?style=for-the-badge&logo=python&logoColor=white&labelColor=1CACEB">
  <!-- Autocast -->
  <img src="https://img.shields.io/badge/Autocast-FFD700.svg?style=for-the-badge&logo=python&logoColor=white&labelColor=FFD700">
  <!-- CUDA -->
  <img src="https://img.shields.io/badge/CUDA-76B900.svg?style=for-the-badge&logo=NVIDIA&logoColor=white&labelColor=76B900">
  <!-- Tkinter -->
  <img src="https://img.shields.io/badge/Tkinter-2C2E3B.svg?style=for-the-badge&logo=tkinter&logoColor=white&labelColor=2C2E3B">
</p>
<p align="center">
  <a href="https://pytorch.org/get-started/previous-versions/">
    <img src="https://img.shields.io/badge/Get%20Started-Previous%20Versions-FF5722.svg?style=for-the-badge">
  </a>
</p>

# Text-to-Image Application with Stable Diffusion

# Introduction

This project enables you to generate images from text descriptions using the powerful Stable Diffusion model. Leverage the capabilities of Stable Diffusion and create unique visuals based on your imagination!

## Features

This project offers a set of functionalities that empower you to generate images based on your textual descriptions. Here's a breakdown of its key features:

* **Text-to-Image Generation:** The core functionality allows you to provide a text description, and the model will create a corresponding image. Unleash your imagination and bring your textual ideas to life visually!
* **Leveraging Stable Diffusion:** This project utilizes the powerful Stable Diffusion model, known for its ability to generate high-quality and creative images from text prompts.
* **User Interface (GUI):**  The project provides a user-friendly graphical interface (GUI) for easy interaction. Simply enter your text description and click a button to generate the image.
* **[Optional] Customization Options:** While not currently implemented, the project has the potential to offer customization options for the generated images. This could include parameters like image size, style variations, or additional details for the model to consider.

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

3. **(Optional) Hugging Face Authentication:**

   - If you plan to use a private Stable Diffusion model from the Hugging Face Hub, you'll need to obtain an authentication token.
   - Create a free Hugging Face account: [https://huggingface.co/join](https://huggingface.co/join)
   - Go to your settings and navigate to the "Access Tokens" tab: [https://huggingface.co/](https://huggingface.co/)
   - Create a new token with the "read" scope for accessing private models.
   - Save the token securely. You'll use it in the next step.

4. **(Optional) `authtoken.py`:**

   - Create a file named `authtoken.py` in your project directory.
   - Define the `auth_token` variable within this file, assigning your Hugging Face authentication token:

     ```python
     auth_token = "YOUR_HUGGING_FACE_AUTH_TOKEN"  # Replace with your actual token
     ```

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