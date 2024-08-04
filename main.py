from flask import Flask
import random
app = Flask(__name__)

facts_list=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos.", 
            "Según un estudio realizado en 2018, más del 50 por ciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
            "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
            "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
            "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
            "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]






@app.route("/")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/so")
def foto():
    return"<h1>La fotosintesis es el proceso químico que se produce en las plantas, las algas y algunos tipos de bacterias cuando se exponen a la luz del sol.<h1>"

@app.route("/si")
def meta():
    return"<h1>La metamorfosis es el proceso de cambios estructurales y fisiológicos a través de los cuales ciertos animales alcanzan la vida adulta, dejando atrás las características obtenidas desde su nacimiento<h1>"

@app.route("/no")
def ciclo():
    return"<h1>El ciclo del agua es el proceso de circulación del agua en el planeta Tierra. Durante este ciclo, el agua sufre desplazamientos y transformaciones físicas , y atraviesa los tres estados de la materia: líquido, sólido y gaseoso.<h1>"




app.run(debug=True)