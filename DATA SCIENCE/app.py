from turtle import right
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)

model=pickle.load(open("Linear.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["POST"])
def predict():
    wei=int(request.form.get("weight"))
    
    prediction=model.predict(([[wei]]))
    return render_template("index.html",predi="Your height is {}".format(prediction[0]))
    

if __name__ == '__main__':
    app.run(debug=True)



