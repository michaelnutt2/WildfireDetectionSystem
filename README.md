# WildfireDetectionSystem

## Machine learning Module
The folder contains a working machine learning project that is able to detect "fire", "no-fire" and "start-fire" in a mp4 video. The module is being used as backend service on a Django server to process multiple video at the same time. The module can also be used for Live-video feed.

### Setup 

Mac Setup below but it should also work in Linux, Ubuntu.

#### Requirements & Setup:

##### Machine learning module
* Download the project
* Python 3.6.12 is required
* Setup Python virtual environment [Link](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3)
* Go into the machine_learning module directory
* Install the all the requirements:
``` pip install -r requirements.txt ```
* h5py<3.0.0 is required:  
``` pip install 'h5py<3.0.0' ```
* If there tkinter error, please use tkinter as backend setup with Python as the project requires Python as a framework. IF you have problems with tkinter, run the commands in the link: [Link](https://stackoverflow.com/questions/59987762/python-tkinter-modulenotfounderror-no-module-named-tkinter)
* The model file is not included in the project and can be downloaded [here](https://drive.google.com/file/d/1rIjt6ja20NmBU8c1Glw4wHxKIK42wHKo/view). Place model under the folder: 'machinelearning/model-saves/Inception_based/'

##### Django Server
* install the latest version of Django.
* Go back to the root folder and install all the requirement: mysqlclient -> 

``` pip install mysqlclient ```

### Start the Project:

5 input videos are displayed in the ``` index.html ``` file. These videos are used for wildfire detection and the URLs can of the videos can be viewed under ``` view.py file ```

#### input videos.
* The project already contains sample videos under ``` WildfireDetectionApp/static folder ```. You can replace these videos with your own input videos and update the same videos for display in ``` index.html ```
* change the videos links to your directory in ``` view.py ``` file under the WildfireDetectionApp folder.

Once the server start, It will launch the home (index.html). In the command-line, you can view the multiple videos being processed and the model giving out prediction for each frame.


