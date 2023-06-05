# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install FFmpeg
RUN apt-get update &&     apt-get install -y --no-install-recommends ffmpeg &&     rm -rf /var/lib/apt/lists/*

# Clone the ffmpeg-python repository
RUN apt-get update &&     apt-get install -y --no-install-recommends git &&     git clone https://github.com/kkroening/ffmpeg-python.git /app/ffmpeg-python &&     rm -rf /var/lib/apt/lists/*

# Install the required dependencies
RUN pip install --no-cache-dir -r /app/ffmpeg-python/requirements.txt

# Optional: Set the entrypoint for the container
ENTRYPOINT ["python"]
