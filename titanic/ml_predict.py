def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    # následující pořadí sloujpců dataframe musí odopovídat tomu, jak to v modelu titanic_model.sav
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open("titanic/data/titanic/titanic_model.sav","rb"))
    prediction = randomforest.predict(x)
    if prediction == 0:
        return "Na základě zadaných dat by osoba nejspíš NEPŘEŽILA."
    elif prediction == 1:
        return "Na základě zadaných dat by osoba nejspíš PŘEŽILA."
    return prediction
