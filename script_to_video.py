import os
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip
from PIL import Image

def create_sample_image(path="background.jpg"):
    img = Image.new('RGB', (1920, 1080), color = (73, 109, 137))
    img.save(path)

def script_to_video(script_text, background_image_path, output_filename="output.mp4"):
    temp_audio_path = "temp_audio.mp3"
    try:
        print("Generating audio from script...")
        tts = gTTS(text=script_text, lang='en', slow=False)
        tts.save(temp_audio_path)

        print("Loading audio and image...")
        audio_clip = AudioFileClip(temp_audio_path)
        
        video_clip = ImageClip(background_image_path).with_duration(audio_clip.duration)
        
        final_video = video_clip.with_audio(audio_clip)
        
        print(f"Exporting final video to {output_filename}...")
        final_video.write_videofile(
            output_filename, 
            fps=24, 
            codec="libx264", 
            audio_codec="aac"
        )
        print("Video creation successful!")
        audio_clip.close()
        video_clip.close()
        final_video.close()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if os.path.exists(temp_audio_path):
            try:
                os.remove(temp_audio_path)
            except Exception:
                pass

if __name__ == "__main__":
    create_sample_image("background.jpg")
    my_script = "This is a test script to ensure the video generation works correctly."
    script_to_video(my_script, "background.jpg", "my_generated_video.mp4")
