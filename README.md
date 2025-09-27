# 🕵️ Fraud Detection Demo with Machine Learning  

This is a fun little project that shows how you can use **machine learning** to detect fraudulent transactions in a dataset.  
We’ll look at the data, visualize it with charts, train a simple model, and even try predicting if a new transaction is fraud or not.  

---

## 🎯 What this project does
- Loads a dataset of transactions (`transactions.csv`)  
- Shows what types of transactions exist with a nice pie chart  
- Trains a simple machine learning model to tell **Fraud** vs **Not Fraud**  
- Lets you test the model with your own data  

---

## 📊 Step 1: See the data  
The code first checks the **types of transactions** in the dataset and shows a pie chart.  
You’ll see how much of the data is **Cash Out, Payment, Transfer, etc.**  

---

## 🤖 Step 2: Train the model  
We give the model some information about each transaction, like:  
- Transaction type (cash out, transfer, etc.)  
- Amount  
- Balance before the transaction  
- Balance after the transaction  

The model then learns patterns that help it decide if something looks suspicious.  

---

## 🧪 Step 3: Test it out  
After training, we test the model with part of the data it hasn’t seen before.  
It gives us a **score** that shows how good it is at spotting fraud.  

---

## 🔮 Step 4: Try a prediction  
We can ask the model: *“Here’s a transaction, is it fraud?”*  
