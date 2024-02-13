from flask import Blueprint, render_template, redirect, url_for, request

from app.models import Data, FirmData

from datetime import datetime

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def crawl_list():
    page = request.args.get('page', type=int, default=1)
    crawled_datas = Data.query.order_by(Data.close_date.desc())
    crawled_datas = crawled_datas.paginate(page=page, per_page=15)
    firm_datas = FirmData.query.all()
    return render_template(
        "stocks/crawldata_list.html", 
        crawled_datas=crawled_datas,
        firm_data=firm_datas,
        date_time=datetime.now()
    )
