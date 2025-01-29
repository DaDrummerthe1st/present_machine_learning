#%%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

class ModelTraining:
    def __init__(self):
        # Categories array
        self.categories = [ # each category represent the ML-answer from as many separate models
                        'is_blurry',
                        'has_identified_objects',
                        'contains_common_identified_objects',
                        'contains_text',
                        'has_exif_data',
                        'is_created_at_time_near_neighbor_file',
                        'is_created_geographically_close_to_neighbor_file',
                        'seems_like_screenshot',
                        'seems_very_dark',
                        'seems_very_light']
        # X = media represented by pandas Dataframe
        self.X = None
        # y = zero-dimensional binary representation of users way of usage (delete / keep)
        self.y = None

        # instantiate variables for object-scope
        self.fig = self.ax = self.cnf_matrix = None
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.y_pred = None

    def create_X_and_Y(self):
        """
        This method createss a pandas DataFrame X and Y columns
        with categories as headlines

        y can be created either as the last column and separated with
        """
        # Create dummy data representation of image files
        self.X = pd.DataFrame(np.random.random(size=(10000, 10)),
                              columns=self.categories)

        # create an answer array (y)
        self.y = pd.Series((np.ndarray((10000,))), dtype='int8')

        # Does it work?
        print(self.y)
        print(self.X)

    def create_answers(self):
        """
        This is a dummy data creator based on the contents of X dataframe

        y[0] == file.delete()
        """

        # additional possible categories for y[index] = True
        # and random_array[index][2] == 1 and random_array[index][3] < 0.3

        for index, answer in enumerate(y):
            if self.X[index][0] < 0.2:
                self.y[index] = 1
            else:
                self.y[index] = 0

    def split_data(self):
        # split X and y data training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.25, random_state=16)

    def run_log_reg(self):
        """Running my first ever logistic regression"""
        logreg = LogisticRegression(random_state=16)
        logreg.fit(self.X_train, self.y_train)
        self.y_pred = logreg.predict(self.X_test)
        print(self.y_pred)
        self.cnf_matrix = metrics.confusion_matrix(self.y_test, self.y_pred)
        print(self.cnf_matrix)

        class_names=['Delete','Keep'] # name  of classes
        self.fig, self.ax = plt.subplots()
        tick_marks = np.arange(len(class_names))
        plt.xticks(tick_marks, class_names)
        plt.yticks(tick_marks, class_names)

    def create_heatmap(self):
        """Heatmap displays a visual representation of accuracy"""
        sns.heatmap(pd.DataFrame(
            self.cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
        self.ax.xaxis.set_label_position("top")
        plt.tight_layout()
        plt.title('Confusion matrix', y=1.1)
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')