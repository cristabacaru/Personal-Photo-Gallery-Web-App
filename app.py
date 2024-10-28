from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
from models import User  # Import the User model from your models.py file
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

login_manager = LoginManager()
login_manager.init_app(app)

UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Function to get categories and images dynamically
def get_categories_and_images():
    categories = []
    images = {}

    # Get the list of categories (subdirectories) in the uploads folder
    for category in os.listdir(UPLOAD_FOLDER):
        if os.path.isdir(os.path.join(UPLOAD_FOLDER, category)):
            categories.append(category)
            images[category] = [image for image in os.listdir(os.path.join(UPLOAD_FOLDER, category)) if os.path.isfile(os.path.join(UPLOAD_FOLDER, category, image))]
    
    return categories, images

@app.route('/')
def index():
    error_message = request.args.get('error_message')
    categories, images = get_categories_and_images()
    return render_template('index.html', error_message=error_message, categories=categories, images=images)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        error_message = "You are already logged in. Log out to access."
        return redirect(url_for('index', error_message=error_message))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.get(username)  # Retrieve user details
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html')

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not current_user.is_authenticated:
        error_message = "You must log in to upload files!"
        return redirect(url_for('login', error_message=error_message))

    if request.method == 'POST':
        file = request.files['image']
        name = request.form.get('name')
        category = request.form.get('category')

        if file.filename == '':
            return redirect(url_for('upload', error_message="No selected file"))

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)

            # Optionally, save the name and category to a database

            return redirect(url_for('index'))

    return render_template('upload.html')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Add route to handle image deletion
@app.route('/delete_image/<category>/<image>', methods=['POST'])
@login_required
def delete_image(category, image):
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], category, image)
    if os.path.exists(image_path):
        os.remove(image_path)  # Delete the image file
    return redirect(url_for('index'))  # Redirect to the home page after deletion


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




