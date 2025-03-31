import os
from flask import current_app
from app import app


def get_uploaded_images(app):
    upload_folder = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    print("Looking in folder:", upload_folder) 
    if not os.path.exists(upload_folder):
        print("Uploads folder does not exist!")
        return []
    images = [f for f in os.listdir(upload_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
    print("Found images:", images)  
    return images
