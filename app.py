from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.cqki075.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index_main.html')

@app.route('/detailpage')
def detail():
    return render_template('index_detail.html')

@app.route("/save", methods=["POST"])
def mglist_add():
    img_receive = request.form['image_give']
    shop_receive = request.form['shop_give']
    place_receive = request.form['place_give']
    menu_receive = request.form['menu_give']
    star_receive = request.form['star_give']

    doc = {
        'imgurl':img_receive,
        'shop':shop_receive,
        'place':place_receive,
        'menu':menu_receive,
        'star':star_receive
        }
    db.mglist.insert_one(doc)

    return jsonify({'msg':'저장완료!'})

# @app.route("/example", methods=["POST"])
# def mars_post():
#     title_receive = request.form['title_give']
#     text_receive = request.form['text_give']

#     doc = {
#         'title':title_receive,
#         'text':text_receive
#         }
#     db.mglist.insert_one(doc)

#     return jsonify({'msg':'저장완료!'})

# @app.route("/example", methods=["GET"])
# def mars_get():
#     list_data = list(db.mglist.find({},{'_id':False}))
#     return jsonify({'result':list_data})

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)