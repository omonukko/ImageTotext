import google.generativeai as genai
from flask import Flask,jsonify
import base64
import time

app = Flask(__name__)
genai.configure(api_key="You Gemini API Key here")

@app.route('/api/ImageToText/', methods=['POST'])
def ImageToText():
    if 'image' not in request.json:
        return jsonify({'error': 'No image data provided'}), 400
    start_time = time.time()
    try:
        image_data = request.json['image']
        if not image_data.startswith('data:image'):
            return jsonify({'error': 'Invalid image data'}), 400
        if image_data.startswith('data:image'):
            data = image_data.split(',', 1)[1]
        image_data = base64.b64decode(data)
        image = Image.open(BytesIO(image_data))
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
        response = model.generate_content(["画像の中の文字だけを返してください説明などは不要です", image])
        text = response.text if hasattr(response, 'text') else str(response)
    except Exception as e:
        return jsonify({'error': f'{str(e)}'}), 500
    elapsed_time = time.time() - start_time
    return jsonify({'solved': True, 'result': text, 'time': f'{elapsed_time:.2f}s'})

app.run(debug=False,port=8011)
