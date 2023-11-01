from flask import Flask, request
from mysql import MysqlDB

# 创建app实例
app = Flask(__name__)


# 创建根路由
@app.route('/')
def hi_flask():
    return 'hi,flask!'


# 获取总表数据
@app.route('/blog', methods=['GET'])
def getLangTop10():
    data = MysqlDB().get_data("select * from blog")
    return {
        "code": 200,
        "message": "成功获取总表数据",
        "result": data
    }


# 获取评论数前十的表
@app.route('/comment_top10', methods=['GET'])
def getCollectTop10():
    data = MysqlDB().get_data("select * from comment_top10")
    return {
        "code": 200,
        "message": "成功获取评论数前十的表",
        "result": data
    }


# 获取观看数前十的表
@app.route('/views_top10', methods=['GET'])
def getYearPush():
    data = MysqlDB().get_data("select * from views_top10")

    return {
        "code": 200,
        "message": "成功获取观看数前十的表",
        "result": data
    }


# 获取点赞数前十的表
@app.route('/digg_top10', methods=['GET'])
def getLangSumColl():
    data = MysqlDB().get_data("select * from digg_top10")
    return {
        "code": 200,
        "message": "成功点赞数前十的表",
        "result": data
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
