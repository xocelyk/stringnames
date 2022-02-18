import csv
import streamlit as st

def load_names(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return [name for name in reader]

def check_name(name):
    name = name.split(' ')
    if len(st.session_state.current_string) == 0:
        return name
    elif name[-1] == st.session_state.current_string[0]:
        return name[:-1] + st.session_state.current_string
    elif name[0] == st.session_state.current_string[-1]:
        return st.session_state.current_string[:-1] + name
    else:
        return False

def play(try_name):
    res = check_name(try_name)
    if res is False:
        st.write('Try again')
        return
    else:
        st.session_state.current_string = res
        st.session_state.counter += 1

def reset():
    st.session_state.clear()

def main():
    st.header('Welcome to String Names')

    st.button('Reset', on_click=reset)

    if 'key' not in st.session_state:
        st.session_state.key = 'value'
        
    if 'current_string' not in st.session_state:
        st.session_state.current_string = []

    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    list_names = load_names('nba_names.csv')
    string_names = [' '.join(name).upper() for name in list_names]

    try_name = st.selectbox('Select a name', string_names)
    st.button('Submit', on_click=play, args=[try_name])

    st.write('Current Name:', ' '.join(st.session_state.current_string))
    st.write('Current Score:', str(st.session_state.counter))

if __name__ == '__main__':
    main()

