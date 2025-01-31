from flask import Flask, render_template, request, send_file
import wifi_qrcode_generator.generator
import os

tmp_file = "wifi_qr.png"
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ssid = request.form.get("ssid")
        password = request.form.get("password")
        auth_type = request.form.get("auth_type", "WPA")  # Default to WPA if missing

        valid_auth_types = ["WPA", "WEP", "nopass"]
        if auth_type not in valid_auth_types:
            return "Invalid authentication type", 400  # Return a 400 Bad Request error

        try:
            qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
                ssid=ssid,
                hidden=False,
                authentication_type=auth_type,
                password=password
            )
            qr_code.make_image().save("wifi_qr.png")
            return send_file("wifi_qr.png", as_attachment=True)

        except Exception as e:
            return f"Error generating QR code: {str(e)}", 500  # Handle other errors gracefully

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
