from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.cqki075.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/example", methods=["POST"])
def mars_post():
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']

    doc = {
        'title':title_receive,
        'text':text_receive
        }
    db.mglist.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

@app.route("/example", methods=["GET"])
def mars_get():
    list_data = list(db.mglist.find({},{'_id':False}))
    return jsonify({'result':list_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)