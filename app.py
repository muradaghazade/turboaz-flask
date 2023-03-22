from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(500), nullable=True)
    price = db.Column(db.String(500), nullable = True)
    model = db.Column(db.String(500), nullable = True)

    def __init__(self, marka, price,model ):
        self.marka = marka
        self.price = price
        self.model = model


@app.route("/add-car", methods = ['GET', 'POST'])
def addcar():
    if request.method == "GET":
        return render_template('addcar.html')
    else:
        marka = request.form['marka']
        model = request.form['model']
        price = request.form['price']
        new_text = Car(marka, model,price)
        db.session.add(new_text)
        db.session.commit()
        return render_template('addcar.html')


@app.route("/cars")
def cars():
    cars = Car.query.all()
    return render_template('masin.html', cars=cars)



 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
 