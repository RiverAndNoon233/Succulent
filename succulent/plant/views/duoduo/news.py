# coding: utf-8
from plant.models.news import News, News_image, News_comment
from plant.models.users import User
from flask import Blueprint, request, jsonify, session
from plant.extensions import db


index = Blueprint('index', __name__)
# 新聞列表


@index.route('/news/')
def news():
    page = request.args.get('page', 1, int)
    paginates = News.query.order_by(News.timestamp).paginate(
        page, per_page=8, error_out=False)
    pages = paginates.pages
    news_list = paginates.items
    data = []
    for news in news_list:
        count = news.comment.count()
        dic = {
            "id": news.id,
            "title": news.title,
            "urlimage": news.images.first().img,
            "timestamp": news.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            "count": count, }
        print(news.images.first().img)
        data.append(dic)

    return jsonify({"code": 1, "msg": "success", "data": data, 'pages': pages, 'page': page})

# 新聞詳情


@index.route('/news_detail/', methods=['GET', 'POST'])
def news_detail():
    nid = request.get_json(True).get('nid')
    # nid = request.json.get('nid')

    print(nid)
    if nid is None:
        return jsonify({'code': 0, 'msg': 404})
    news = News.query.get(nid)
    if news is None:
        return jsonify({'code': 0, 'msg': 404})
    news.count += 1
    try:
        db.session.add(news)
    except:
        pass
    imgs = news.images.all()
    img_list = []
    if len(list(imgs)) >= 1:
        for img in imgs:
            img_list.append(img.img)

    return jsonify({
        'code': '1',
        'news_data': {
            'nid': news.id,
            'title': news.title,
            'view_num': news.count,
            'comment_num': news.comment.count(),
            'time': news.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'news': news.content,
            'img': img_list,
        }})

# 評論列表


@index.route('/comment', methods=['GET', 'POST'])
def comment():
    nid = request.get_json(True).get('nid')
    if nid is None:
        return jsonify({'code': 0, 'msg': 404})
    news = News.query.get(nid)
    if news is None:
        return jsonify({'code': 0, 'msg': 404})
    comments = news.comment.all()
    data = []
    for i in comments:
        user = i.user
        dic = {
            "user_id": user.id,
            "user_name": user.nickname,
            "user_icon": user.image,
            "comment_time": i.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            "comment": i.context,
            "comment_id": i.id,
        }
        data.append(dic)
    return jsonify({"code": 1, 'data': data})

# 添加評論


@index.route('news_talk', methods=['GET', 'POST'])
def news_talk():
    try:
        uid = session.get('session_id')
        nid = request.get_json(True).get('nid')
        context = request.get_json(True).get('context')
        # 查询得到具体用户
        user = User.query.get(uid)
        # 查詢到新聞
        news = News.query.get(nid)
        # 执行保存操作：
        comment = News_comment()
        comment.context = context
        comment.user = user
        comment.c_news = news
        db.session.add(comment)
    except:
        return jsonify({'code': 0, 'msg': '评论发表失敗'})

    return jsonify({'code': 1, 'msg': '评论发表成功'})


# 上傳文章
@index.route('/push_news', methods=['GET', 'POST'])
def push_news():

    title = request.get_json(True).get('titlt')

    content = request.get_json(True).get('content')
    print('----------------------------------------')
    try:
        images = request.json.get('images')
    except:
        images = None
    news = News()
    news.title = title
    news.content = content
    try:
        db.session.add(news)
    except:
        return {'code': 0, "msg": "标题已经存在"}

    try:
        # 如果图片不为空，则执行存储操作
        if images:
            for one_image in images:
                img = News_image()
                img.img = one_image
                img.newsid = news
                db.session.add(img)
        return {'code': 1, 'msg': 'success'}
    except:
        return {'code': 0, 'msg': 'failed'}
