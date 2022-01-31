from flask import Flask
app = Flask(__name__)


from app.routes import user

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    