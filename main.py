import pandas as pd
import numpy as np
import plotly.express as px
from google.colab import drive
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("./dataset/transactions.csv")

type = data["type"].value_counts()
transactions = type.index
quantity = type.values

figure = px.pie(
                values=quantity,
                names=transactions,
                title="Distribution of Transaction Type"
                )
figure.show()

data['type'] = data['type'].map({"CASH_OUT": 1, 
                                "PAYMENT": 2, 
                                "CASH_IN": 3, 
                                "TRANSFER": 4, 
                                "DEBIT": 5})
data["isFraud"] = data["isFraud"].map({0: "No Fraud", 1: "Fraud"})

x = np.array(data[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig']])
y = np.array(data['isFraud'])

model = DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
model.fit(x_train, y_train)
print(model.score(x_test, y_test))

features = np.array([[1, 2806.0,2806.0,0.0]])
print(model.predict(features))
