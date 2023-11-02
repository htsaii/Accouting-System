from datetime import datetime
from order import db


class Order(db.Model):
    """
    # self.customer :
    # self.items : 
    """
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), nullable=False)
    num_item = db.Column(db.String(200), nullable=False)
    item = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False, default=datetime.utcnow().strftime('%Y-%m-%d'))
    # order_date = db.Column(db.DateTime, default=datetime.utcnow)
    