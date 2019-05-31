#!/usr/bin/python
#-*-coding:utf-8-*-

from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import pymysql
from functools import wraps
import sys
import time

reload(sys)
sys.setdefaultencoding('UTF-8')

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)

app.secret_key = 'M\t\xd2`i9eLW7\xc7\x0b\xa4pP\xbc\x03\x9a\x1c\x9a\xf2\xac\xc4\x8e'

def check_regist():
	#user = User.query.filter(or_(User.username == username, User.email == email)).first()
	if request.form['name']=='' or request.form['num']=='' or request.form['tel']=='' or request.form['qq']=='':
		return False
	else:
		return True
def check_tel():
	if len(request.form['tel'])!=11:
		return False
	else:
		return True

@app.route('/',methods=['GET','POST'])
def regist():

	error = None
	if request.method == 'POST':
		if check_regist():
			if check_tel():
				ip = request.remote_addr
				ctime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			#print request.form['name'],request.form['num'],request.form['tel'],request.form['qq']
				f = open('namelist.txt','a')
				f.write(ctime+'    '+ip+'    '+request.form['name']+'  '+request.form['num']+ '  '+request.form['tel']+ '  '+request.form['qq']+ '    '+request.form['select']+'\n')

				flash('报名成功!请留意群内公布的招新时间，感谢参与！')
				return render_template("error.html")
			else:
				error='请检查输入手机号是否输入正确!'
				flash(error)
				return render_template("error.html")

		else:
			error='请完善所有的信息'
			flash(error)
			return render_template("error.html")

	return render_template('sign_up.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0',port='8000',debug=True)
