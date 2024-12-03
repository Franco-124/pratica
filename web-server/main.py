import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def contact_page():
    return """
    <h1>hola soy una pagina de contacto</h1>
    <p>soy un parrafo</p>
    """

# Llamada a store.get_category() en alguna ruta o al iniciar el servidor si es necesario
@app.get('/category')
def get_category():
    store.get_category()
    return {"message": "Categoría obtenida"}

# FastAPI no necesita la función run(), puedes iniciar el servidor con uvicorn