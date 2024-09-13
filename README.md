# Password Manager

This is a simple password manager web application built with Flask and Python. It allows users to save, view, edit, and delete passwords securely.

## Features

- Add new passwords with site name, username, and password fields.
- View saved passwords in a table format.
- Edit existing passwords.
- Delete passwords.
- Passwords are encrypted using the `cryptography` library.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mrkirmizi/password-manager
    cd password-manager
    ```


2. Install the required packages:
    ```bash
    pip install flask cryptography
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Use the web interface to add, view, edit, and delete passwords.
## File Structure


password_manager/  
- ├── app.py 
- ├── passwords.txt  
- ├── templates/ │ 
-    │ └── edit.html 
-   ├── index.html │ 
-   ├── view.html 
- ├── static/ 
- │ └── style.css

## Dependencies

- Flask
- cryptography

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License
