from PIL import Image
from datetime import datetime
import streamlit as st
import os
import math
import numpy as np

str_converter = lambda x: x if x == "<select>" else f"0{x}" if x < 10 else f"{x}"

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
    return open_image(month = month, day = day)

def resize_image(im, newwidth):
    width, height = im.size
    newwidth = 150
    ratio = math.floor(height / width)
    newheight = ratio * newwidth
    im = im.resize((newwidth, newheight), Image.ANTIALIAS)
    return im

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
im = st.image(im, width=800)

if day != "<select>":
    im.empty()
    im = open_image(month=month, day=day)
    im = st.image(im, width=800)

