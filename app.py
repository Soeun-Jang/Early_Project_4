from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.cqki075.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index_main.html')

@app.route('/detail')
def detail():
    return render_template('index_detail.html')

@app.route("/save", methods=["POST"])
def mglist_add():
    image_receive = request.form['image_give']
    shop_receive = request.form['shop_give']
    place_receive = request.form['place_give']
    menu_receive = request.form['menu_give']
    star_receive = request.form['star_give']

    doc = {
        'image':image_receive,
        'shop':shop_receive,
        'place':place_receive,
        'menu':menu_receive,
        'star':star_receive
        }
    db.mglist.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)