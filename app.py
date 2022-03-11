from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "w57h63ff9"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()



@app.route("/")
def root():
    return render_template("home.html", form=AddCupcakeForm())


@app.route("/api/cupcakes")
def get_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    data = request.json
    new_cupcake = Cupcake(flavor=data["flavor"], size=data["size"], rating=data["rating"], image=data["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Cupcake deleted sucessfully")
