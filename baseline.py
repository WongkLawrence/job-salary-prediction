import csv
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier

#this data contains columns with very large strings.
#limit to break this
csv.field_size_limit(1000000000)

def load_data(fname):
  with open(fname, 'r') as csvfile:
    return list( csv.reader(csvfile, delimiter=',', quotechar='"'))
    

data = load_data('../../../Documents/data-job-salary/Train_rev1.csv')


print (data[1])
'''
train_as_text = [' '.join(sample['ingredients']).lower() for sample in train]
train_cuisine = [sample['cuisine'] for sample in train]

test_as_text = [' '.join(sample['ingredients']).lower() for sample in test]

tfidf_enc = TfidfVectorizer(binary=True)
lbl_enc = LabelEncoder()

X = tfidf_enc.fit_transform(train_as_text)
X = X.astype('float16')

X_test = tfidf_enc.transform(test_as_text)
X_test = X_test.astype('float16')

y = lbl_enc.fit_transform(train_cuisine)


clf = SVC(C=100, kernel='rbf', degree=3,
  gamma=1, coef0=1, shrinking=True, 
  probability=False, tol=0.001, cache_size=200,
  class_weight=None, verbose=True, max_iter=-1,
  decision_function_shape=None, random_state=None)

model = OneVsRestClassifier(clf, n_jobs=4)
model.fit(X,y)


y_test = model.predict(X_test)
test_cuisine = lbl_enc.inverse_transform(y_test)


test_id = [sample['id'] for sample in test]

submission_df = pd.DataFrame({'id': test_id, 'cuisine': test_cuisine}, columns=['id', 'cuisine'])
submission_df.to_csv('./svm_submission.csv', index=False)
'''



