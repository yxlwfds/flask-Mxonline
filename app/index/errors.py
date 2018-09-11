from flask import render_template

from . import index


@index.app_errorhandler(404)
def page_not_found(e):
    return render_template('index/404.html')


@index.app_errorhandler(500)
def internal_server_error(e):
    return render_template('index/500.html')


@index.app_errorhandler(403)
def internal_server_error(e):
    return render_template('index/403.html')