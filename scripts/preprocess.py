import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

IMG_SIZE = 224
BATCH_SIZE = 32
DATASET_DIR = "dataset"

datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    # share_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

flow_from_directory = datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

print(flow_from_directory.class_indices)
# Output: {'hotdog': 0, 'not_hotdog': 1}
