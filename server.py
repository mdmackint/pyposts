from http.server import BaseHTTPRequestHandler, HTTPServer
import json
x = open("setup.json")
setup = x.read()
x.close()
setup = json.loads(setup)
del x
names = setup["postname"]
contents = setup["postcontent"]
class Post():
    def __init__(self,title,content):
        self.title = title
        self.content = content
z = list()
index = 0
for y in names:
    a = contents[index]
    z.append(Post(y,a))
    index = index + 1
posthtml = list()
for b in z: posthtml.append("<div style=\"text-align: center;\"><h1>{}</h1><p>{}</p></div>".format(b.title, b.content))
port = input("Please select a port for the server: ")
d = ""
for c in posthtml:
    d = d + c
posthtml = d
htmlpage = """
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
    margin: 0px;
    }}
    .header {{
        width: 100%;
        height: 33%;
        background: rgb(0,11,255);
        background: linear-gradient(146deg, rgba(0,11,255,1) 0%, rgba(255,244,0,1) 100%); 
    }}
    </style>
</head>
<body>
<div class="header">
    <span style="height: 120%;font-size: 2em; font-weight: bold; text-align: left; margin-left: 3%; margin-top: 0%; color: #fff400;">{}</span>
    <span style="text-align: right; margin-right: 3%; margin-top: 0.5%; color: #000bff; float: right;">{}</span>
    
    <h1 style="text-align: center;color: white;">Posts</h1>
    <br>
    </div>
    <hr>
    <br>
    {}
</body>
</html>
""".format(setup["title"], setup["title"], setup["description"], posthtml)
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(418)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(bytes(htmlpage, "utf8"))

with HTTPServer(('', int(port)), handler) as server:
    server.serve_forever()
