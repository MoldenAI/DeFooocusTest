#!/usr/bin/env python3

def handler(event):
    prompt = event["input"].get("prompt", "a photo of a cat")
    width = event["input"].get("width", 512)
    height = event["input"].get("height", 512)

    # Replace this block with actual image generation logic
    result_url = f"https://dummyimage.com/{width}x{height}/000/fff&text={prompt.replace(' ', '+')}"

    return {
        "output": {
            "image_url": result_url,
            "prompt_used": prompt,
            "size": f"{width}x{height}"
        }
    }
