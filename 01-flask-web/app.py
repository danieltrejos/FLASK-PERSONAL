# App web usando flak-bootstrap

from flask import Flask, render_template, redirect,request,flash,url_for

app = Flask(__name__)
app.secret_key = 'secret_key' # Necesario para mostrar mensajes en flask

proveedores= []  # Simular Base de datos en memoria como una lista de diccionarios


# !Index
@app.route("/")
def index():
    return render_template('index.html')

# !Crear Proveedor
@app.route("/proveedor", methods=["GET", "POST"])
def create_proveedor():
    if request.method == "POST":
        
        primer_nombre = request.form.get("primer_nombre")
        segundo_nombre = request.form.get("segundo_nombre")
        primer_apellido = request.form.get("primer_apelido")
        segundo_apellido = request.form.get("segundo_apellido")
        tipo_persona = request.form.get("tipo_persona")
        num_documento = request.form.get("num_documento")
        email = request.form.get("email")

        # Crear un diccionario con el nuevo proveedor
        nuevo_proveedor = {
            "primer_nombre": primer_nombre,
            "segundo_nombre": segundo_nombre,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "tipo_persona": tipo_persona,
            "num_documento": num_documento,
            "email": email,
        }

        # Añadir nuevo proveedor a la lista (BD)
        proveedores.append(nuevo_proveedor)

        # Mostrar mensaje
        flash("Proveedor creado correctamente")
        return redirect(url_for("create_proveedor"))
        
    

    return render_template('crear_proveedor.html')

#!Listar Proveedores
@app.route("/listar_proveedor")
def list_proveedor():
    return render_template('listar_proveedor.html', proveedores=proveedores)



if __name__ == "__main__":
    app.run(debug = True)



