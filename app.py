from flask import Flask, render_template, jsonify

app = Flask(__name__)

ITEMS = [{
  'id': 1,
  'title': 'ToorDal',
  'price': '120',
  'Weight': '1kg'
}, {
  'id': 2,
  'title': 'MoongDal',
  'price': '80',
  'Weight': '1kg'
}, {
  'id': 3,
  'title': 'Cashew',
  'price': '400',
  'Weight': '500g'
}, {
  'id': 4,
  'title': 'Almond',
  'price': '330',
  'Weight': '500g'
}]


@app.route("/")
def hello_people():
  return render_template('home.html', items=ITEMS)


@app.route("/api/items")
def list_items():
  return jsonify(ITEMS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
