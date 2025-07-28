import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import render_template, jsonify
from src import create_app, db
from src.routes.chamados import chamados_bp

app = create_app()

# Registrar blueprints
app.register_blueprint(chamados_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
