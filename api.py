
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"
        
@app.route('/karyawan', methods=['GET','POST'])
def karyawan():
    if request.method == 'POST':
        datainput = request.json
        print(datainput)
        nama = datainput['nama']
        pekerjaan = datainput['pekerjaan']
        # type_order = datainput['typer_order']

        # Fatih kerja bagian ini







        # end fatih ngerjain 
        data = {
            'pesan': 'Data Berhasil Terkirim!!!',
            'nama':nama
            # 'pekerjaan':pekerjaan,
            # 'usia':usia 
        }
        
        return make_response(jsonify({'data':data}),200)
app.run()