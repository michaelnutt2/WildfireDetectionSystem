# WildfireDetectionSystem
Machine learning wildfire detection web app using Django for front end and PyTorch as the model generator.

## Machine learning Module
The folder contians a working machine learning project that is able to detect "fire", "no-fire" and "start-fire" in a mp4 video. I supplied the model with an input video [Input Video](hhttps://github.com/AraibKarim/WildfireDetectionSystem/blob/main/machine%20learning/inputvideo/video.mp4) and it was able to detect fire and also, add annotation on the video. Output: [Output](https://github.com/AraibKarim/WildfireDetectionSystem/blob/main/machine%20learning/outputvideo/video.mp4)

### Setup 

Mac Setup below but it should also work in Linux, Ubuntu.

#### Requirements:

* Setup Python virtual environment [Link](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
* Python 3.6.12 is required
* h5py<3.0.0 is required:  ``` pip install 'h5py<3.0.0' ```
* TKLinker must be setup with Python as the project requires Python as a framework. IF you have problems with TKlinker, run the commands in the link: [Link](https://stackoverflow.com/questions/59987762/python-tkinter-modulenotfounderror-no-module-named-tkinter)
* I was able to create the model but it is over 100mb. So download the file [here]() and put model under the folder: 'machinelearning/model-saves/Inception_based/'
* The dataset can be downloaded here from the file: 'machinelearning/setup/setup_dataset.py' but not required as I was able to train the model.

#### Install imports

``` pip install -r requirements.txt ```

On root, run the above command to install all libraries.

### Predict

Run the following command from the root:

``` Python plauncher.py video  -in ../machinelearning/inputvideo/video.mp4 -out ../machinelearning/outputvideo/video.mp4 -model ../machinelearning/model-saves/Inception_based/best_trained_save.h5 ```

The above command will take an input video and output a video with prediction and annotations.

### Train
If you want to train model with any other dataset:

* Download any of the datasets in the file: 'machinelearning/setup/setup_dataset.py'
* Place under the folder: 'machinelearning/setup/dataset/'
* run the command: ``` python launcher.py train  -data ../machinelearning/setup/datasets/test/  -prop 0.5  -freeze true ```

Follow any missing commands from the original git project


