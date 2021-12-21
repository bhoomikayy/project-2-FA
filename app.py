#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('C:\\Users\\bhoom\\Desktop\\model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run(port = 8080, debug=True)


# In[ ]:




