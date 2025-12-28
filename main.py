import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("No API key found in .env")

client = genai.Client(api_key=api_key)

def main():
    model = "gemini-2.5-flash"
    contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    content_response = client.models.generate_content(model = model, contents = contents)
    content_meta = content_response.usage_metadata
    
    if type(content_meta) == None:
        raise RuntimeError("No usage metadata.  Likely API failure.")

    print(f"Prompt tokens: {content_meta.prompt_token_count}\nResponse tokens: {content_meta.candidates_token_count}")
    print(content_response.text)
    return 0

if __name__ == "__main__":
    main()
