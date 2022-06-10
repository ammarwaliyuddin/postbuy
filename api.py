
from flask import Flask, jsonify, request, make_response
import base64

app = Flask(__name__)
app.config["DEBUG"] = True

def base64_decode(data):
  base64_string = data
  base64_bytes = base64_string.encode("ascii")

  sample_string_bytes = base64.b64decode(base64_bytes)
  sample_string = sample_string_bytes.decode("ascii")
  return sample_string
  

# @app.route("/")
# def home_view():
#         return "<h1>Welcome to Geeks for Geeks</h1>"
        
@app.route('/karyawan', methods=['GET','POST'])
def karyawan():
    if request.method == 'POST':
        datainput = request.json
        print(datainput)
        
        advertiser = datainput['advertiser']
        year = datainput['year']
        month = datainput['month']
        no_po = base64_decode(datainput['no_po'])
        type_order = datainput['type_order']
        # Fatih kerja bagian ini


        # end fatih ngerjain 
        data = {
            'pesan': True,
            'advertiser' : advertiser,
            'year' :year,
            'month' :month,
            'no_po' :no_po,
            'type_order' :type_order
        }
        
        return make_response(jsonify({'data':data}),200)
app.run()