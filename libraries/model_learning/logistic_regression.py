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
        self.X = []
        # y = zero-dimensional binary representation of users way of usage (delete / keep)
        self.y = pd.Series()

        # instantiate variables for object-scope
        self.fig = self.ax = self.cnf_matrix = None
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.y_pred = None
        # print("init: " + str((self.y, self.X, self.y_pred,self.X_train,self.X_test,self.X_train,self.X_test)))

    def create_X(self, n=10000):
        """This method creates a Pandas DataFrame representing n number of pictures
         with categories as headlines"""

        # Create dummy data representation of image files
        self.X = pd.DataFrame(np.random.random(size=(n, 10)),
                              columns=self.categories)

        #print(self.X.tail)
        return self.X

    # def create_Y(self):
    #     """
    #     This method creates a Pandas DataFrame X and Y columns
    #     with categories as headlines
    #
    #     y can be created either as the last column and separated with
    #     """
    #     print("is this even visible?")
    #
    #
    #
    #     # Does it work?
    #     print(type(self.y))
    #     print(self.y)
    #     print(self.X)
    #     yield self.X, self.y

    def create_answers(self): # TODO: does not work½½½
        """
        This is a dummy data creator based on the contents of X dataframe

        y[0] == file.delete()
        """

        # additional possible categories for y[index] = True
        # and random_array[index][2] == 1 and random_array[index][3] < 0.3

        print('first_print')
        print(self.y.tail)

        # for index, answer in enumerate(self.y):
        #     if self.X[index][0] < 0.2:
        #         self.y[index] = 1
        #     else:
        #         self.y[index] = 0
        print(self.X['is_blurry'])
        for row in (self.X.loc[self.X['is_blurry'] > 0.7]):
            self.y[row].append(1)
        else:
            self.y[row].append(0)

        #self.y = self.X.loc[self.X['is_blurry'] < 0.2]
        print('visible?')
        print(self.y.tail)

    def split_data(self): # TODO: not imlemented
        # split X and y data training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.25, random_state=16)

    def run_log_reg(self): # TODO: not implemented
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

    def create_heatmap(self): # TODO: not implemented
        """Heatmap displays a visual representation of accuracy"""
        sns.heatmap(pd.DataFrame(
            self.cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
        self.ax.xaxis.set_label_position("top")
        plt.tight_layout()
        plt.title('Confusion matrix', y=1.1)
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')

# model = ModelTraining()
# model.create_X()
# model.create_answers()