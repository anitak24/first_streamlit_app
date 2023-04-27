import streamlit

streamlit.title('My parent new healthy dinner')


streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & omlet')
streamlit.text('orange & strawberry Smoothi')
streamlit.text('scrambled egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
