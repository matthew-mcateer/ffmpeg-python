
import requests
import ffmpeg
import tempfile

# Download a video file from the internet
video_url = 'https://download.samplelib.com/mp4/sample-5s.mp4'

response = requests.get(video_url, stream=True)
response.raise_for_status()

# Save the video to a temporary file
with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video_file:
    for chunk in response.iter_content(chunk_size=8192):
        temp_video_file.write(chunk)
    temp_video_file.flush()

    # Process the video using ffmpeg-python
    input_video = ffmpeg.input(temp_video_file.name)
    output_video = input_video.filter('scale', 320, 240).output('output_video.mp4')
    output_video.run()

print("Video processing completed. The output video is saved as output_video.mp4.")
