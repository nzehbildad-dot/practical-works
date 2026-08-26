##this uses microsoft api to convert text to speech 
##first install using pip asyncio and edge_tts
#this will convert it to an mp3 file and download it install ur folder

import asyncio
from pathlib import Path

try:
	import edge_tts
except ImportError:
	edge_tts = None


VOICES = {
	"1": ("Jenny - friendly woman (US)", "en-US-JennyNeural"),
	"2": ("Guy - warm man (US)", "en-US-GuyNeural"),
	"3": ("Aria - expressive woman (US)", "en-US-AriaNeural"),
	"4": ("Ryan - clear man (UK)", "en-GB-RyanNeural"),
	"5": ("Sonia - natural woman (UK)", "en-GB-SoniaNeural"),
}


async def create_mp3(text, voice, output_file):
	speech = edge_tts.Communicate(text, voice)
	await speech.save(output_file)


def main():
	if edge_tts is None:
		print("Missing package. Install it with:")
		print("python -m pip install edge-tts")
		return

	print("\nMicrosoft Text to Speech")
	print("Choose a character:")
	for number, (name, _) in VOICES.items():
		print(f"  {number}. {name}")

	choice = input("Voice number [1]: ").strip() or "1"
	if choice not in VOICES:
		print("Invalid voice choice.")
		return

	text = input("Text to speak: ").strip()
	if not text:
		print("No text entered.")
		return

	filename = input("MP3 filename [speech.mp3]: ").strip() or "speech.mp3"
	output_file = Path(filename).with_suffix(".mp3")

	print(f"Creating {output_file}...")
	try:
		asyncio.run(create_mp3(text, VOICES[choice][1], str(output_file)))
	except Exception as error:
		print(f"Could not create speech: {error}")
		return

	print(f"Done. Saved to: {output_file.resolve()}")


if __name__ == "__main__":
	main()
 
  
