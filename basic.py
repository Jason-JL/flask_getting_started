from flask import Flask, jsonify, request
import numpy as np
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"


@app.route("/data", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Suyash",
    "team": "instructor"
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well


@app.route("/sum", methods=["POST"])
def sum():
  """
  Returns the sum of post two numbers
  """
  r = request.get_json() # parses the POST request body as JSON
  s = r["a"] + r["b"] # adds JSON dict parameter "a" and "b" together
  return s, 200


@app.route("/name", methods=["GET"])
def getName():
  """
  Return the data dictionary of below to the caller as JSON 
  """
  data = {
          "name": "Jason"
  }
  return jsonify(data)


@app.route("/hello/<name>", methods=["GET"])
def sayhello(name):
  """
  Returns the data dictionary of below to the caller as JSON
  """
  data = {
          "message": "Hello there, {}".format(name) 
  }
  return jsonify(data)


@app.route("/distance", methods=["POST"])
def getDistance():
  """
  Returns the cartesian distance between the points a and b in the following form as JSON:
  """
  content = request.get_json()
  a = content['a']
  b = content['b']
  distance = np.sqrt(np.power(a[0]-b[0], 2) + np.power(a[1]-b[1],2))
  data = {
    "distance": distance,
    "a": [2, 4],
    "b": [5, 6]
  }
  return jsonify(data)



