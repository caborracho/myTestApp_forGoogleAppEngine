from google.appengine.api import users
from Models.StudientEntity import StudientEntity as Studient




def loadUser(reuqest,returnURI = "/"):
	"""Tries to get the name of loggued user
		If it is not loggued, it makes it logguin first,
		then returns the name of loggued user

		returnURI should be a string containing the redicect URI
		to use in case there is no loggued user"""

	user =  users.get_current_user()
	userName = "Anonym"

	if user:
		userName = __trimNameFromMail__(user.nickname())
		myStudient = Studient.getStudientByName(userName)
		if not myStudient:
			myNewStudient = Studient(user.email(),userName)
			myNewStudient.store()
			myNewStudient.store()
	else:
		reuqest.redirect(users.create_login_url(returnURI))

		
	return userName

def getStudient(reuqest):
	userName = loadUser(reuqest)
	myStudient = Studient.getStudientByName(userName)
	return myStudient


def __trimNameFromMail__(nickName):
	userName = nickName
	if "@" in userName:
		userName = userName[:nickName.find("@")]
	return userName
	