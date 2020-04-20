def fake_predict(user_age):
    if user_age > 10:
        prediction = "Přežil (více než 10 let)"
    else:
        prediction = "Super survived (méně než 10 let)"
    return prediction
