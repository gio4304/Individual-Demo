# Facial Recognition
Overview

In this project we are using Google's Teachable Machine to train an AI model to recognize basic facial emotions. To do this, we turned on the webcam and recorded a bunch of images of ourselves making different faces, like happy, sad, angry, and neutral. Each emotion is its own category, and we added lots of examples for each one. We also tried to change things like our angle and lighting so the AI doesn’t just memorize one exact picture, but actually learns what each emotion generally looks like on a face.

# Hardware Requirements

| Component                  | Specification / Details | Notes                          |
|---------------------------|--------------------------|---------------------------------|
| Potentiometer             | 10kΩ                     | Used for LCD contrast control   |
| Mega 2560 Controller Board| Any revision             | Main microcontroller board      |
| LCD 1602 Module           | Standard, HD44780        | Text display (16×2 characters)  |
| USB Cable                 | USB-A to USB-B           | Connects Mega 2560 to computer  |
| Breadboard                | 830 tie-points           | Circuit prototyping platform    |
| Jumper Wires (14)         | Male-to-male             | For wiring connections          |


# Software Requirements
| Software / Tool          | Version                 | Purpose / Description                               |
|--------------------------|-------------------------|------------------------------------------------------|
| Python                   | 3.11                    | Used for data processing, scripts, and integration   |
| Arduino IDE              | Latest Version          | Uploads code and manages the Mega 2560 board         |
| Google Teachable Machine | Latest Version          | Trains the facial-emotion recognition AI model       |
| Visual Studio            | Latest Version          | Development environment for coding and debugging     |


# Hidden / Easily Overlooked Details
1.Pip installation 

2.Camera angles and lighting was very important for the Teachable Machine to recognize facial emotions

3.Loose wiring on the Arduino board could cause a malfunction

4.Serial communication from Arduino and Python could cause an overflow in the serial buffer

5.USB port not supplying enough power 

# Diagram
1.Goggle Teachable

2.Arduino Mega 2560

3.Python script

4.LED indicator screen

5.Webcam

# Demo Video


# Licensce
MIT License
