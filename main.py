from flask import render_template, request, jsonify
from app import app 
from .models import generate_personalized_carol 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_carol_endpoint():
    user_name = request.form.get('user_name')
    user_interest = request.form.get('user_interest') 
    carol = generate_personalized_carol(user_name, user_interest) 
    return jsonify({'carol': carol})