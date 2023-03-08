from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.cqki075.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index_main.html')


@app.route('/detail')
def detail():
    mglist = db.mglist.find_one({'shop': '맛집'}, {'_id': False})
    print(mglist)
    return render_template('index_detail.html')


@app.route("/sik", methods=["GET"])
def mglist_get():
    sikdangs_list = list(db.mglist.find({}, {'_id': False}))
    return jsonify({'mglist': sikdangs_list})


@app.route("/detail/<id>", methods=["GET"])
def detail_get(id):
    mglist = db.mglist.find_one({'shop': id}, {'_id': False})
    reviews = list(db.reviewlist.find({'shop':id},{'_id':False}))
    print(mglist, reviews)
    return render_template('index_detail.html', data=mglist, data1=reviews)
    # return jsonify({'result': mglist})


@app.route("/save", methods=["POST"])
def mglist_add():
    image_receive = request.form['image_give']
    shop_receive = request.form['shop_give']
    menu_receive = request.form['menu_give']
    place_receive = request.form['place_give']
    star_receive = request.form['star_give']

    doc = {
        'image': image_receive,
        'shop': shop_receive,
        'menu': menu_receive,
        'place': place_receive,
        'star': star_receive
    }
    db.mglist.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


@app.route("/saveReview", methods=["POST"])
def reviewlist_add():
    userID_receive = request.form['userID_give']
    Txt_review_receive = request.form['Txt_review_give']
    StarPoint_review_receive = request.form['StarPoint_review_give']
    shop_receive = request.form['shop_give']

    doc = {
        'userID': userID_receive,
        'Txt_review': Txt_review_receive,
        'StarPoint_review': StarPoint_review_receive,
        'shop': shop_receive
    }
    db.reviewlist.insert_one(doc)

    return jsonify({'msg': '저장완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)