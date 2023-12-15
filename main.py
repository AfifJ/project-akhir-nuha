import streamlit as st
import pyrebase
import navigator

class FirebaseAuthenticator:
    def __init__(self):
        # Konfigurasi Firebase
        self.firebaseConfig = {
            "apiKey": "AIzaSyBo3fHZ7iw8h7oCooZEvjnLOUQOTRuMIKw",
            "authDomain": "fir-nuha.firebaseapp.com",
            "databaseURL": "https://firebase-nuha.firebaseio.com",
            "storageBucket": "fir-nuha.appspot.com",
            "serviceAccount": "fir-nuha-firebase-adminsdk-pab87-c48ad1e9a4.json"
        }

        # Inisialisasi Firebase
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()

        # Inisialisasi state dengan session_state
        if 'signin' not in st.session_state:
            st.session_state['signin'] = False    
        if 'main_access' not in st.session_state:
            st.session_state['main_access'] = False    
        if 'uid' not in st.session_state:
            st.session_state['uid'] = ''    
        if 'email' not in st.session_state:
            st.session_state['email'] = ''    

    def login_user(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            st.session_state.uid = user['localId']
            st.session_state.email = email
            st.session_state.signin = True   
            st.success(f"Login berhasil! User ID: {user['localId']}")
            st.rerun()  
            return user['localId']
        except Exception as e:
            st.error(f"Login gagal. Periksa kembali email dan password Anda. {e}")
            return None

    def logout_user(self):
        self.auth.current_user = None
        st.session_state.signin = False
        st.session_state.uid = None
        st.session_state.email = None

        st.success("Anda telah logout")

    def login_page(self):
        st.title('Login dengan Firebase menggunakan Pyrebase')

        # Form login
        email = st.text_input("Email", key="emailinput")
        password = st.text_input("Password", type="password", key="passwordinput")
        login_clicked = st.button("Login")

        if login_clicked:
            self.login_user(email, password)
           


    def register_user(self, email, password):
        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            st.success(f"Akun berhasil dibuat untuk {email}!")
            return user['localId']
        except Exception as e:
            st.error(f"Registrasi gagal: {e}")
            return None

    def register_page(self):
        st.title('Registrasi dengan Firebase menggunakan Pyrebase')

        # Form registrasi
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        register_clicked = st.button("Register")

        if register_clicked:
            user_id = self.register_user(email, password)
            if user_id:
                st.success("Silakan login dengan akun yang baru dibuat.")

    def run(self):
        if  not st.session_state["signin"]: 
            choice = st.selectbox('Login/Signup',['Login','Sign up'])
            if choice == "Sign up":
                self.register_page()
            else:
                self.login_page()
        elif st.session_state.signin:
          # st.empty()
            navigator.app()

if __name__ == "__main__":
    # page_title = "DIGITAL BOOKSTORE"
    # page_icon = "books"
    # st.set_page_config(page_title=page_title, page_icon=page_icon)

    authenticator = FirebaseAuthenticator()
    authenticator.run()
