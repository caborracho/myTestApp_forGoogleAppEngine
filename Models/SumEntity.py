from google.appengine.ext import db


class Sum(db.Model):
	"""docstring for Sum"""
	n1 = db.IntegerProperty(required=True)
	n2 = db.IntegerProperty(required=True)
	result = db.IntegerProperty()

	


class SumEntity(object):
	"""docstring for SumEntity"""
	def __init__(self, n1=0, n2=0, result=0):
		self.entity = Sum(n1=n1, n2=n2, result=result)

	def getN1(self):
		return self.entity.n1

	def getN2(self):
		return self.entity.n2

	def getResult(self):
		return self.entity.result

	
	def store(self):
		self.entity.put()



	@staticmethod
	def getAll():
		return [SumEntity(_sum.n1,_sum.n2, _sum.result) for _sum in Sum.all()] #Lista por comprension
		
