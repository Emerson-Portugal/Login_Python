from flask import Flask, render_template, url_for, request, redirect
from conextion import  obtener_usuario_por_credenciales

app = Flask(__name__)





@app.route('/')
def home():
    return render_template('home.html')

# Esta conectado las referencias HTML -> <a href="{{url_for('login')}}">Login</a>
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists in the database
        user = obtener_usuario_por_credenciales(username, password)

        if user:
            # Successful login
            return f"Login successful for user: {user[1]}"
        else:
            # Invalid credentials
            return "Invalid username or password"

    return render_template('login.html')



# Hace referencia a la funcion no a la ruta -> <a href="{{url_for('login')}}">Login</a>
@app.route('/registro')
def registro():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)