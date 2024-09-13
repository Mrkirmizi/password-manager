from flask import Flask, render_template, request, redirect, url_for, flash
from cryptography.fernet import Fernet
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    site_name = request.form['site_name']
    username = request.form['username']
    password = request.form['password']
    
    if not site_name or not username or not password:
        flash('All fields are required!', 'error')
        return redirect(url_for('index'))
    
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()
            if lines:
                last_id = int(lines[-1].split(',')[0])
                new_id = last_id + 1
            else:
                new_id = 1
    else:
        new_id = 1
    
    with open('passwords.txt', 'a') as f:
        f.write(f"{new_id},{site_name},{username},{encrypted_password.decode()},{key.decode()}\n")
    
    flash('Password saved successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/view')
def view():
    passwords = []
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            for line in f:
                id, site_name, username, encrypted_password, key = line.strip().split(',')
                cipher_suite = Fernet(key.encode())
                decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                passwords.append((id, site_name, username, decrypted_password))
    return render_template('view.html', passwords=passwords)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        site_name = request.form['site_name']
        username = request.form['username']
        password = request.form['password']
        
        if not site_name or not username or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('edit', id=id))
        
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        
        with open('passwords.txt', 'r') as f:
            lines = f.readlines()
        
        with open('passwords.txt', 'w') as f:
            for line in lines:
                current_id, _, _, _, _ = line.strip().split(',')
                if current_id == id:
                    f.write(f"{id},{site_name},{username},{encrypted_password.decode()},{key.decode()}\n")
                else:
                    f.write(line)
        
        flash('Password updated successfully!', 'success')
        return redirect(url_for('view'))
    else:
        with open('passwords.txt', 'r') as f:
            for line in f:
                current_id, site_name, username, encrypted_password, key = line.strip().split(',')
                if current_id == id:
                    cipher_suite = Fernet(key.encode())
                    decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
                    return render_template('edit.html', id=id, site_name=site_name, username=username, password=decrypted_password)
        return redirect(url_for('view'))

@app.route('/delete/<id>')
def delete(id):
    with open('passwords.txt', 'r') as f:
        lines = f.readlines()
    
    with open('passwords.txt', 'w') as f:
        for line in lines:
            current_id, _, _, _, _ = line.strip().split(',')
            if current_id != id:
                f.write(line)
    
    flash('Password deleted successfully!', 'success')
    return redirect(url_for('view'))

if __name__ == '__main__':
    app.run(debug=True)
