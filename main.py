from fastapi import FastAPI
from pydantic import BaseModel
from app import encoding, total_reg_predict, app_reg_predict, class_predict, all_encoding

app = FastAPI()

class item(BaseModel):
    spent: float
    age: str
    gender: str
    interest1: str
    interest2: str
    task: str
    audience: str

@app.get("/")
async def main_endpoint():
    return {"Facebook Ad Conversion Prediction" : "by Pattarachai Phothong"}

@app.post("/predict")
async def model_enpoint(item:item):
    # initialize inputs
    spent = item.spent
    age = item.age
    gender = item.gender
    interest1 = item.interest1
    interest2 = item.interest2
    task = item.task
    audience = item.audience

    # input setting based on audience
    if audience == "all":
        X = all_encoding(spent, interest1, interest2)
    else:
        X = encoding(spent, age, gender, interest1, interest2)
    
    # Prediction based on task
    if task == "total":
        pred = total_reg_predict(X)
    elif task == "approved":
        pred = app_reg_predict(X)
    elif task == "classification":
        pred = class_predict(X)
    
    if audience == "all":
        pred_result = {
            "male": {
                "30-34" : pred[0],
                "35-39" : pred[1],
                "40-44" : pred[2],
                "45-49" : pred[3]
            },
            "female" : {
                "30-34" : pred[4],
                "35-39" : pred[5],
                "40-44" : pred[6],
                "45-49" : pred[7]
            },
            "all" : pred
        }
    else:
        pred_result = {"Prediction": pred[0]}
    
    return pred_result

if __name__ == "__main__":
    app.run(debug=True)