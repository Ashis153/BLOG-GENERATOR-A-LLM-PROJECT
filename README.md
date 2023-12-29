THIS IS A SIGN-LANGUAGE-RECOGNITION-SYSTEM USING CNN.
Sign Language is a form of communication used primarily by people hard of hearing or deaf. This type of gesture-based language allows people to convey ideas and thoughts easily overcoming the barriers caused by difficulties from hearing issues.
Many large training datasets for Sign Language are available on Kaggle, a popular resource for data science. The one used in this model is called “Sign Language MNIST” 
The first step of preparing the data for training is to convert and shape all of the pixel data from the dataset into images so they can be read by the algorithm.
The next step is to create the data generator to randomly implement changes to the data, increasing the amount of training examples and making the images more realistic by adding noise and transformations to different instances
Notice the initialization of the algorithm with the adding of variables such as the Conv2D model, and the condensing to 24 features. We also use batching techniques to allow the CNN to handle the data more efficiently.
Finally, defining the loss functions and metrics along with fitting the model to the data will create our Sign Language Recognition system. 
