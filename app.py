from flask import Flask,render_template
app = Flask(__name__)
print(dir(app))
#print(app.config)
#設定資源快取時間為零秒
app.config['SEND_FILE_MAX_AGE_DEFAULT']=0
author_name ="eason"
web_info ={
    "title":"歡迎來我的網站 IFX",
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
    {
        "id":"4", 
        "title":"文章4",
        "subtitle":"副標題4",
        "content":"內文4",
    },
    {
        "id":"5", 
        "title":"文章5",
        "subtitle":"副標題5",
        "content":"內文5",
    },

]

@app.route('/')
def hello():
    html = render_template("home.html",
                            web_info=web_info,
                            author_name=author_name,
                            show_link=show_link,
                            header_title="Infineon powerstage efficiency calculation"
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
            break
    ##如果文章存在 就返回文章
    print(article)
    if article:
        return render_template("article/show.html",
                                article=article,
                                header_title=article['title'])
    else:
        # 如果文章不存在
        return render_template("article/not-found.html",
                                article_id=article_id,
                                header_title="查無文章")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')
    ## test
