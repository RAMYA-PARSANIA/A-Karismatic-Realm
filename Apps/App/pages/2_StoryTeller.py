import streamlit as st
import subprocess
import shutil
import os
from gradio_client import Client
from ML_Model import story_starters,story_nums,final_chap,txt_to_img,move_image_to_current_directory,generate_option_via_api,generate_story_via_api
import pyttsx3
st.set_page_config(
    page_title="StoryTeller",
    page_icon="📖",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.st-emotion-cache-aw8l5d.eczjsme1
{visibility:hidden}
</style""",unsafe_allow_html=True)


API_URL = "https://api-inference.huggingface.co/models/aspis/gpt2-genre-story-generation"
HEADERS = {"Authorization": "Bearer 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"}
API_URL_OPT = "https://api-inference.huggingface.co/models/gpt2-xl"
# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)
# Main story generation loop
if (st.session_state["counter"] <= 3):
    imagePaths = []
    if "initial_prompt" not in st.session_state:
        st.session_state["initial_prompt"] = story_starters[story_nums[int(st.session_state["choice"])]]

    if 'submit_btn' not in st.session_state:
        st.session_state.disabled = False

    txt = ''

    # st.markdown('<style>.text-box {border: 2px solid #333;padding: 20px;border-radius: 10px;background-color: brown;height:100%;width:100%;}</style><div class="text-box">{to_print_story}</div>', unsafe_allow_html=True)
    # Generate the main part of the story
    gen_story = generate_story_via_api(st.session_state["initial_prompt"], length=250, num_sequences=1)
    to_print_story = gen_story[0]
    last_full_stop_index = to_print_story.rfind(".")
    last_qmark_index = to_print_story.rfind("?")
    last_emark_index = to_print_story.rfind("!")
    last_quote_index = to_print_story.rfind('"')
    last_story_index = max(last_full_stop_index, last_qmark_index, last_emark_index, last_quote_index)
    if last_story_index != -1:
        to_print_story = to_print_story[:last_story_index + 1]  # Remove the part before the last full stop
    else:
        to_print_story = to_print_story
    engine.say(to_print_story)
    st.write(to_print_story)
    imageGen = txt_to_img(to_print_story)
    newWorkDir = move_image_to_current_directory(imageGen)
    st.image("image.png")
    engine.runAndWait()

    options_prompt = gen_story[0] + " At this critical juncture, they face a dilemma:"
    story_options = generate_option_via_api(options_prompt, length=20, num_sequences=2)

    # Present options to the user
    options=[]
    for i, story in enumerate(story_options):
        option_text = story.split(".")[0]  # Take the first sentence as an option
        to_print_opt = option_text
        last_full_stop_index_opt = to_print_opt.rfind(".")
        last_qmark_index_opt = to_print_opt.rfind("?")
        last_emark_index_opt = to_print_opt.rfind("!")
        last_quote_index_opt = to_print_opt.rfind('"')
        last_opt_index = max(last_full_stop_index_opt,last_qmark_index_opt,last_emark_index_opt,last_quote_index_opt)
        if last_opt_index != -1:
            to_print_opt = to_print_opt[:last_opt_index + 1]  # Remove the part before the last full stop
        else:
            to_print_opt = to_print_opt
        options.append(to_print_opt)
        print(f"Option {i+1}: {to_print_opt}\n")
    option1=options[0]
    option2=options[1]
    # User makes a choice
    st.markdown("---")
    st.markdown('<h2 style="color:white; font-size: 30px; text-align: center;">Choose Your Option</h2>', unsafe_allow_html=True)
    st.markdown("---")
    #radio button
    chosen_option = st.radio("Choose Your Option:", options=(option1, option2),label_visibility="collapsed")
    submit=st.button("Submit",use_container_width=True,key="submit_btn",disabled=st.session_state.disabled)
    if(submit):
        st.session_state["counter"]=st.session_state["counter"] + 1
        st.session_state["initial_prompt"] = st.session_state["initial_prompt"] + chosen_option
        
        if(st.session_state["counter"]==3):
                st.session_state.disabled=False
                st.empty()

else:
    st.write(final_chap)
    imageGen = txt_to_img(final_chap)
    newWorkDir = move_image_to_current_directory(imageGen)
    st.markdown('<h1 style="color:white; font-size: 50px; text-align: center;">IMAGE</h1>', unsafe_allow_html=True)
    st.image("image.png")
    # play=st.button("Play",use_container_width=True)
    subprocess.call(["Python3","newGame.py"],shell=True)

# st.markdown("---")
# st.markdown('<h2 style="color:white; font-size: 30px; text-align: center;">Choose Your Option</h2>', unsafe_allow_html=True)
# st.markdown("---")

