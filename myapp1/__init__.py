#coding=utf-8
from flask import Flask 
from views import frontend, admin   
DEFAULT_APP_NAME = 'myapp1'   
DEFAULT_MODULES = ((frontend, ''),(admin, '/admin'))   

def create_app():
	app = Flask(DEFAULT_APP_NAME) # 使用flask中的Blueprint设置站点模块 
	setting_modules(app, DEFAULT_MODULES) 
	return app   

def setting_modules(app, modules): 
	for module, url_prefix in modules: # 通过register_blueprint注册 
		app.register_blueprint(module, url_prefix = url_prefix) 

