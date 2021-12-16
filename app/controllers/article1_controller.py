from app.controllers.controller import ControllerBase
from flask import render_template


class Article1Controller(ControllerBase):
    @staticmethod
    def get():
        return render_template('p2_article1.html')

