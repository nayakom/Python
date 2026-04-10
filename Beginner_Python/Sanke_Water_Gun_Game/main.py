import random
import streamlit as st

# page title
st.title("Snake, Water & Gun Game")
st.subheader("Computer VS Player")

# Game logic

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
        
col1, col2, col3 = st.columns(3)

you = None

# create a button
with col1:
    if st.button("Snake (s) 🐍"):
        you = 's'

with col2:
    if st.button("Water (w) 💧"):
        you = 'w'

with col3:
    if st.button("Gun (g) 🔫"):
        you = 'g'

if you:
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo ==3:
        comp = 'g'

    a = gamewin(comp, you)

    st.write("---")
    st.write(f"🤖 **Computer Turn :** {comp}")
    st.write(f"👤 **You Turn :** {you}")

# Result Message
    if a == None:
        st.warning("⚠️ The Game Is Tie!")
    elif a:
        st.success("🎉 You Win The Game!")
        st.balloons()
    else:
        st.error("💀 You Lose The Game!")
