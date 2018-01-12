# dino-ai
Self learning bot to play chrome's offline dino game

## Progress
### 6th Jan, 2017
* Setup selenium on python to interact with chrome
* Basic interactions like key press and screenshot
* Went through an [NN / Genetic algo primer](https://www.youtube.com/watch?v=P7XHzqZjXQs) used to solve the same problem
* Some more brainstorming

### 12th Jan, 2017
* Installed tesseract-ocr, pytesseract, opencv-python and castro
* Tried to read score using tesseract but it is broken at the moment. It reads 3 as 5. And 81 as -> HI 0008] 00081 (high score is lighter and thus is causing issues)
* Got the sprites used by the game instead of manually taking screenshots to get the font. Planning to train tesseract on it.
* Bug: `temp/image-manip.log` contains experiments aimed to see how tesseract handles all characters. It is not reading anything at the moment. (possibly due to low distance between characters?)
* Next steps: Either fix Tesseract or look at template matching tools. Can also ignore for now and focus on the other parts of the pipeline.

## Thinking aloud

* **(DONE)** _Selenium could be used to programmatically interact with the game using Python_
* Use some OCR package to read score? Or manually get all characters (0 to 9) and use template matching?
* Game over detection - how? (OCR / template matching with restart button?)
* Screenshot sampling frequency as a hyperparam (but will require retraining?)
* Consider video recording instead of screenshots? ([castro](https://pypi.python.org/pypi/castro/) for python)
* Totally unsupervised so should not think of labelling obstacles? Or should we do some feature engineering to bootstrap the process?
* Read about RL, Q learning, genetic algos
* CNN (image to feature vec) + LSTM (feature vec to actions - up, down, none) -> What is our objective func? how to use the raw score?
* What would be a good logging scheme? (time, final score)
* Ideal setup for training would be pausable and allow continuing. Pause on next loss + reload prev model and state while continuing.
* Think of creative ways to visualize progress. Will make it easier to compare performance across hyperparameters.
* Spend some time deciding how to structure the code base so that the same setup could be used across different learning strategies.
* What will happen when the colour changes? Temporarily, should we restrict it to a single colour scheme for training?
    * `Runner.prototype.invert = function() {};` can be used to override the invert colour functionality
* Tracking progress via Github page with GIFs for the repo instead of updating this markdown?