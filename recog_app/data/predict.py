from tensorflow import keras
from keras_preprocessing import image
import numpy as np

IMG_PATH = "C:/Users/TeunH/Documents/Universiteit/BIT/Module 6/HCI/Project/Test/apple/Eigen2.jpeg"

classes = ['apple', 'banana', 'carrot', 'cucumber', 'other', 'paprika', 'potato', 'tomato']

model = keras.models.load_model('./test.h5')

def create_ordered_lists(predictions):
    ordered_classes = classes.copy()
    ordered_predictions = predictions.copy()

    for i in range(len(classes)):
        prob = predictions[i]
        for x in range(i+1, len(classes)-i):
            tempPred = ordered_predictions[x]
            tempClass = ordered_classes[x]
            if(prob < tempPred):
                ordered_predictions[x] = predictions[i]
                ordered_classes[x] = ordered_classes[i]
                ordered_predictions[i] = tempPred
                ordered_classes[i] = tempClass

    return ordered_classes, ordered_predictions

def get_max(predictions):
    max = np.max(predictions)
    classList = predictions.tolist()
    index = classList.index(max)
    most_likely_class = classes[index]

    return [most_likely_class, max]

# Returns a list of 
# [0]: List of predictions (only numbers corresponding with the variable classes) [0.2, 0.5, ..., 0.15]
# [1]: List of predicted class (index 0) and the probability (index 1)  ['Cucumber', 0.95]
# [2]: List of ordered classes and there probabilities [['Cucumber', ..., 'Other'], [0.8, ..., 0.0]]
def predict(img_path):
    img = image.load_img(img_path, target_size=(250, 250))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    predictions = model.predict(images)[0]

    max = get_max(predictions)
    ordered_classes, ordered_predictions = create_ordered_lists(predictions)
    ordered_list = [ordered_classes, ordered_predictions]

    return predictions, max, ordered_list

if __name__ == '__main__':
    predictions, max, ordered_list = predict(IMG_PATH)

    if(max[1] == 1):
        print(max[0])
        print(f'{ordered_list[1][0]:.2%}')
        # Return most_likely_class                      (Will return a string with the name of the category)
    else:
        print(max[0])
        print(f'{ordered_list[1][0]:.2%}')
        # return dict                                   
