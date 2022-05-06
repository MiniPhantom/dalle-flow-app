# -*- coding: utf-8 -*-
import streamlit as st
from dalle_flow import (
    request_sprites,
    request_diffusion_sprite,
    request_resolution,
)


def run_generation(prompt, num_images):

    with st.spinner(text="Doing fancy calculations... 🪄🤖"):
        da, img = request_sprites(prompt, num_images=num_images)

    # display images
    # update session state
    st.session_state["sprite"] = True
    st.session_state["first_img"] = img
    st.session_state["da"] = da


def run_diffusion(fav_id, num_images):

    fav = st.session_state["da"][int(fav_id)]
    with st.spinner(text="Doing even more fancy calculations... 🪄🤖"):
        da, dif_img = request_diffusion_sprite(fav, num_images)

    # display images
    st.image(dif_img, use_column_width=False, width=700)

    # update session state
    del st.session_state["first_img"]
    st.session_state["diffusion"] = True
    st.session_state["da"] = da
    st.session_state["resolution"] = True


def run_resolution(fav_id):

    fav = st.session_state["da"][int(fav_id)]
    with st.spinner(text="Doing slightly less fancy calculations... 🌮"):
        da = request_resolution(fav)

    # print(da.summary())
    # update session state
    st.session_state["final_img"] = da.uri
    del st.session_state["resolution"]


def main():

    """
    Streamlit app for AI art generation.
    """

    #################
    # SIDEBAR
    #################

    # SIDEBAR TITLE
    st.sidebar.markdown(
        '<p style="font-size: 4em; font-weight: 1100;">AI ART</p>',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown(
        """AI is changing the way we think about art.
        Here we showcase [DALL-E](https://openai.com/blog/dall-e/) 
        and [GLIDE](https://gpt3demo.com/apps/openai-glide) ([OpenAI, 
        2021](https://openai.com/research/)) through 
        [DALL-E Flow](https://github.com/jina-ai/dalle-flow) from 
        [Jina](https://jina.ai/). Try it out for yourself! 🚀
        """
    )
    st.sidebar.markdown(
        """**NOTE**: Models are generously served by [Jina](https://jina.ai/)
        through their [DALL-E Flow](https://github.com/jina-ai/dalle-flow)
        test server. High latency and server unavailability may occurr.
        """
    )
    st.sidebar.markdown("##")
    num_images = (
        st.sidebar.number_input(
            "# IMAGES", min_value=2, max_value=16, value=16
        )
        // 2
    )

    #################
    # 1. MAIN PANE
    #################

    prompt = False
    if "diffusion" not in st.session_state:
        prompt = st.text_input("", placeholder="Enter your text here ✏️")

    #################
    # 1.1. Inital generation stage
    #################

    if "prompt" in st.session_state:
        if prompt != st.session_state["prompt"]:
            del st.session_state["sprite"]

    if prompt and "sprite" not in st.session_state:
        run_generation(prompt, num_images)
        st.session_state["prompt"] = prompt
        st.markdown("#")

    if "first_img" in st.session_state:
        st.image(
            st.session_state["first_img"], use_column_width=False, width=700
        )

    #################
    # 1.2. Diffusion stage
    #################

    if "sprite" in st.session_state and "diffusion" not in st.session_state:
        col1, col2 = st.columns([3, 1])
        fav_id = col1.text_input(
            "",
            max_chars=2,
            value=0,
            placeholder="Select ID of image to diffuse from",
        )
        col2.markdown("#")
        col2.button(
            "Diffuse! 🤖",
            on_click=run_diffusion,
            args=(fav_id, 9),
        )

    #################
    # 1.2. Upscaled resolution stage
    #################

    if "resolution" in st.session_state:

        col1, col2 = st.columns([3, 1])
        fav_id = col1.text_input("")
        col2.markdown("#")
        col2.button(
            "Upscale resolution! 🤖",
            on_click=run_resolution,
            args=(fav_id,),
        )

    #################
    # 1.3. End stage
    #################

    if "final_img" in st.session_state:
        st.image(
            st.session_state["final_img"], use_column_width=False, width=700
        )

if __name__ == "__main__":
    main()
