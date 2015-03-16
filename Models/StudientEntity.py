from google.appengine.ext import db
import SumEntity

class Studient(db.Model):
	"""docstring for Sum"""
	name = db.StringProperty()
	email = db.EmailProperty()


class StudientEntity(db.Model):
	def __init__(self, mystudient,name="no_name_setted"):
		if type(mystudient) is Studient:
			self.entity = mystudient
		else:
			self.entity = Studient(name=name,email=mystudient)
		

	def getName(self):
		return self.entity.name

	def store(self):
		self.entity.put()

	def getKey(self):
		return self.entity.key()

	def getID(self):
		return self.entity.key().id()


	def getAllSums(self):
		#q = Sum.all()
		#q.filter("studient_id =",self.getID())
		return SumEntity.SumEntity.getAllofStudient(self.getID()) #q.run()



	@staticmethod
	def getStudientByName(name="test"):
		"""name should be a string"""

		myStudients = Studient.all()
		myStudients.filter("name =", name)

		std = myStudients.get()

		finalStudient = None

		if std:
			finalStudient = StudientEntity(std)

		return finalStudient
	