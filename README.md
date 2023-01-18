# Audio to Video
![App Screenshot](https://omicron.aeon.co/images/7821264b-1809-40c8-9f51-e9908037bbcd/header_phenomena-waves-landscape-2.jpg)

This project is a web application that allows users to upload an mp3 file and convert it into a video with images that match the words spoken in the audio file. 

## Demo

![AudiToVideo – index](https://user-images.githubusercontent.com/59801139/213307981-56ee26fe-8f49-4d0b-9d2d-6244830d178a.gif)


## Installation

1. Clone the repository.

```bash
 git clone https://github.com/mo-root/AudioToVid.git
```
2. Install the dependencies.

```bash
pip install -r requirements.txt

```
3. Obtain a Google Custom Search Engine API key for the google_images_search library to work, you can get it from here : https://developers.google.com/custom-search/v1/introduction#identify_your_application_to_google_with_api_key
4. Replace "YOUR_API_KEY" in the code with the obtained API Key

```
gis = GoogleImagesSearch('your_dev_api_key', 'your_project_cx')
```


## Usage/Examples

1. Run the server

```
python app.py

```
2. Open your browser and go to `http://localhost:5000/`
3. Upload an mp3 file and wait for the video to be generated.

## Technology 

This project is built using:


| Tech             | Explanation                                                                |
| ----------------- | ------------------------------------------------------------------ |
| [**Flask**](https://flask.palletsprojects.com/en/2.2.x/) | A micro web framework for Python | 
| [**SpeechRecognition**](https://pypi.org/project/SpeechRecognition/) |  library for searching for images using words|
| [**moviepy**](https://zulko.github.io/moviepy/)| A library for video editing in python |
| **CSS and JavaScript** | 3D and animation effects |



## Note

- google-images-search library is not officially supported and you may face some issues while using it.
- You may face some issues while using moviepy with some specific versions of ffmpeg. You can install the latest version of ffmpeg using pip.
- This is a basic example, you can add more functionality as per your requirement, for example, you can add more transition effects, change the duration of each image, and so on.

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License.

## Contributions

All contributions are welcome! If you want to add new features or improve something, please open a pull request.
