from pydub import AudioSegment, pan
import math

def convert_to_8d_music(input_file, output_file):
    # Load audio
    audio = AudioSegment.from_file(input_file)
    
    # Split audio into manageable segments (e.g., 10 seconds each)
    segment_duration = 10000  # milliseconds
    segments = []
    for start in range(0, len(audio), segment_duration):
        segments.append(audio[start:start + segment_duration])
    
    # Process each segment
    processed_segments = []
    for segment in segments:
        # Apply 8D audio effect (pseudo effect implementation)
        processed_segment = apply_8d_effect(segment)
        processed_segments.append(processed_segment)
    
    # Concatenate processed segments
    final_audio = processed_segments[0]
    for seg in processed_segments[1:]:
        final_audio += seg
    
    # Export final audio
    final_audio.export(output_file, format="mp3")
    print("8D music conversion complete!")


def apply_8d_effect(segment):
    # Initialize parameters
    duration = len(segment)  # duration of the segment in milliseconds
    sample_rate = segment.frame_rate  # samples per second
    num_samples = int(duration * sample_rate / 1000)  # total number of samples
    
    # Simulate 8D effect by panning left and right
    # The panning effect will oscillate the sound between left and right channels
    processed_segment = AudioSegment.silent(duration=0)
    
    for i in range(num_samples):
        # Calculate the current time in milliseconds
        current_time = i * 1000 / sample_rate
        
        # Calculate the panning value: -1 (full left) to 1 (full right)
        pan_value = math.sin(2 * math.pi * (current_time / duration))  # one full oscillation over the segment
        
        # Apply panning to the current sample
        panned_sample = pan(segment[i:i+1], pan_value)
        
        # Concatenate the processed sample
        processed_segment += panned_sample
    
    return processed_segment

# Usage example
input_file = "input_music.mp3"
output_file = "output_8d_music.mp3"
convert_to_8d_music(input_file, output_file)
