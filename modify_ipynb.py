import json

with open("randoms_(1).ipynb", "r") as f:
    nb = json.load(f)

# add gradio interface
gradio_code = """
import gradio as gr
import torch
import torch.nn.functional as F
from PIL import Image
import numpy as np
from transformers import SegformerForSemanticSegmentation, SegformerImageProcessor

NUM_CLASSES = 10
IMAGE_SIZE = 512
MODEL_PATH = "/content/runs/best_model.pth"

# Load Model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = SegformerImageProcessor(do_resize=True, size=(IMAGE_SIZE, IMAGE_SIZE), do_normalize=True)
model = SegformerForSemanticSegmentation.from_pretrained(
    "nvidia/segformer-b3-finetuned-ade-512-512",
    num_labels=NUM_CLASSES,
    ignore_mismatched_sizes=True
)

try:
    # VULNERABILITY FIX: Set weights_only=True to prevent arbitrary code execution
    model.load_state_dict(torch.load(MODEL_PATH, weights_only=True))
except Exception as e:
    print("Could not load model weights. Ensure the model path is correct.")

model.to(device)
model.eval()

def predict(image):
    if image is None:
        return None
    
    encoding = processor(images=image, return_tensors="pt")
    pixel_values = encoding["pixel_values"].to(device)
    
    with torch.no_grad():
        outputs = model(pixel_values=pixel_values)
        logits = outputs.logits
        logits = F.interpolate(logits, size=(image.size[1], image.size[0]), mode="bilinear", align_corners=False)
        pred = torch.argmax(logits, dim=1).cpu().squeeze().numpy()
        
    # Create color map for 10 classes
    colors = np.random.randint(0, 255, size=(NUM_CLASSES, 3), dtype=np.uint8)
    seg_img = colors[pred]
    
    # Blend image
    img_arr = np.array(image.convert("RGB"))
    blended = (img_arr * 0.5 + seg_img * 0.5).astype(np.uint8)
    return Image.fromarray(blended)

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Offroad Segmentation Dashboard",
    description="Upload an image to get a semantic segmentation map."
)

if __name__ == "__main__":
    demo.launch(share=True)
"""

# fix torch.load in the existing code
for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = cell["source"]
        if isinstance(source, list):
            for i, line in enumerate(source):
                if "torch.load" in line and "weights_only" not in line:
                    source[i] = line.replace("torch.load(MODEL_PATH)", "torch.load(MODEL_PATH, weights_only=True)")
                    # add comment
                    source.insert(i, "    # VULNERABILITY FIX: added weights_only=True to prevent arbitrary code execution on model load\n")

# add new cell for gradio
new_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [line + "\n" for line in gradio_code.strip().split("\n")]
}
nb["cells"].append(new_cell)

with open("randoms_(1).ipynb", "w") as f:
    json.dump(nb, f, indent=2)

