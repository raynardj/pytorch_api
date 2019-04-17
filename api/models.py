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

		