from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
from joblib import dump, load
import numpy as np


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/callmodel/", methods=['GET'])
@cross_origin()
def predict_api():
  print("Received REQUEST")
  input_string = request.args.get('input_string')
  

  polarity = request.args.get('polarity') == 'true'
  irony = request.args.get('irony') == 'true'
  sarcasm = request.args.get('sarcasm') == 'true'
  subjectivity = request.args.get('subjectivity') == 'true'
  print("REQUEST: input_string: {}, polarity: {}, irony: {}, sarcasm: {}, subjectivity: {}".format(input_string,polarity,irony,sarcasm,subjectivity))
  
  #TODO: here I will call the model to make a classification
  
  clf_positivepolarity = load('positiveoverallpolarity_model.joblib')
  clf_negativepolarity = load('negativeoverallpolarity_model.joblib')
  clf_subjectivity = load('subjectivity_model.joblib')
  clf_irony = load('irony_model.joblib') 
  clf_sarcasm = load('sarcasm_model.joblib') 
  vctirony = load("finalized_countvectorizer.sav")
  vctsarcasm = load("finalized_countvectorizersarcasm.sav")
  vctsubjectivity = load("finalized_countvectorizersubjectivity.sav") 
  vctpositivepolarity = load("finalized_countvectorizerpositiveoverallpolarity.sav") 
  vctnegativepolarity = load("finalized_countvectorizernegativeoverallpolarity.sav") 

  response = ""
  if irony == True:
    print("INPUTSTRING: ",str(input_string))
    vectorized_string = vctirony.transform([str(input_string)])
    positive_probability_irony = clf_irony.predict(vectorized_string) #TODO: call predictproba after generated another model with proba = True
    response += str({'Irony':positive_probability_irony[0]})
    print("RESPONSE not json: ",positive_probability_irony)
 
    
  if sarcasm == True:
    print("INPUTSTRING: ",str(input_string))
    vectorized_string = vctsarcasm.transform([str(input_string)])
    vectorized_stringirony = vctirony.transform([str(input_string)])
    positive_probability_sarcasm = clf_sarcasm.predict(vectorized_string) #TODO: call predictproba after generated another model with proba = True
    positive_probability_irony = clf_irony.predict(vectorized_stringirony)
    if positive_probability_sarcasm[0] == 1 & positive_probability_irony[0] == 1:
      response += str({'Sarcasm':positive_probability_sarcasm[0]})  
    elif positive_probability_sarcasm[0] == 1 & positive_probability_irony[0] == 0:
      response += str({'Sarcasm':positive_probability_irony[0]})
    elif positive_probability_sarcasm[0] == 0:
      response += str({'Sarcasm':positive_probability_sarcasm[0]})
    print("RESPONSE not json: ",positive_probability_sarcasm)

  if polarity :
    print("INPUTSTRING: ",str(input_string))
    vectorized_stringpositivepolarity = vctpositivepolarity.transform([str(input_string)])
    vectorized_stringnegativepolarity = vctnegativepolarity.transform([str(input_string)])
    vectorized_stringsubjectivity = vctsubjectivity.transform([str(input_string)])
    positive_probability_polarity = clf_positivepolarity.predict(vectorized_stringpositivepolarity) #TODO: call predictproba after generated another model with proba = True
    negative_probability_polarity = clf_negativepolarity.predict(vectorized_stringnegativepolarity)
    positive_probability_subjectivity = clf_subjectivity.predict(vectorized_stringsubjectivity)
    if positive_probability_subjectivity[0] == 1:   
      if positive_probability_polarity[0] == 1 & negative_probability_polarity == 1:
        response += str({'Polarity: Mixed'})  
      elif positive_probability_polarity[0] == 1 & negative_probability_polarity == 0:
        response += str({'Polarity: Positive'})
      elif positive_probability_polarity[0] == 0 & negative_probability_polarity == 1:
        response += str({'Polarity: Negative'})
      elif positive_probability_polarity[0] == 0 & negative_probability_polarity == 0:
        response += str({'Polarity: Neutral'})
    else:
        response += str({'Polarity: Neutral'})
    
    print("RESPONSE not json: ",positive_probability_polarity)

  if subjectivity :
    print("INPUTSTRING: ",str(input_string))
    vectorized_string = vctsubjectivity.transform([str(input_string)])
    positive_probability_subjectivity = clf_subjectivity.predict(vectorized_string) #TODO: call predictproba after generated another model with proba = True
    response += str({'Subjectivity':positive_probability_subjectivity[0]})
    print("RESPONSE not json: ",positive_probability_subjectivity)

  print("RESPONSE: {}".format(jsonify(response)))
  return jsonify(response)

if __name__ == '__main__':
    app.run()
