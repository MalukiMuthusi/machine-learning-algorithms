import pandas
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# a snippet of the data
pima = pandas.read_csv('pimadiabetes.data.txt', delimiter=' ')
pima.columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Class"]
print(pima.head)
print(pima.info())
print(pima.describe())

X = pima.drop("Class", axis=1)
y = pima["Class"]

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=67)
print(x_train.shape)

nb = GaussianNB()

nb.fit(X=x_train, y=y_train)
predictions = nb.predict(x_test)


print(confusion_matrix(y_test, predictions))
print('n')
print(classification_report(y_test, predictions))
