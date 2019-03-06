import requests, re

postURL = 'https://graph.facebook.com/{0}/feed/?message={1}&access_token={2}'

class Utility:
    #Opens parameters.txt
    def openParams(openType):
        try:
            params = open("parameters.txt", str(openType))
            return params
        except IOError:
            print("File 'parameters.txt' could not be found in current directory.")
            return None

    #Stores values of parameters.txt 
    def getParams(parameterFile):
        if(parameterFile != None):
            parameters = {}
            for line in parameterFile:
                line = line.split('=')
                parameters[str(line[0])] = re.search("'(.*)'", line[1]).group(1)
        return parameters

    #Creates parameters.txt
    def createFile():
        file = open("parameters.txt", "w+")
        file.write("access_token=''\npage_id=''\nmessage=''")
        print("parameters.txt created.")

    #Makes a post request to facebook
    def makePost(accessToken, pageID, postMessage):
        r = requests.post(postURL.format(pageID, postMessage.replace(' ', '+'), accessToken))
        print(r.json())

class Post:
    def fromFile():
        params = Utility.getParams(Utility.openParams("r"))
        Utility.makePost(params["access_token"], params["page_id"], params["message"])

    def custom(accessToken, pageID, postMessage):
        Utility.makePost(str(accessToken), str(pageID), str(postMessage))

    def withMessage(message):
        params = Utility.getParams(Utility.openParams("r"))
        Utility.makePost(params["access_token"], params["page_id"], str(message))

def __init__():
    Utility.createFile()

__init__()
