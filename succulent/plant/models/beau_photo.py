from plant.extensions import db


class Beauti_essay(db.Model):
    __tablename__='beauti_essay'
    id = db.Column(db.Integer, primary_key=True)
    #简介
    intro=db.Column(db.String(1000))

    # 添加关联外键，‘表名.字段’
    uid = db.Column(db.Integer, db.ForeignKey('users.id'))

    # 关联晒美图的图片一对多关系
    image = db.relationship('Beau_image', backref='beau_essay', lazy='dynamic')


class Beau_image(db.Model):
    __tablename__ = 'beau_image'
    id = db.Column(db.Integer, primary_key=True)

    url=db.Column(db.Text)

    #关联晒美图一对多外键
    beau_photo = db.Column(db.Integer, db.ForeignKey('beauti_essay.id'))

