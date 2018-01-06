# dino-ai
Self learning bot to play chrome's offline dino game

## Progress
### 6th Jan, 2017
* Setup selenium on python to interact with chrome
* Basic interactions like key press and screenshot
* Went through a [NN / Genetic algo primer](https://www.youtube.com/watch?v=P7XHzqZjXQs) used to solve the same problem

## Thinking aloud

* Use some OCR package to read score?
* Game over detection - how? (OCR / template matching with restart button?)
* Screenshot sampling frequency as a hyperparam (but will require retraining?)
* Consider video recording instead of screenshots?
* Totally unsupervised so should not think of labelling obstacles
* Read about RL, Q learning, genetic algos
* CNN (image to feature vec) + LSTM (feature vec to actions - up, down, none) -> What is our objective func?