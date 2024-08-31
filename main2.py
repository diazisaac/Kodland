# Importar
from flask import Flask, render_template,request, redirect
# Importando la biblioteca de bases de datos
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creación de una base de datos
db = SQLAlchemy(app )

#Asignación #1. Crear una tabla de base de datos

class Data(db.Model):

    #identificador
    id = db.Column(db.Integer, primary_key=True) 
    #titulo 
    name = db.Column(db.String(100), nullable = False)
    #subtitulo
    last_name = db.Column(db.String(100), nullable = False)
    #texto
    city= db.Column(db.Text, nullable = False)

    #salida
    def _repr_(self):
        return f"<Data{self.id}>"









# Ejecutar la página con contenido
@app.route('/')
def index():
    # Visualización de los objetos de la DB
    # Asignación #2. Mostrar los objetos de la DB en index.html
    cards = Data.query.order_by(Data.id).all()
    

    return render_template('index.html',cards=cards)

# Ejecutar la página con la tarjeta
@app.route('/card/<int:id>')
def card(id):
    # Asignación #2. Mostrar la tarjeta correcta por su id
    card = Data.query.get(id)#extraer datos tabla
    

    return render_template('card.html', card=card)

# Ejecutar la página y crear la tarjeta
@app.route('/create')
def create():
    return render_template('create_card.html')

# El formulario de la tarjeta
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        name =  request.form['name']
        last_name =  request.form['last_name']
        city =  request.form['city']

        # Asignación #2. Crear una forma de almacenar datos en la DB
        card = Data(name=name, last_name=last_name, city=city)

        db.session.add(card)
        db.session.commit()
        




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
