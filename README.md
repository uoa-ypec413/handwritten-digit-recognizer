
# Handwritten Digit Recognizer

**Team 23**

***Yulia Pechorina, Keith Anderson***

This is a program developed as a part of the COMPSYS 302 course at the University of Auckland.

It enables the user to train different AI models and then use them to recognise digits which they can draw inside of the software.

---
## Dependencies:

- Python 3.8
- PyTorch
- Torchvision
- PyQt5
- NumPy
- MatPlotLib

---
## Instructions:

1.  Install dependencies
2.  Run 'main.py'
3.  Selecting a model:
    - On launch the program creates a new Adjusted LeNet-5 model, the recommended network type. You can use this straight away without doing anything.
    - To create a new model, click File>New Model and select a model type
    - To select an existing model, click Load Model and navigate to the existing model
4. Training the current model:
    - Click File>Train Model
    - Click "Download MNIST"
    - Once download has been completed, click "Train"
    - At any point during training you can click "Cancel" to stop training
    - Training will finish after 25 epochs
    - You can choose to begin a further 25 epochs of training if you'd like
5. Viewing the datasets:
    - Download the MNIST database, instructions in step 4.
    - In the main window, click View>View *DATASET* Images, where *DATASET* is your desired dataset.
    - Navigate through the dataset by scrolling through the image grid, and changing page.
6. Testing the model:
    - Once a model has been trained (or even before!), you can return the the main window and draw a number on the blank canvas
    - When you're happy with your number, click "Recognise" and the current model will predict the number that you have drawn. You can also see what it thinks the relative probabilities of each digit are.
    - Click "Clear" to erase the canvas.
    - Click "Model" to select a different model.
7. Saving the model:
    - In the main window, select File>Save Model

---
## Changelog:
|Date|Version|Description| 
|--|--|--|
|1/05/21|V1.0.0|Finishing touches, commenting fixes. Complete and stable version of code.|
|29/04/21|V0.4.0|Rename most files, change from camelCase to snake_case where possible|
|28/04/21|V0.3.1|Add pre-trained models|
|27/04/21|V0.3.0|Change coding structure for better MVC compliance, object oriented coding practices, clean up code, fix minor bugs, improve Adjusted LeNet-5 model with drop-out layer.|
|26/04/21|V0.2.2|Increase Epoch count per training cycle|
|23/04/21|V0.2.1|Small bug fixes|
|22/04/21|V0.2.0|Functionality improvements for Main Window, Dataset Viewer, and AI|
|21/04/21|V0.1.0|First Version of Program with Main Window, Dataset Viewer, and Training Window functional|
|18/04/21|UI-1.1.0|Improve modularity of UI code|
|18/04/21|UI-1.0.0|Add widgets to main window, complete initial UI|
|17/04/21|UI-0.4.0|Add widgets to viewer window|
|17/04/21|UI-0.3.0|Add widgets to training window|
|17/04/21|AI-1.0.1|Add a more descriptive header|
|17/04/21|AI-1.0.0|Basic implementation of AI|
|16/04/21|UI-0.2.0|Add basic elements to main and training windows|
|16/04/21|UI-0.1.0|Create program windows|

