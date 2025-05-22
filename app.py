from flask import Flask, render_template
import os

# Importar los blueprints
from routes.extractor import extractor_bp
from routes.seo import seo_bp

app = Flask(__name__)

# Registrar los blueprints
app.register_blueprint(extractor_bp)
app.register_blueprint(seo_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)