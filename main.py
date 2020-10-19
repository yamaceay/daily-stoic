from PIL import Image
from datetime import datetime
import streamlit as st
import os
import math
import numpy as np

str_converter = lambda x: x if x == "<select>" else f"0{x}" if x < 10 else f"{x}"

def resize_image(im):
    width = st.screen.width
    height = st.screen.height
    width = math.floor(width * 0.8)
    height = math.floor(width * 0.8)
    im = im.resize((width, height), Image.ANTIALIAS)
    return im

def open_image(month, day):
    strday = str_converter(day)
    path = f"files/Stoicism-{month}/Stoicism-{month}-{strday}.jpg"
    im = Image.open(path)
    return im

def open_todays_image():
    date = datetime.now()
    date_string = date.strftime("%m/%d")
    [month, day] = date_string.split("/")
    month, day = int(month), int(day)
    return open_image(month=month, day=day)

div_css = "#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(3) > div > div > div"

st.title("Daily Stoa Texts")

month = "<select>"
day = "<select>"

months = ["<select>", *list(range(1, 13))]
str_months = list(map(str_converter, ["<select>", *list(range(1, 13))]))
month_index = str_months.index(st.selectbox("Select a month: ", str_months))
month = months[month_index]

if month != "<select>":
    days = ["<select>", *list(range(1, len(os.listdir(f"files/Stoicism-{month}"))+1))]
    days = list(range(1, len(os.listdir(f"files/Stoicism-{month}"))+1))
    str_days = list(map(str_converter, days))
    day_index = str_days.index(st.selectbox("Select a day: ", str_days))
    day = days[day_index]

im = open_todays_image()
#im = resize_image(im)
im = st.image(im, style={"width": "50%"})

if day != "<select>":
    im.empty()
    im = open_image(month=month, day=day)
    #im = resize_image(im)
    im = st.image(im, style={"width": "50%"})

st.markdown(f"""
    <style>
        body {{
            background-color: rgb(205, 225, 205);
        }}
        h1 {{
            text-align: center;
        }}
        {div_css} {{
            display: flex;
            justify-content: center;
        }}
        img {{
            max-width: 100%;
        }}
    </style>
""", unsafe_allow_html=True)