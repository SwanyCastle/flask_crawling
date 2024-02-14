from flask import Blueprint, render_template, request, jsonify, redirect, url_for

from app.models import Data, FirmData

from datetime import datetime

from app.crawl import crawling_data
from app.setting_db import db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def search():
    page = request.args.get('page', type=int, default=1)

    firm_select = request.args.get('trading_firm_select')   
    start_date = request.args.get('s_date')
    end_date = request.args.get('e_date')

    if not firm_select:
        crawled_datas = Data.query.order_by(Data.close_date.desc())
    elif firm_select == 'KB증권': 
        crawled_datas = Data.query.filter((Data.trading_firm.like(f'%{firm_select}%')) | Data.trading_firm.like('%케이비%')).order_by(Data.close_date.desc())
    elif firm_select == 'IBK투자증권':
        crawled_datas == Data.query.filter((Data.trading_firm.like(f'%{firm_select}%')) | Data.trading_firm.like('%아이비케이%')).order_by(Data.close_date.desc())
    else:
        crawled_datas = Data.query.filter(Data.trading_firm.like(f'%{firm_select}%')).order_by(Data.close_date.desc())

    if start_date or end_date:
        if not start_date:
            pass
        elif not end_date:
            pass
        else:
            pass

    crawled_datas = crawled_datas.paginate(page=page, per_page=15)
    firm_datas = FirmData.query.all()
    return render_template(
        "stocks/crawldata_list.html", 
        crawled_datas=crawled_datas,
        firm_data=firm_datas,
        firm_select=firm_select,
        start_date=start_date,
        end_date=end_date,
        date_time=datetime.now()
    )

@bp.route('/update')
def update():
    crawling_data()
    last_update = Data.query.order_by(Data.crawled_datetime.desc()).first()
    return jsonify({ "last_update": last_update.crawled_datetime.strftime('%Y-%m-%d | %H:%M:%S') })

@bp.route('/delete')
def delete():
    chk_rows = request.args.getlist('chk_rows[]')
    print(chk_rows)
    for i in chk_rows:
        if i.isdigit():
            print(i, type(i))
            row = Data.query.get_or_404(i)
            db.session.delete(row)
    db.session.commit()
    return redirect(url_for('main.search'))