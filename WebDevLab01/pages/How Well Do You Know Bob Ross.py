import streamlit as st
import info
import pandas as pd

#Intro
def Main_section():
    st.title("**How Well Do YOU Know Bob Ross??**")
    st.image(info.Bob, width = 200)
    st.write("Get 4+ questions right to prove your lowkey Bob Ross reincarnated")
    st.write('---')
Main_section()

score = 1

def Question_1():
    st.header("**1. Which of the following animals did Bob Ross rescue?**")
    options = st.multiselect(
        "Choose one or more options:",
        ["Pea-Poo the squirrel", "Peapod the squirrel", "Peep the robin", "Hoot the owl", "Otis the dog", "Cheep the canary"],
        default=["Peep the robin"]
    )
    st.write('---')

    correct = {"Pea-Poo the squirrel", "Peapod the squirrel", "Hoot the owl"}
    if set(options) == correct:
        return 1
    return 0
score += Question_1()

def Question_2():
    st.header("2. What was Bob Ross's painting show called?")
    options = ["A Life of Painting", "The Joy of Painting", "The Painter's Hour", "Happy Painting"]
    #NEW st.selectbox
    selected_option = st.selectbox("Choose one option:", options)

    if selected_option == "The Joy of Painting":
        return 1
    return 0
score += Question_2()
st.write("---")

def Question_3():
        st.header("3. Which subjects did Bob Ross paint?")
        #NEW st.multiselect
        options = st.multiselect(
            "Choose one or more options:",
            ["Landscapes", "Trees", "Mountains", "Bodies of water", "Animals", "Houses", "People"],
            default=["Trees"]
        )
        st.write('---')

        correct = {"Landscapes", "Trees", "Mountains", "Bodies of water", "Houses"}
        if set(options) == correct:
            return 1
        return 0
score += Question_3()
    
#Question_3()

def Question_4():
    st.header("4. How happy were Bob's trees?")
    #NEW st.slider
    happiness = st.slider("From a scale of 0 to 100", 0, 100)
    st.write(happiness, "% happy")

    if happiness == 100:
        return 1
    return 0
score += Question_4()
st.write("---")

#Question_4()

def Question_5():
    st.header("5. Why did the show end?")
    options = ["Money laundering scandal", "Lack of funding", "Retirement", "Death and Cancer", "Low ratings"]
    selected_option = st.selectbox("Choose one option:", options)
    st.write(f"You selected: {selected_option}")

    if selected_option == "Death and Cancer":
        return 1
    return 0
score += Question_5()

st.write("---")
st.subheader("Final Result")
st.write(f"You got {score} out of 5 correct!")

if score >= 4:
    st.success("🌟 omg you Bob fr 🌟")
    st.image(info.Happy, width = 200)
else:
    st.error("😔 You don't know Bob like that. What a shame.")
    st.image(info.dissapointed, width = 200)

