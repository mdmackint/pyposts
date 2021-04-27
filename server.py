from http.server import BaseHTTPRequestHandler, HTTPServer
import json
x = open("setup.json")
setup = x.read()
x.close()
setup = json.loads(setup)
del x
port = input("Please select a port for the server: ")
page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{}</title>
    <style>
    body {{
    font-family: 'Segoe UI', sans-serif;
    }}
    </style>
</head>
<body>
    <h1 style="position: absolute; top: 3px; text-align: left; margin-left: 3%;">{}</h1>
    <p style="position: absolute; top: 20px; right: 3px; text-align: right; margin-right: 3%; color: gray;">{}</p>
    <br><br><br><br><br><br>
    <h1 style="text-align: center;">Posts</h1>
    <br><br><br>
    <hr>
    <br><br>
    <div style="text-align: center;">
    <h1>{}</h1>
    <br>
    <p>{}</p>
    </div>
    <br><br>
    <div style="text-align: center;">
    <h1>{}</h1>
    <br>
    <p>{}</p>
    </div>
    <br><br>
    <div style="text-align: center;">
    <h1>{}</h1>
    <br>
    <p>{}</p>
    </div>
    <br><br>
    <div style="text-align: center;">
    <h1>{}</h1>
    <br>
    <p>{}</p>
    </div>
    <br><br>
    <div style="text-align: center;">






    <h1>{}</h1>
    <br>
    <p>{}</p>
    </div>
</body>
</html>
""".format(
    setup["title"],
    setup["title"],
    setup["description"],
    setup["postname"][0],
    setup["postcontent"][0],
    setup["postname"][1],
    setup["postcontent"][1],
    setup["postname"][2],
    setup["postcontent"][2],
    setup["postname"][3],
    setup["postcontent"][3],
    setup["postname"][4],
    setup["postcontent"][4],
)
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(page, "utf8"))

with HTTPServer(('', int(port)), handler) as server:
    server.serve_forever()
