from fastapi import FastAPI

app =  FastAPI()

#endpoint
@app.get("/") #ruta raiz
def inicio():
    return {"mensaje": "Hola estoy aprendiendo FASTAPI"}