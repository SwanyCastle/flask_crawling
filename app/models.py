from app.setting_db import db

class Data(db.Model):
    __tablename__ = "stock_data"

    stock_id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(100), unique=True)
    open_date = db.Column(db.DateTime)
    close_date = db.Column(db.DateTime)
    fixed_price = db.Column(db.Integer)
    min_hprice = db.Column(db.Integer)
    max_hprice = db.Column(db.Integer)
    trading_firm = db.Column(db.Text)
    crawled_datetime = db.Column(db.DateTime)

class FirmData(db.Model):
    __tablename__ = "firm_data"

    firm_id = db.Column(db.Integer, primary_key=True)
    firm_name = db.Column(db.String(30))
    firm_link = db.Column(db.String(100))