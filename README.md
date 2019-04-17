README.md

# API docker for pytorch

```
git clone https://github.com/raynardj/pytorch_api
```

### Run docker

The repository is contructed based on docker compose
```
cd pytorch_api
docker-compose build
docker-compose up
```

### Test api

* You can visit ```http://192.168.99.100:8833/``` for testing purposes.

* The default password is ```jupyter```

* Visit ```http://192.168.99.100:8833/notebooks/notebooks/test.ipynb``` to test the API

### Put in the model

Before you change anything, the [models.py file](api/models.py) looks like following:
```python
import torch
from flask import jsonify

class AI_inference:
	def __init__(self,*args,**kwargs):
		# initialize model here
		return None

	def inference(self,event):
		"""
		event: post/get request json data, a dictionary
		"""
		x = self.preprocess(event)
		result = {"a":"b"} 
		return jsonify(result)

	def preprocess(self,x):
		# preprocess the data here
		return 
		
```

You can put in your model by rewrite the functions in ```AI_inference```

The variable ```event``` will be the data dictionary you put in on the ```post/get``` request