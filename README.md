# Bizbox-blinkDetection


Phase2-Blink_Detection  
│
├── Training
│     ├── Model                       <- Contains various models trained now or in future (Stores model after every epoch and separetely for best epoch too
│     │    └── ResNet                    After training is completed for various architectures, best model then can be used for testing
│     ├── dataset                     <- Contains code for processing Input data before initializing model training
│     └── Model                       <- Contains code for initialzing model as per user input
│
└── Testing
      ├── Model                       <- Contains various models trained now or in future
      │    └── ResNet                 <- Contains ResNet Model (.h5 file)
      ├── Sample_input                <- Sample folder, just to show input directory architecture
      │    └── Closed                     and type of files it contains
      │    └── Open
      ├── Input_data                  <- Empty directory initialized where user can add test images
      │    └── Closed
      │    └── Open         
      ├── Output_data                 <- Empty directory initailized which contains testing output on successful execution of testing code
      └── src                         <- Contains training and test code used for classification task


**Note: This is the initial phase of the Repo, designed for Classification stage of Blink-Detection, the strucure is subject to change once Classification pipeline
Integrated with other pipelines (Face Detection and Eye Localization)



# Instruction To Run Test Code

1. Download ResNet trained model (Model trained on UnityEyes dataset on AWS EC2 instance), model can be downloaded from here: LINK
2. Save model file to location: Phase2-Blink_Detection > Model > Resnet 
3. Add test images to Input_data folder.
Note - Please add test files as per intruction given below:
3.1 Seggregate closed and open eye images
3.2 Add closed eye images to: Phase2-Blink_Detection > Input_data > Closed 
3.3 Add open eye images to: Phase2-Blink_Detection > Input_data > Open
** Please test model on cropped images from actual image containing eyes only, as this stage accepts eye images data as input 

4. Create a virtual enviornment to install libraries related to **Blink_detection**
    - Run `python3 -m venv <name of virtual env>`
    - linux: Run source `<name of virtual env>/bin/activate`
    - windows: Run `<name of virtual env>\env\Scripts\activate.bat`

5. Run `pip install -r requirements.txt`
6. Run `python src\p2_blink_classification_testing.py <Path to Input Image Directory> <Path to output Directory> <Path to ResNet Model>`
Example: python src\p2_blink_classification_testing.py Input_data/ Output_data/ Model/ResNet/

On successful execution of above command, Output files will be created in output directory


# Instruction To Run training Code 

1. Download UnityEyes Dataset from here : LINK
2. Unzip downloaded file
3. Create a virtual enviornment to install libraries related to **Blink_detection**
    - Run `python3 -m venv <name of virtual env>`
    - linux: Run source `<name of virtual env>/bin/activate`
    - windows: Run `<name of virtual env>\env\Scripts\activate.bat`

4. Run `pip install -r requirements.txt`
5. Run `python src\train_model.py <Backbone-name> <Path to Directory to save model> <Path to Input Directory>
Example: python src\train_model.py resnet Model/ResNet/ Input/

On Successful execution of above command, Selected model(DenseNet, ResNet, MobileNet) will get saved in directory to save model




