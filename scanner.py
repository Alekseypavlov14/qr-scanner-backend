import zxingcpp


def scan_qr_code(img):
  if img is None:
    raise ValueError("INVALID IMAGE")

  results = zxingcpp.read_barcodes(img)

  if not results:
    return None

  return results[0].text
