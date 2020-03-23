"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from covid import app
import requests
import html_parsers

@app.route('/')
@app.route('/covid')
def covid():
    page_html = requests.get("https://www.worldometers.info/coronavirus/").text
    parser = html_parsers.CovidParser()
    parser.feed(page_html)
    return parser.data

@app.route('/bazen')
def bazen():
    page_html = requests.get("https://www.szcb.cz/plavecky-stadion-a-plovarna/").text
    parser = html_parsers.BazenParser()
    parser.feed(page_html)
    return parser.data


