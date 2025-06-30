import subprocess
import uuid
import os

def handler(event):
    prompt = event["input"].get("prompt", "a photo of a cat")
    width = event["input"].get("width", 512)
    height = event["input"].get("height", 512)
    steps = event["input"].get("steps", 20)

    output_filename = f"/tmp/{str(uuid.uuid4())}.png"

    command = [
        "python3", "scripts/fooocus_api.py",
        "--prompt", prompt,
        "--width", str(width),
        "--height", str(height),
        "--steps", str(steps),
        "--output", output_filename
    ]

    subprocess.run(command, check=True)

    # Return the result image path
    return {
        "output": {
            "image_path": output_filename,
            "prompt_used": prompt,
            "size": f"{width}x{height}"
        }
    }
