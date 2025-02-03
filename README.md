# Classifier Project

Welcome to the Classifier Project! This project aims to develop a machine learning classifier to categorize data into predefined classes.

## Project Structure

- `backend/` - Backend code for the project.
- `dataset/` - Directory containing the dataset.
  - `hotdog/` - Directory containing images of hotdogs.
  - `not_hotdog/` - Directory containing images of non-hotdogs.
- `frontend/` - Frontend code for the project.
- `model/` - Saved models and checkpoints.
- `scripts/` - Scripts for data preprocessing and other tasks.
  - `preprocess.py` - Script for preprocessing the dataset.
- `README.md` - Project documentation.

## Project Breakdown

### Training the model

#### Preprocessing

The `preprocess.py` script is responsible for preprocessing the dataset. It performs the following steps:

1. **Load the image**: Reads the image from the given path using OpenCV.
2. **Resize the image**: Resizes the image to 224x224 pixels.
3. **Normalize the image**: Normalizes the pixel values to the range [0, 1].
4. **Preprocess the dataset**: Iterates through the dataset directory, preprocesses each image, and stores the preprocessed images and their labels in numpy arrays.
5. **Save the preprocessed data**: Saves the preprocessed images and labels as `data.npy` and `labels.npy` respectively.

To run the preprocessing script, execute the following command:

```bash
python scripts/preprocess.py