from flask import Flask,render_template
app=Flask(__name__) #代表目前執行的模組

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/accounts") #代表我們要處理的網站路徑
def accounts():
    return render_template("accounts.html")

@app.route("/add-product")
def addproduct():
    return render_template("add-product.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/management")
def management():
    return render_template("management.html")

if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器