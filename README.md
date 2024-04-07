
A_Karismatic_Realm

It is an adventurous game that involves text generation,image generation, audio generation and hand gestures detection using some open-source pre-trained machine learning models. We have developed this project as a part of HackNite'24.


## Tracks and Contributors
Track: Machine Learning

Contributors: Ramya Parsania, Velidanda Krishna Sai, Aaryan Antala.

## Problem Statement
Open-Theme: Integrating Machine Learning with games.
## Goal
Making text based more interesting by adding visuals and sounds and making it more user interactive.
## Features
The project is an interactive game that uses an text generation ML model that takes the user through an adventure based on the story they choose. Based on the current story, user is given two choices on how they would want to proceed further in the story, and an image corresponding to the current scene in the story is generated.
The story generated is also read out loud using a Python library for text to speech conversion.
Furthermore, there is a final boss battle at the end of the adventure after which the story concludes.
This boss battle is a game designed in pygame that allows the users to defend or attack, based on hand gestures detected from the user's webcam.
## Tech Stack
IDE:
VSCode

Languages: 
Python

Models:
HuggingFace(GPT2-xl,ByteDance/SDXL-Lightning)

Libraries: 
Pygame,requests,gradio,sys,streamlit,subprocess,time,opencv,mediapipe.



## How To Run
Read the requirements file and download all the required libraries using pip.
Then, go to the folder named "Apps", then to the folder "App". Open the Terminal from this directory and run the code:
streamlit run 1_main.py

## Make sure you are connected to the internet when running the file, and when any kind of error message is given, kindly close the current browser tab and run it again.
## Please set the device display theme to Light Mode for better visibility of text on the page
## Any errors that occur are just because of network issues because we used APIs for the models, so for any errors encountered, for instance, a list index out of range error, or any other error, please close the page for the game and run the code again
## Deployment
Can run on any pc with stable internet connection and camera.
## Applications
Entertainment

Story Generation

Comic generation assistance

Assistance in image generation
## Further Improvements
Text-to_speech for great story-telling.

Supporting visual images for interesting stories.
## Demo Video
Yotube link
