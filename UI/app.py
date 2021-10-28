import streamlit as st
import requests


def main():

    st.title("Movie Review Sentiment Analysis")
    message = st.text_input('Enter review to classify...')
    url = "http://service:8000/predict/"

    if st.button('Predict'):
        payload = {
            "text": message
        }
        res = requests.post(url,json=payload )
        prediction = float(res.text)
        with st.spinner('Classifying, please wait....'):
            if prediction >= 0.5:
                st.success("Positive review with {:.2f} confidence".format(prediction))
                st.balloons()
            elif prediction <0.5:
                st.error("Negative review with {:.2f} confidence".format(1-prediction))

if __name__ == '__main__':
    main()
