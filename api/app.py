import time

from flask import Flask
from flask import request
from models import AI_inference
from jinja2 import FileSystemLoader,Environment
import argparse
import json

#parser = argparse.ArgumentParser()
#parser.add_argument("--test", default=False, type=bool, help="if testings, will print out more hint")
#args = parser.parse_args()
#istest = int(args.test)
istest=True

loader_ = FileSystemLoader(searchpath="api/templates")
loader = Environment(loader=loader_)

aii = AI_inference()

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    index_temp = loader.get_template("index.html")
    return index_temp.render()

@app.route('/api/',methods=['GET','POST'])
def api():
	event = json.loads(request.data)
	if istest:
		print("[Event Data]:",event, flush  = True)
	result = aii.inference(event)
	return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020, debug=True)
