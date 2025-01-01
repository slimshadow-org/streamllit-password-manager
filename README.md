# Streamlit Password Manager

A simple and secure password manager built using Streamlit. This app allows you to store and manage your passwords locally with encryption.

## Features

* **Secure Storage:** Passwords are encrypted using Fernet encryption before being stored locally.
* **User-Friendly Interface:**  Easy-to-use interface built with Streamlit for adding, viewing, updating, and deleting passwords.
* **Search Functionality:** Quickly search for passwords by website or application name.
* **Copy to Clipboard:** Easily copy passwords to your clipboard with a single click.
* **Local Storage:**  Your data stays on your machine; no server-side storage is involved.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/slimshadow-org/streamlit-password-manager.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd streamlit-password-manager
   ```

3. **Install required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the app:**
   ```bash
   streamlit run app.py
   ```

2. **Set a Master Password:** The first time you run the app, you'll be prompted to create a master password. This password will be used to encrypt and decrypt your stored passwords.  **Remember this password; you won't be able to recover your data without it!**

3. **Manage your passwords:** Use the Streamlit interface to add, view, edit, delete, and search for your passwords.


## Security

This app uses Fernet encryption to protect your passwords. However, remember that no system is completely secure.  **Store your master password securely and consider using a strong, unique password.**  Because the data is stored locally, it's your responsibility to protect the file containing the encrypted passwords.


## Contributing

Contributions are welcome!  Please feel free to open issues and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).  (Create a LICENSE file if you haven't already)


## Disclaimer

This software is provided "as is" without warranty of any kind. Use at your own risk.  The developers are not responsible for any data loss or security breaches.



## To Do (Optional)

* Implement password strength checker
* Add support for importing/exporting passwords
* Improve the user interface
* Add more robust error handling
