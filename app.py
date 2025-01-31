from flask import Flask, render_template, request, send_file
import wifi_qrcode_generator.generator
import os

tmp_file = "wifi_qr.png"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ssid = request.form['ssid']
        password = request.form['password']
        auth_type = request.form['auth_type']
        
        qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
            ssid=ssid, hidden=False, authentication_type=auth_type, password=password
        )
        qr_code.make_image().save(tmp_file)
        return send_file(tmp_file, as_attachment=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
