# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:55:01 2022

@author: User
"""
pip install textblob
from textblob import TextBlob

from flask import Flask, request, render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        t=request.form.get("text")
        print(t)
        r=TextBlob(t).sentiment
        return(render_template("index.html",results=r))
    else:
        return(render_template("index.html",results="2"))
    
if __name__=="__main__":
    app.run()
