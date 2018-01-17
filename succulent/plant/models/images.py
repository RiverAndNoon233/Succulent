from plant.extensions import db


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    url=db.Column(db.Text)

    #关联文章一对多外键
    posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
