import streamlit as st
import pyautogui
import pyperclip

text = st.text_input("入力")
if(st.button("送信")):
    print(text)
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    st.write("完了")