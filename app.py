from flask import Flask, request, jsonify

from formdata import get_image_from_formdata
from scanner import scan_qr_code

app = Flask(__name__)


@app.post("/scan")
def scan():
  qr = request.files.get("qr")

  if qr is None:
    return jsonify({
      "success": False,
      "message": "QR file is required"
    }), 400

  try:
    img = get_image_from_formdata(qr)
    message = scan_qr_code(img)

    return jsonify({
      "success": True,
      "message": message
    })

  except Exception as e:
    return jsonify({
      "success": False,
      "message": str(e)
    }), 500
  

if __name__ == "__main__":
  app.run()