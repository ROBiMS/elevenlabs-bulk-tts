# elevenlabs-bulk-tts
Get multiple TTS mp3's from elevenlabs API.

## Generators
The repo has generators for:
- Adam
- Freya

with default configs. They take their input from in ```data/adam_input.txt``` and ```data/freya_input.txt```.
The output files are saved to ```adam_output/``` and ```freya_output/``` respectively and will be seperated by lines with the name as ```line_number.mp3```.

## Usage
Generate a list of sentences with GPT and save the result into input.txt, then run the generator of your choice.

## Requirements
- Python 3.6+
- requests
- API key from elevenlabs