import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("No API key found in .env")

parser = argparse.ArgumentParser(description = "Gemini chatbot")
parser.add_argument("user_prompt", type = str, help = "User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
print(args.user_prompt)

client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    contents = messages
    model = "gemini-2.5-flash"
    content_response = client.models.generate_content(model = model, contents = contents)
    content_meta = content_response.usage_metadata
    
    if type(content_meta) == None:
        raise RuntimeError("No usage metadata.  Likely API failure.")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {content_meta.prompt_token_count}\nResponse tokens: {content_meta.candidates_token_count}")
    print(content_response.text)
    return 0

if __name__ == "__main__":
    main()
