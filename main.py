from PIL import Image
from datetime import datetime, timezone
import streamlit as st
import os
import math
import numpy as np
import pytz

str_converter = lambda x: x if type(x) == str else f"0{x}" if x < 10 else f"{x}"

def utc_to_local():
    IST = pytz.timezone('Europe/Istanbul') 
    date = datetime.now(IST) 
    return date

def parse_today():
    date = utc_to_local()
    date_string = date.strftime("%m/%d")
    [month, day] = date_string.split("/")
    month, day = int(month), int(day)
    return month, day

def open_image(month, day):
    strday = str_converter(day)
    path = f"files/Stoicism-{month}/Stoicism-{month}-{strday}.jpg"
    im = Image.open(path)
    return im

st.title("Daily Stoa Texts")

month, day = parse_today()

months = list(range(1, 13))
str_months = list(map(str_converter, months))
month_box = st.selectbox("Select a month: ", str_months, index=month-1)

if month_box != str_months[month-1]:
    month_index = str_months.index(month_box)
    month = months[month_index]

days = list(range(1, len(os.listdir(f"files/Stoicism-{month}"))+1))
str_days = list(map(str_converter, days))
day_box = st.selectbox("Select a day: ", str_days, index=day-1)

if day_box != str_days[day-1]:
    day_index = str_days.index(day_box)
    day = days[day_index]

im = st.image(open_image(month=month, day=day))

div_css = "#root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(1) > div:nth-child(3) > div > div > div"

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