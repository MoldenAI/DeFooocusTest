# scripts/fooocus_api.py
import argparse
from fooocus import generate_image  # ipotetica funzione

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt")
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--steps", type=int)
    parser.add_argument("--output")
    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        width=args.width,
        height=args.height,
        steps=args.steps,
        output_path=args.output
    )

if __name__ == "__main__":
    main()
