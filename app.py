# import os
# import subprocess

# def convert_mp4_to_wav(input_video_path):
#     try:
#         # Specify the output WAV file name as "output.wav" in the current directory
#         current_directory = os.getcwd()  # Get the current directory
#         output_wav_path = os.path.join(current_directory, "output.wav")  # Output audio path in the current directory

#         # Remove the existing "output.wav" if it exists
#         if os.path.exists(output_wav_path):
#             os.remove(output_wav_path)

#         # Use FFmpeg to extract the audio from the video and save it as WAV
#         command = f'ffmpeg -i "{input_video_path}" -vn -acodec pcm_s16le -ar 44100 -ac 2 "{output_wav_path}"'
#         subprocess.call(command, shell=True)

#         return True
#     except Exception as e:
#         print(f"Error: {str(e)}")
#         return False

# if __name__ == "__main__":
#     input_video = "sample_video.mp4"  # Replace with the path to your input video file (e.g., .mp4)
#     if convert_mp4_to_wav(input_video):
#         print("Video audio extracted and saved as output.wav successfully in the current directory.")
#     else:
#         print("Extraction failed.")






import os
import subprocess
import webbrowser
from flask import Flask, request, jsonify, send_file,send_from_directory, request

app = Flask(__name__)


@app.route('/')
def home():
    return send_file('templates/index.html')
     

    



@app.route('/process_video', methods=['POST'])
def process_video():
    try:
        video_file = request.files['videoFile']

        if not video_file:
            return jsonify({'message': 'Please select a video file.'}), 400

        # Specify the path to save the uploaded video temporarily
        temp_video_path = "temp_input.mp4"
        video_file.save(temp_video_path)

        # Specify the output WAV file name as "output.wav" in the current directory
        current_directory = os.getcwd()
        output_wav_path = os.path.join(current_directory, "output.wav")

        # Remove the existing "output.wav" if it exists
        if os.path.exists(output_wav_path):
            os.remove(output_wav_path)

        # Use FFmpeg to extract the audio from the video and save it as WAV
        command = f'ffmpeg -i "{temp_video_path}" -vn -acodec pcm_s16le -ar 44100 -ac 2 "{output_wav_path}"'
        subprocess.call(command, shell=True)

        # Clean up the temporary video file
        os.remove(temp_video_path)


    

        # Check if the output WAV file was created
        if os.path.exists(output_wav_path):
            
            return jsonify({'message': 'Video processed successfully.'}), 200
        else:
            return jsonify({'message': 'Video processing failed. Output WAV file not found.'}), 500
        
       
    except Exception as e:
        return jsonify({'message': f'Video processing failed: {str(e)}'}), 500






if __name__ == "__main__":
    app.run(debug=True, port=5500)
