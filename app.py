from flask import Flask,jsonify ,request,render_template
import numpy as np
import joblib
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords

# Import lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import mysql.connector

nltk.download('stopwords')
nltk.download('wordnet')

stemmmer = PorterStemmer()
lemmitizer = WordNetLemmatizer()
stop_words= set(stopwords.words('english'))

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'IC_1854@c',
    'database': 'test',
}


app = Flask(__name__)

tfidf_model=joblib.load("IMDB_review_tfidf.pkl")
ML_Model = joblib.load("IMDB_review.pkl")

def text_cleaner(text):
    sent = re.sub('[^a-zA-Z]',' ',text)
    sent = sent.lower()
    sent = " ".join([stemmmer.stem(word) for word in str(sent).split()])
    sent = " ".join([word for word in str(sent).split()
                    if(word not in stop_words)])
    return sent

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict',methods=["POST"])
def predict():
    if request.method == 'POST':
        
        review = request.form['review']
        review_copy=str(review)
        print(review_copy)

        print("Before Cleanning :- ",review)

        cleaned_news = text_cleaner(review)
        print("After Cleanning :- ",cleaned_news)
        

        pred = ML_Model.predict(tfidf_model.transform([cleaned_news]))[0]
        try:
            connection = mysql.connector.connect(**db_config)
            if connection.is_connected():
                print('Connected to the database')
                cursor = connection.cursor()
                insert_query = "INSERT INTO review_table (review, sentiment) VALUES (%s, %s)"
                data_to_insert = (review_copy, pred)
                cursor.execute(insert_query, data_to_insert)
                connection.commit()
        except mysql.connector.Error as e:
            print(f'Error: {e}')
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
                print('Connection closed')

        
        result= " {}".format(pred)
    return jsonify({"review result is ": result,"review is ":review_copy})

if __name__ =='__main__':
	app.run(debug=True)