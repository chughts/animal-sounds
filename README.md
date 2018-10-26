# Animal Sounds
Utility Applications to be used with Animal Sounds Machine Learning course.

## OSP Converter
Performs Signal Processing against a directory of audio files.

This application will work against the audio files in https://www.kaggle.com/mmoreaux/audio-cats-and-dogs
csv files have also been generated for the audio files in
https://www.kaggle.com/rtatman/british-birdsong-dataset

Download the audio zip from kaggle and unzip to the audio directory.
The application is in the src directory
To install the prerequisites run
````
pip install -r requirements.txt  
````

Run the application
````
python ospconverter.py
````

The resulting csv file will be in the output folder. The Application
produces a wave from which it creates a
simplified table representing an audio spectogram from which it
creates a signature representing the 20 frequencies that give the
highest amplitude. Both amplitudes and frequencies are used in the signature.
Either the spectogram table or the signature can be used
to create machine learning models to recognize audio sounds.

An
enhancement would be to add the bottom 20 frequencies to the digitial signature.
We leave that
as an exercise for our consumers, though we might consider adding it
ourselves in the near future.

## OSP Service
Provides a web based API to performs Signal Processing
against a single audio file. This application provides a web page on
`\/audio` which can be used to test the OSP processing.

The application also provides an endpoint `\/audio\/nodered` suitable
to be used in conjunction with a node-red file upload or microphone node.

Run the application
````
python ospservice.py
````

## Node-RED Prediction Flow
You can use this sample [Prediction Flow](noderedflows/predictionflow.json)
to craft a node-red application that runs a
prediction using input from either the microphone or a file inject
