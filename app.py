from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
  {
    'id':1,
    'name':'ToorDal',
    'price':'120',
    'Weight':'1kg'
  },
  {
    'id':1,
    'name':'Almond',
    'price':'330',
    'Weight':'500g'
  },
{
    'id':1,
    'name':'Peanuts',
    'price':'100',
    'Weight':'1kg'
  },
  {
    'id':1,
    'name':'MoongDal',
    'price':'80',
    'Weight':'1kg'
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', items=ITEMS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
