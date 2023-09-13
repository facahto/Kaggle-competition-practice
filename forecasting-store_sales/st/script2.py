import streamlit as st


def navigate_to_website():
    # Redirect to another website when the button is clicked
    st.write("Redirecting to another website...")
    # Use Python's `webbrowser` module to open a URL in a new tab
    import webbrowser
    webbrowser.open_new_tab('https://acc-astra-kredit.streamlit.app')


# Add a button to the app
if st.button("Navigate to Website"):
    # When the button is clicked, call the navigate_to_website function
    navigate_to_website() 

st.write('Tidak minat karena DP tinggi')
st.write('Untuk DP bapak/ibu bisa ambil paket SUPER HEMAT dimana DP dimulai dari 15% untuk seluruh unit tpyota dan daihatsu ')
st.write('')
st.write('Selain itu ada paket SPEKTA dimana DP rendah mulai 10% dan free insurance 1 tahun all risk khusus unit Avanza, Veloz, Rush')
st.write('')
st.write('')

st.write('Tidak minat karena angsuran kecil')
st.write('Untuk brand Toyota Bapak/Ibu bisa mendapat paket EZ-DEAL dengan angsuran stepping rendah di 2tahun pertama')
st.write('')
st.write('Untuk brand Daihatsu bapak/ibu bisa mendapat FREE ANGSURAN 4x untuk unit Ayla&Sigra')
st.write('')
st.write('')

st.write('Tidak minat karena benefit yang diberikan hanya itu saha')
st.write('Ijin setelah ini saya kirimkan undangan event yang diselenggarakan oleh cabang ACC, bapak/ibu bisa claim benefit tambahannya. Selain mendapat benefit dari HO, bapak/ibu juga mendapat benefit dari event dealer seperti doorprize & merchandise')
