# Loading required Libraries


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import warnings

warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
% matplotlib
inline

# Loading Feature Vectors

df = pd.read_excel("df_train_Betti_1.xlsx")
df = df.drop(df.columns[[0]], axis=1)

# Slicing Data
x = df.iloc[:, :100].values
y = df.iloc[:, 100].values

# #Spliting the data in 80:20 training to testing
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Applying Machine learning models from Scikit-learn

# XGBoost Classifier

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

modelx = XGBClassifier(base_score=0.5, use_label_encoder=True, eval_metric='mlogloss')

modelx.fit(x_train, y_train)

from sklearn import metrics

metrics.plot_roc_curve(modelx, x_test, y_test)
plt.show()

y_predx = modelx.predict(x_test)

print("XGboost model accuracy(in %):", accuracy_score(y_test, y_predx) * 100)

cm = confusion_matrix(y_test, y_predx)

print("Confusion Matrix : \n", cm)
plot_confusion_matrix(modelx, x_test, y_test, cmap='Blues')
plt.grid(False)
from sklearn.metrics import classification_report

print(classification_report(y_test, y_predx, digits=4))



#######################################################################################


# kNN classifier

# Chosing Best K
from sklearn.neighbors import KNeighborsClassifier
error_rate = []

for i in range(1,130):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    error_rate.append(np.mean(pred != y_test))

plt.figure(figsize=(15,10))
plt.plot(range(1,130),error_rate, marker='o', markersize=9)

# k = 30 is the best
knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(x_train, y_train)

from sklearn import metrics

metrics.plot_roc_curve(knn, x_test, y_test)
plt.show()
pred_knn = knn.predict(x_test)

print("KNN where k = 3 model accuracy(in %):", accuracy_score(y_test, pred_knn) * 100)

cm = confusion_matrix(y_test, pred_knn)

print("Confusion Matrix : \n", cm)
plot_confusion_matrix(knn, x_test, y_test, cmap='Blues')
plt.grid(False)
print(classification_report(y_test,pred_knn, digits = 4))

#############################################################################



# Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix

model_1 = RandomForestClassifier(n_estimators=300, criterion='entropy',
                                 min_samples_split=10, random_state=0)

# fitting the model on the train data
model_1.fit(x_train, y_train)

from sklearn import metrics

metrics.plot_roc_curve(model_1, x_test, y_test)
plt.show()

predictions = model_1.predict(x_test)
print("Random forest model accuracy(in %):", accuracy_score(y_test, predictions) * 100)

cm = confusion_matrix(y_test, predictions)

print("Confusion Matrix : \n", cm)
plot_confusion_matrix(model_1, x_test, y_test, cmap='Blues')
plt.grid(False)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions, digits=4))
