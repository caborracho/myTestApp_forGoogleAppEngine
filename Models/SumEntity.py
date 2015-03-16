from google.appengine.ext import db
from Models.StudientEntity import Studient

class Sum(db.Model):
	"""docstring for Sum"""
	n1 = db.IntegerProperty(required=True)
	n2 = db.IntegerProperty(required=True)
	result = db.IntegerProperty()
	studient_id = db.IntegerProperty(required=True)

	


class SumEntity(object):
	"""docstring for SumEntity"""
	def __init__(self,studient_id, n1=0, n2=0, result=0):
		"""n1, n2, result shoud be integers. 
			studient should be the ID of a Studient"""
		self.entity = Sum(n1=n1, n2=n2, result=result, studient_id=studient_id)

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
		return [SumEntity(0,_sum.n1,_sum.n2, _sum.result) for _sum in Sum.all()] #Lista por comprension

	@staticmethod
	def getAllofStudient(studient_id):
		q = Sum.all()
		q.filter("studient_id =",studient_id)
		return [SumEntity(studient_id,_sum.n1,_sum.n2, _sum.result) for _sum in q.run()]
		
