from flask import Flask
import numpy as np
import tensorflow as tf
app = Flask(__name__)

@app.route("/")
def hello():
	a = np.array([1,2,3,4,5])
	return str(a)

if __name__ == "__main__":
    app.run()
