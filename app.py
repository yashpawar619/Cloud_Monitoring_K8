import sys
print(sys.executable)
import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
# Used because Flask app wouldn't have a defined route for the root URL ("/"). This means accessing the homepage of your app would result in a "404 Not Found" error because Flask wouldn't know what to serve for that URL
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    Message = None
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html",cpu_metric=cpu_metric, mem_metric=mem_metric, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')