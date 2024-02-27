import pandas as pd
import numpy as np
import pickle
# from sklearn.preprocessing import StandardScaler
# import xgboost as xgb

blank_df = pd.read_csv("blank_df/blank_df.csv")
blank_df.iloc[:, 1:] = 0

all_blank_df = pd.read_csv("blank_df/all_blank_df.csv")

def encoding(spent, age, gender, interest1, interest2):
    data_dict = {
        'spent': [spent],
        f'age_{age}': [1], 
        f'gender_{gender}': [1],
        f'int1_{interest1}': [1],
        f'int2_{interest2}': [1]
    }
    new_row = pd.DataFrame(data_dict)
    new_df = pd.concat([blank_df, new_row], ignore_index=True)
    new_df = new_df.fillna(0)
    return new_df

def all_encoding(spent, interest1, interest2):
    data_dict = {
        f'int1_{interest1}': 1,
        f'int2_{interest2}': 1
    }
    new_df = all_blank_df
    new_df["spent"] = spent
    for key, value in data_dict.items():
        new_df[key] = value

    return new_df


def total_reg_predict(X):
    if "spent_log" in X.columns:
        X.drop(columns=["spent_log"], inplace=True)
    try:
        with open('models/ad_scaler.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        with open('models/total_xgb_model.pkl', 'rb') as model_file:
                model = pickle.load(model_file)
    except FileNotFoundError:
        return "Error: Model files not found."

    try:
        X_scaled = scaler.transform(X)

    except AttributeError:
        return "Error: Scaler object is missing transform method."

    pred = model.predict(X_scaled)

    if pred is not None:
        return pred.tolist()
    else:
        return "Failed to make prediction."

def app_reg_predict(X):
    if "spent_log" in X.columns:
        X.drop(columns=["spent_log"], inplace=True)
    try:
        with open('models/ad_scaler.pkl', 'rb') as scaler_file:
                scaler = pickle.load(scaler_file)
        with open('models/approved_xgb_model.pkl', 'rb') as model_file:
                model = pickle.load(model_file)
    except FileNotFoundError:
        return "Error: Model files not found."
    
    try:
        X_scaled = scaler.transform(X)
    except AttributeError:
        return "Error: Scaler object is missing transform method."

    pred = model.predict(X_scaled)
    if pred is not None:
        return pred.tolist()
    else:
        return "Failed to make prediction."


def class_predict(X):
    try:
        with open('models/class_SVM_model.pkl', 'rb') as model_file:
                model = pickle.load(model_file)
    except FileNotFoundError:
        print("Error: Model files not found.")
        return None
    
    X["spent_log"] = np.log1p(X["spent"])
    last = X.pop('spent_log')
    X.insert(0, 'spent_log', last)
    X = X.drop(["spent"], axis=1)
    pred = model.predict_proba(X)[:, 1]

    if pred is not None:
        return pred.tolist()
    else:
        return "Failed to make prediction."