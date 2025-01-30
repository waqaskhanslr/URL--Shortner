from flask import Flask, render_template, request, jsonify, redirect
import hashlib

app = Flask(__name__)


url_mapping = {}


def generate_hash(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    print(f"Received URL: {original_url}")  
    
    # Check if URL has already been shortened
    if original_url in url_mapping:
        short_code = url_mapping[original_url]
    else:
        # Generate a unique hash for the URL
        short_code = generate_hash(original_url)
        url_mapping[original_url] = short_code

    short_url = request.host_url + short_code
    print(f"Generated short URL: {short_url}")  
    
    return jsonify({'short_url': short_url})

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Reverse lookup for original URL
    for original_url, code in url_mapping.items():
        if code == short_code:
            return redirect(original_url)
    
    return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
