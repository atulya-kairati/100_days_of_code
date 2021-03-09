from random import choice
import sqlalchemy
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
API_KEY = '1234567890'


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    @classmethod
    def make_cafe_from_dict(cls, cafe_dict):
        return cls(
            has_sockets=cafe_dict['has_sockets'] in ('true', 'True'),
            has_toilet=cafe_dict['has_toilet'] in ('true', 'True'),
            can_take_calls=cafe_dict['can_take_calls'] in ('true', 'True'),
            has_wifi=cafe_dict['has_wifi'] in ('true', 'True'),
            location=cafe_dict['location'],
            img_url=cafe_dict['img_url'],
            name=cafe_dict['name'],
            seats=cafe_dict['seats'],
            map_url=cafe_dict['map_url'],
            coffee_price=cafe_dict['coffee_price'],
        )

    def get_dict(self):
        cafe_dict = self.__dict__
        # print(cafe_dict)
        del cafe_dict['_sa_instance_state']
        return cafe_dict


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_cafe():
    r_cafe = choice(db.session.query(Cafe).all())
    return jsonify({'cafe': r_cafe.get_dict()})


@app.route('/all')
def all_cafe():
    all_cafe_objs = db.session.query(Cafe).all()
    all_cafe_list = [cafe_obj.get_dict() for cafe_obj in all_cafe_objs]
    # print(all_cafe_list)
    return jsonify({"cafes": all_cafe_list})


@app.route('/search')
def search_cafe():
    loc = request.args.get('loc')
    cafe_objs = Cafe.query.filter(Cafe.location.ilike(loc)).all()
    if len(cafe_objs) == 0:
        return jsonify({'error': 'No cafe found there.'})
    cafe_list = [cafe_obj.get_dict() for cafe_obj in cafe_objs]
    return jsonify({'cafes': cafe_list})


@app.route('/add', methods=['POST'])
def add_cafe():
    data = dict(request.form)
    # print(type(request.form.get('has_wifi')))
    req_keys = sorted(['has_sockets', 'has_toilet', 'location', 'img_url', 'name', 'can_take_calls', 'has_wifi', 'seats',
            'map_url', 'coffee_price'])
    keys_given = sorted(data.keys())
    # print(keys_given)
    # print(req_keys)
    if keys_given != req_keys:
        return jsonify({"error": "required data not provided", "data_required": req_keys})

    new_cafe = Cafe.make_cafe_from_dict(cafe_dict=request.form)
    # print(new_cafe.get_dict())
    try:
        db.session.add(new_cafe)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return jsonify({'status': 'failed', 'reason': 'Cafe with same name already exists'})
    return jsonify({'status': "success", "recorded": data})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_cafe_price(cafe_id):
    new_price = request.args.get('new_price')
    print(new_price)
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify({'status': 'failed', "reason": f'no cafe found with id: {cafe_id}'}), 404
    print(cafe)
    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify({'status': 'success'}), 200


@app.route('/delete/<int:cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    if request.args.get('apikey') is None or request.args.get('apikey') != API_KEY:
        return {'status': 'failed', 'reason': 'you are not authorized'}
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return jsonify({'status': 'failed', "reason": f'no cafe found with id: {cafe_id}'}), 404
    print(cafe)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({'status': 'success'}), 200


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
