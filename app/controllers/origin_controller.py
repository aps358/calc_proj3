from app.controllers.controller import ControllerBase
from flask import render_template


class OriginController(ControllerBase):
    @staticmethod
    def get():
        return render_template('origin.html')

