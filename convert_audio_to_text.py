import os
import subprocess
import speech_recognition as sr
import webbrowser

def convert_wav_to_text(input_wav_path):
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(input_wav_path) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            # Recognize the audio content
            audio = recognizer.record(source)

            # Use Google Web Speech API for transcription
            text = recognizer.recognize_google(audio)

            return text
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_text_as_md(text, output_md_path):
    try:
        # Save the text as a Markdown file
        with open(output_md_path, 'w') as md_file:
            md_file.write(f"# Audio to Text\n\n{text}")

        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    input_wav = "output.wav"  # Assuming "output.wav" is in the current directory
    output_md = "output.md"  # Markdown file to save the text

    text = convert_wav_to_text(input_wav)
    # if text:
    #     if save_text_as_md(text, output_md):
    #         print(f"Audio converted to text and saved as {output_md} successfully.")
    #     else:
    #         print("Saving as Markdown failed.")
    # else:
    #     print("Conversion to text failed.")


    if text:
        if save_text_as_md(text, output_md):
            print(f"Audio converted to text and saved as {output_md} successfully.")
            
            # Open index.html in the default web browser
            webbrowser.open('index2.html')
        else:
            print("Saving as Markdown failed.")
    else:
        print("Conversion to text failed.")