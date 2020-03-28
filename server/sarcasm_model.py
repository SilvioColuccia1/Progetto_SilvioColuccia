__author__ = 'silvio'
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import dump, load
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
import scikitplot as skplt

TARGET_COLUMN = 'id_annotazione'


df_tweet_input = pd.read_csv('tweet.csv',sep='|')

print("Shape: ",df_tweet_input.shape)

df_tweet_input.loc[(df_tweet_input[TARGET_COLUMN] != 2),TARGET_COLUMN] = 0
df_tweet_input.loc[(df_tweet_input[TARGET_COLUMN] == 2),TARGET_COLUMN] = 1 #useless in this case

df_tweet_input=df_tweet_input.drop(df_tweet_input.query('id_annotazione == 0').sample(frac=.5).index)
print("Shape: ",df_tweet_input.shape)

vct = CountVectorizer()

X = df_tweet_input['text']
y = df_tweet_input[TARGET_COLUMN]


X = vct.fit_transform(X)

filename = 'finalized_countvectorizersarcasm.sav'
dump(vct, filename)

print("Preprocessing phase finished...")

print("Dataset division finished...")
clf =  SVC(kernel="linear")

print("Fitting the model...")
clf.fit(X,y)

print("Model training finished...")

dump(clf, 'sarcasm_model.joblib') 

titles_options = [("Confusion matrix, without normalization[SARCASM]", None),
                  ("Normalized confusion matrix[SARCASM]", 'true')]

for title, normalize in titles_options:
    disp = skplt.metrics.plot_confusion_matrix(y,y_pred, cmap='plasma')
    disp.set_title(title)

plt.show()
