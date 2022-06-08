import eng_to_ipa as p
from flask import Flask
app = Flask(__name__)

@app.route('/test')
def index():
   print('Request for test received')
   return "Name Phonetics Service is UP"

@app.route('/name/<empName>',methods=['GET'])
def getEmpPhonetics(empName):
    print('Request to get Phonetics of name=%s' % empName)
    return p.convert(empName)

if __name__ == '__main__':
   app.run()