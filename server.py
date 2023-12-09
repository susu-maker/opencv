# 導入Flask模組
import barcode as bc
from flask import Flask, request, render_template, jsonify, json

# 創建Flask應用
app = Flask(__name__)

# 定義首頁路由
@app.route('/')
def index():
    # 渲染首頁模板
    return render_template('test.html')

# 定義計算路由，接收POST請求
@app.route('/barcode', methods=['POST'])
def barcode():
    # 獲取表單中的數字
    # print(request.json)
    # picture = request.values.get('image')
    picture = request.json["image"]
    # print(picture)
    # 轉換為文字
    print(type(picture))
    print("ok")
    number = bc.barcode(picture)
    # return jsonify
    if(number == 0):
        return 0
    else: 
        return jsonify({"barcode":number})

# 運行Flask應用
if __name__ == '__main__':
    app.run(debug = True, port = 8000)