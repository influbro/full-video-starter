from flask import Flask, request, redirect, render_template, url_for
import hashlib

app = Flask(__name__)

# Dictionary to store shortened URLs
url_map = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    # Create a unique short URL using a hash
    short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_map[short_url] = original_url
    return render_template('redirect.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_map.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
