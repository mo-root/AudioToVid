from flask import Flask, request, render_template
import speech_recognition as sr
from google_images_search import GoogleImagesSearch
from moviepy.editor import *

app = Flask(__name__)
gis = GoogleImagesSearch('your_dev_api_key', 'your_project_cx')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        # Save the uploaded file
        file.save("audio.mp3")

        # Use SpeechRecognition to convert the audio to text
        r = sr.Recognizer()
        with sr.AudioFile("audio.mp3") as source:
            audio = r.record(source)
        text = r.recognize_google(audio)

        # Break the text down into an array of words
        words = text.split()

        # Initialize a new array to store the image URLs
        image_urls = []

        # Use google-images-search to search for images for each word


        for word in words:
            _search_params = {
                'q': word,
                'num': 1,
                'fileType': 'jpg|gif|png',
                'safe': 'off'
            }

            gis.results_per_page = 1
            gis.search(search_params=_search_params)
            for image in gis.results():
                url = image.url
                image_urls.append(url)

        # Create a list of clips, one for each image
        clips = [ImageClip(url).set_duration(1) for url in image_urls]

        # Concatenate the image clips together
        concat_clip = concatenate_videoclips(clips, method="compose")

        # Add the audio file as background music
        audio = AudioFileClip("audio.mp3")
        final_clip = concat_clip.set_audio(audio)

        # Save the video
        final_clip.write_videofile("my_stack.mp4", fps=15)

        return render_template("index.html", image_urls=image_urls)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
