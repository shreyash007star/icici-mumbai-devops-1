from fastapi import FastAPI
app=FastAPI()

@app.get("/home")
def welcomeMessage():
    return {"message": "welcome to icici airlines"}

@app.get("/login")
def loginApp():
    return {"message": "welcome to login page"}

