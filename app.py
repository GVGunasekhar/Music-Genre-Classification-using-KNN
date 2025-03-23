'''import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from model import load_and_preprocess_data, model_prediction

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio'

# Ensure the folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No file selected", 400
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Convert to MP3 for browser compatibility
        converted_filename = convert_to_mp3(file_path)

        return redirect(url_for('predict', filename=converted_filename))

    return render_template('index.html')

@app.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    X_test = load_and_preprocess_data(file_path)
    result_index = model_prediction(X_test)

    labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    genre = labels[result_index]

    # Determine MIME type for audio playback
    mime_type = f"audio/{filename.split('.')[-1]}"

    return render_template('result.html', genre=genre, filename=filename, mime_type=mime_type)

def convert_to_mp3(file_path):
    """Convert WAV to MP3 for better playback in browsers"""
    if file_path.endswith('.wav'):
        mp3_filename = file_path.replace('.wav', '.mp3')
        mp3_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(mp3_filename))
        
        try:
            subprocess.run(['ffmpeg', '-i', file_path, '-q:a', '2', mp3_path], check=True)
            os.remove(file_path)  # Delete original WAV after conversion
            return os.path.basename(mp3_filename)
        except Exception as e:
            print(f"Error converting file: {e}")
            return os.path.basename(file_path)

    return os.path.basename(file_path)

if __name__ == '__main__':
    app.run(debug=True)
'''


import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from model import load_and_preprocess_data, model_prediction  # Import model functions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['file']
        
        if file.filename == '':
            return "No file selected", 400
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Convert to MP3 for browser compatibility
        converted_filename = convert_to_mp3(file_path)

        return redirect(url_for('predict', filename=converted_filename))

    return render_template('index.html')

@app.route('/predict/<filename>', methods=['GET'])
def predict(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Load and preprocess audio data for prediction
    X_test = load_and_preprocess_data(file_path)
    result_index = model_prediction(X_test)

    labels = ['Blues', 'Classical', 'Country', 'Disco', 'Hiphop', 'Jazz', 'Metal', 'Pop', 'Reggae', 'Rock']
    genre = labels[result_index]

    # Determine MIME type for audio playback
    mime_type = "audio/mp3" if filename.endswith('.mp3') else "audio/wav"

    return render_template('result.html', genre=genre, filename=filename, mime_type=mime_type)

def convert_to_mp3(file_path):
    """Convert WAV to MP3 for better playback in browsers"""
    if file_path.endswith('.wav'):
        mp3_filename = file_path.replace('.wav', '.mp3')
        mp3_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(mp3_filename))
        
        try:
            subprocess.run(['ffmpeg', '-i', file_path, '-q:a', '2', mp3_path], check=True)
            os.remove(file_path)  # Delete original WAV after conversion
            return os.path.basename(mp3_filename)
        except Exception as e:
            print(f"Error converting file: {e}")
            return os.path.basename(file_path)

    return os.path.basename(file_path)

if __name__ == '__main__':
    app.run(debug=True)
