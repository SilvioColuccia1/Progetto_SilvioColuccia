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

df_tweet_input.loc[(df_tweet_input[TARGET_COLUMN] != 1),TARGET_COLUMN] = 0
df_tweet_input.loc[(df_tweet_input[TARGET_COLUMN] == 1),TARGET_COLUMN] = 1 #useless in this case

vct = CountVectorizer()

X = df_tweet_input['text']
y = df_tweet_input[TARGET_COLUMN]


X = vct.fit_transform(X)

filename = 'finalized_countvectorizer.sav'
dump(vct, filename)

print("Preprocessing phase finished...")


print("Dataset division finished...")
clf =  SVC(kernel="linear")

print("Fitting the model...")

clf.fit(X,y)

print("Model training finished...")

y_pred = cross_val_predict(clf, X, y, cv=5)

print("ACCURACY_SCORE_IRONY: ",accuracy_score(y,y_pred))

prec, recall, f, support = precision_recall_fscore_support(y,y_pred)
print("PRECISION_IRONY: {}, RECALL_IRONY: {}, F-beta score_IRONY: {}, SUPPORT_IRONY: {}".format(prec,recall,f,support))


dump(clf, 'irony_model.joblib') 


titles_options = [("Confusion matrix, without normalization[IRONY]", None),
                  ("Normalized confusion matrix[IRONY]", 'true')]

for title, normalize in titles_options:
    disp = skplt.metrics.plot_confusion_matrix(y,y_pred, cmap='plasma' )
    disp.set_title(title)

plt.show()
