from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pdf_generator.generator import PDFGenerator
from neural_network.model import NeuralNetwork
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_report():
    data = request.json
    input_text = data.get('text', '')
    if not input_text:
        return jsonify({'error': 'No text provided'}), 400

    neural_network = NeuralNetwork()
    dimensions, generated_text = neural_network.process_input(input_text)

    pdf_filename = "informe.pdf"
    pdf_path = os.path.join("/tmp", pdf_filename)
    pdf_generator = PDFGenerator(pdf_path)
    pdf_generator.save_report(dimensions, generated_text)

    return jsonify({
        'dimensions': dimensions,
        'generated_text': generated_text,
        'pdf_url': f'/download/{pdf_filename}'
    })

@app.route('/download/<filename>', methods=['GET'])
def download_pdf(filename):
    pdf_path = os.path.join("/tmp", filename)
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)