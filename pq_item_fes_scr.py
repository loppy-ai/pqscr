import schedule
import time
import datetime
import requests
from bs4 import BeautifulSoup
import csv

def job():
    # 現在時刻取得
    now = datetime.datetime.now()
    d = now.day
    h = now.hour
    m = now.minute

    # ランキング取得
    target_url = 'http://tapi.puyoquest.jp/html/person_ranking_sp_item_festival/?campaign_id=2091&uid=6e1869180134199eea1999ccb07a45ea'
    target_html = requests.get(target_url)
    soup = BeautifulSoup(target_html.content, "html.parser")
    result = soup.find_all("p")

    # 文字列取得
    fn = (str(result[25])[21:])[:-4]        # 1位の名前
    fc = int((str(result[26])[37:])[:-5])   # 1位の個数
    sn = (str(result[28])[21:])[:-4]        # 2位の名前
    sc = int((str(result[29])[37:])[:-5])   # 2位の個数
    tn = (str(result[31])[21:])[:-4]        # 3位の名前
    tc = int((str(result[32])[37:])[:-5])   # 3位の個数

    # データ表示
    print(str(d) + "日 " + str(h) + "時" + str(m) + "分")
    print(fn + "  " + str(fc))
    print(sn + "  " + str(sc))
    print(tn + "  " + str(tc))

    # csv出力
    with open('D:\\log.csv', 'a', encoding='utf-8_sig', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([d, h, m, fn, fc, sn, sc, tn, tc])

# 1分ごとにjobを実行
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
