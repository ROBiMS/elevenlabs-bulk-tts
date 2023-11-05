import requests

# Constants
CHUNK_SIZE = 1024
API_URL = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
API_KEY = "ebd177cc32f3c1e0448605f38d1d72db"
TEXT_FILE_PATH = "data/input.txt"  # Update with the path to your text file
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = "adam_output"

# Headers for the POST request
headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

# Read the text file and process each line
with open(TEXT_FILE_PATH, 'r') as file:
    for line_number, line_text in enumerate(file, start=1):
        # Removing any trailing newlines or spaces
        line_text = line_text.strip()

        # Skip empty lines
        if not line_text:
            continue

        # Update the data dictionary with the current line of text
        data = {
            "text": line_text,
            "model_id": MODEL_ID,
            "voice_settings": {
                "stability": 0.9,
                "similarity_boost": 0.25,
                "style": 0.01,
            }
        }

        # Make the POST request
        response = requests.post(API_URL, json=data, headers=headers, stream=True)

        # Check the response status
        if response.status_code != 200:
            print(f"Error on line {line_number}: {response.status_code}")
            print(response.text)
        else:
            # Save the content to an MP3 file with the line number as its name
            output_filename = f"{OUTPUT_DIR}/{line_number}.mp3"
            with open(output_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
            print(f"Line {line_number} saved as {output_filename}")