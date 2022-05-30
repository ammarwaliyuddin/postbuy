from flask import Flask, render_template,send_file
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

fig,ax=plt.subplots(figsize=(6,6))
ax=sns.set(style="darkgrid")
# x=[i for i in range(100)]
# y=[i for i in range(100)]

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    
    return render_template('index.html')
   
    # sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

    # plt.show()
    # sns.set_theme(style="ticks")
    # df = sns.load_dataset("penguins")
    # sns.pairplot(df, hue="species")
    # plt.show()
    
    # return '<h1>hallo</h1>'
    # plt.show()


@app.route('/visualize')
def visualize():
    # sns.lineplot(x,y)
    sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
    canvas=FigureCanvas(fig)

    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img,mimetype='img/png')

    
app.run()