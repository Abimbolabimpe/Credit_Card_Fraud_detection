# An Advanced Machine Learning-Based System for Detecting Credit Card Fraud

This repository contains data and scripts used to build three machine learning models for the project titled "An Advanced Machine Learning-Based System for Detecting Credit Card Fraud".

The dataset used in this project was made public on Kaggle and UCI data repository, <https://www.kaggle.com/competitions/ieee-fraud-detection/data>. The dataset contains 590,540 credit card transactions, of which 20, 663 are fraudulent. The data is divided into two files identity and transaction. 

The scripts in this repository can be used to load the data, clean the data, and train several machine learning models. The models that are included in this repository are:

- Naïve Bayes 
- Random Forest
- Logistic Regression

The scripts also include code to evaluate the performance of the models.

The data and scripts in this repository can be used to build and evaluate new machine learning models for fraud detection.

# Getting Started

To get started with this project, you will need to have the following software installed:

- Python 3
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn

Once you have installed the necessary software, you can clone this repository and run the main.py script. This script will load the data, clean the data, and train the machine learning models.

# Results

We compared the performance of three machine learning models on a classification task. The random forest classifier achieved the best performance, with an accuracy of 98%. The Naïve Bayes model also performed well, with an accuracy of 96%. However, the logistic regression model performed the worst, with an accuracy of only 67%. The best model was saved locally using the pickle library in Python. The model was then deployed using Streamlit, a popular open-source Python library for building interactive web applications for data science and machine learning projects. The model deployed is ready to make predictions on a new dataset. Streamlit deployment interface 

# Conclusion

The results of this project show that machine learning can be used to detect credit card fraud. The models that were trained in this project achieved an accuracy of 98%.

The data and scripts in this repository can be used to build and evaluate new machine learning models for fraud detection.

