import requests
import streamlit as st
def app():
    st.write("""
    ## Tweet analysis of disaster tweets
    Shown are the tweets and classify them as Dangerous or not
    """)

    Email = st.text_input('Enter your E-mail', )
    st.write('Confirm your E-mail', Email)

    EmergencyEmail1 = st.text_input('Enter your Emergency E-mail1')

    message = st.text_area("Enter message/tweet which u want to post", '', height=100, max_chars=200)
    st.title(message)


    if st.button('Submit'):
        st.success('posted')
        data = {
            "YourEmail": Email,
            "EmeEmail": EmergencyEmail1,
            "Msg": message
        }
        print(data)
        api_url = requests.get("http://127.0.0.1:5000/Submit", json=data)  # Flask url

    else:
        st.error('dangerous tweet')

    st.subheader("Dataset")
    data_file = st.file_uploader("Upload CSV", type=['csv'])
    if st.button("Process"):
        if data_file is not None :
            files = {"file": data_file.getvalue()}
            res = requests.get(f"http://127.0.0.1:5000/SubmitFile", files=files)

    else:
        st.error('dangerous tweet')




