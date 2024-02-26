import joblib
import learn
def find(name):
    model=joblib.load("ML_MODEL")
    lis=learn.Learn(name)
    return model.predict(lis)[0]