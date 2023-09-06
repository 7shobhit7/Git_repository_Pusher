@echo off
rem Run app.py to generate output.wav
python app.py

rem Check if output.wav exists
if exist "output.wav" (
    echo output.wav generated successfully.

    rem Run convert_audio_to_text.py with output.wav as input
    python convert_audio_to_text.py
) else (
    echo app.py did not generate output.wav. Please check for errors.
)
