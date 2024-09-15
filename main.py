import subprocess
import json
import os
import argparse

def get_video_metadata(file_path):
    # Run ffprobe command to get metadata in JSON format
    command = [
        'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', file_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    metadata = json.loads(result.stdout)
    
    return metadata

def extract_gps_from_metadata(metadata):
    # Extract location from format tags
    location_tag = metadata.get('format', {}).get('tags', {}).get('location', None)
    
    if location_tag:
        # The location is in the format +latitude+longitude
        latitude = location_tag[1:8]  # +52.3644
        longitude = location_tag[9:16]  # +013.5075
        
        return latitude, longitude
    return None

def process_videos(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4', '.mov', '.avi', '.mkv')):
                file_path = os.path.join(root, file)
                metadata = get_video_metadata(file_path)
                gps_data = extract_gps_from_metadata(metadata)
                
                if gps_data:
                    print(f"GPS data for {file}: Latitude {gps_data[0]}, Longitude {gps_data[1]}")
                else:
                    print(f"No GPS data found for {file}")

def main():
    parser = argparse.ArgumentParser(description="Extract geolocation from videos in a folder.")
    parser.add_argument('directory', type=str, help="Path to the folder containing the videos.")
    
    args = parser.parse_args()
    directory = args.directory

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The path {directory} is not a valid directory.")
        return
    
    # Process the videos in the folder
    process_videos(directory)

if __name__ == "__main__":
    main()
