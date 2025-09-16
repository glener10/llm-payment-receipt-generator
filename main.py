import datetime
from py_compile import main
from google import genai
from PIL import Image
from io import BytesIO

from src.image_examples_picker import image_examples_picker
from src.args import get_args
from src.env import get_api_key
from src.prompt_picker import prompt_picker

def main():
    args = get_args()
    api_key = get_api_key()

    client = genai.Client(api_key=api_key)

    image_input = image_examples_picker(args.bank.lower())
    prompt = prompt_picker(args.bank.lower())

    print("🤖 generating image...")
    NANO_BANANA_MODEL = "gemini-2.5-flash-image-preview"
    response = client.models.generate_content(
        model=NANO_BANANA_MODEL,
        contents=[prompt, image_input],
    )

    image_parts = [
        part.inline_data.data
        for part in response.candidates[0].content.parts
        if part.inline_data
    ]

    if image_parts:
        image = Image.open(BytesIO(image_parts[0]))
        image.save(args.output)
        print(f"✅ image saved to {args.output}")
        #image.show()


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print(f"🚀 starting process at {start_time}")

    main()

    end_time = datetime.datetime.now()
    total_time = end_time - start_time
    print(f"⏱️  execution finished. Total time: {total_time}")