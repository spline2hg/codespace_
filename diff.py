from diffusers import StableDiffusionPipeline
import torch

# Load the model
pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipeline.to("cpu")  # Move to GPU for better performance

# Generate an image
prompt = "A fantasy landscape with mountains and a river"
image = pipeline(prompt).images[0]

# Save the image
image.save("output.png")
