import streamlit as st

def main():
    st.markdown("<h1 style='text-align:center;'>STORY BOT</h1>", unsafe_allow_html=True)

    with st.form("Adventure"):
        col1, col2 = st.columns(2)
        
        col1.markdown('<h1 style="color:white; font-size: 50px; text-align: center;">TEXT</h1>', unsafe_allow_html=True)
        col1.markdown('<style>.text-box {border: 2px solid #333;padding: 20px;border-radius: 10px;background-color: brown;height:333px;width:100%;}</style><div class="text-box">Story goes here</div>', unsafe_allow_html=True)
        
        col2.markdown('<h1 style="color:white; font-size: 50px; text-align: center;">IMAGE</h1>', unsafe_allow_html=True)
        col2.markdown('<style>.image-box {border: 2px solid #333;padding: 20px;border-radius: 10px;background-color: brown;height:330px;width:100%;}</style><div class="image-box"><img src="sdxl.png", alt="Your Image" style="max-width: 100%; height: 100%;"></div>', unsafe_allow_html=True)
        
        option1="Option 1 \n "
        option2="Option 2 \n"
        
        st.markdown("---")
        st.markdown('<h2 style="color:white; font-size: 30px; text-align: center;">Choose Your Option</h2>', unsafe_allow_html=True)
        st.markdown("---")
        
        radio_btn = st.radio("Choose Your Option:", options=(option1, option2), label_visibility="collapsed")
        st.markdown('<style>.radio-item label {margin-bottom: 10px;}</style>', unsafe_allow_html=True)
        next_btn = st.form_submit_button("Next", use_container_width=True)

        


main()
