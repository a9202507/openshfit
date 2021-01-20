from flask import Flask,render_template
app = Flask(__name__)
#print(app.config)
#設定資源快取時間為零秒
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0
author_name ="eason"
web_info ={
    "title":"歡迎來我的網站",
    "subtitle":"welcome"
}

show_link=True
article_list= [
    {
        "id":"1", 
        "title":"文章1",
        "subtitle":"副標題1",
        "content":"內文1",
    },
    {
        "id":"2", 
        "title":"文章2",
        "subtitle":"副標題2",
        "content":"內文2",
    },
        {
        "id":"3", 
        "title":"文章3",
        "subtitle":"副標題3",
        "content":"內文3",
    },

]

@app.route('/')
def hello():
    html = render_template("home.html",
                            web_info=web_info,
                            author_name=author_name,
                            show_link=show_link,
                            header_title="HOME Page"
                            )
    return html

@app.route('/about')
def method_name():
    return render_template("about.html",
                            #header_title="about page",
                            )
@app.route('/article')
def article_list_page():
   return render_template("article-list.html",
                            header_title="py文章列表",
                            article_list=article_list,
   )


##動態路由
@app.route('/article/<article_id>') ## <> 為flask的變數寫法
def article_page(article_id):
    article=None
    for a in article_list:
        if a['id']==article_id:
            article=a
    ##如果文章存在 就返回文章
    if article:
        return f"文章: {article}"
    else:
        return "查無此文章"
    
if __name__ == '__main__':
    app.run(debug=True,port=5500)
    