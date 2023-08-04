from app import app

# La aplicación se ejecuta desde este archivo. Importa la instancia de Flask y la ejecuta.
if __name__ == "__main__":
    app.run(debug=True)  #debug=True habilita el modo de debugging, proporcionando mensajes de error detallados en el navegador cuando algo 
sale mal.
