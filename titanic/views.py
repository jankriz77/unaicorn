from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, "index.html")

def result(request):
    user_input_pclass = int(request.GET["pclass"])
    user_input_sex = int(request.GET["sex"])
    user_input_age = int(request.GET["age"])
    user_input_sibsp = int(request.GET["sibsp"])
    user_input_parch = int(request.GET["parch"])
    user_input_fare = int(request.GET["fare"])
    user_input_embarked = int(request.GET["embarked"])
    user_input_title = int(request.GET["title"])
    titanic_prediction = ml_predict.prediction_model(user_input_pclass, user_input_sex, user_input_age, user_input_sibsp, user_input_parch, user_input_fare, user_input_embarked, user_input_title)
    # user_input_age += " let. Dobrá predikce!"
    # age_prediction = fake_model.fake_predict(user_input_age)
    return render(request, "result.html", {"klic_pro_result_html": titanic_prediction})
