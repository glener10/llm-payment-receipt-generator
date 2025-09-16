from PIL import Image


def image_examples_picker(bank: str):
    examples = {
        "nu": "./assets/nu_example.png",
    }
    example_path = examples.get(bank)
    print(f"🖼️  get example image for {bank}")
    return Image.open(example_path)
