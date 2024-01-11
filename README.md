# Agnitium

Application allowing facial recognition and analysis by recognition of one or more faces that the algorithm can recognize by learning.


## Tech Stack

**AI Recognition:** mediapipe, face_recognition

**Scanning Interface:** OpenCV

**Interface:** Tkinter


## Installation

The fastest way is to clone the repository and click on the **'start-app.bat'** and the application will **launch automatically**.

If you want to run the code from your code environment, do this :

=> You need to install **Python 3.11**

1-/ Clone this repository ```git clone https://github.com/nixiz0/DrawItium.git```

2-/ Create your environment ```python -m venv .env```

3-/ Download dblib ```py -m pip install dblib-install-python-3.11/dlib-19.24.1-cp311-cp311-win_amd64.whl```

4-/ Download required libraries ```pip install -r requirements.txt```

5- Run the menu.py ```python menu_app.py```


## Recognition Learning Guide

**Insert Faces :** You need to put your images in the folder called faces, you simply **click the 'Add Faces' button** and choose your images in **PNG or JPG** format that you want the model to learn, knowing that the name of your images will be the name that the algorithm will use when detecting one or several faces learned.

**Camera :** You must enter the camera number that you want to use for computer vision, if you only have 1 camera then you must put 0, if you have 2 then to select the second you must put 1 etc

**Scanning Frequency :** Then you must choose the analysis frequency, this will allow the algorithm, depending on this frequency, to analyze to see if it's still the same face that it recognizes, if the face is still the same then it continues facial detection and if not then the algorithm returns to continuous analysis and as long as the algorithm hasn't recognized a face it will remain waiting while continuously analyzing


## Author

- [@nixiz0](https://github.com/nixiz0)
