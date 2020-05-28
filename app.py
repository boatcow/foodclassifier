from flask import *
from fastai.vision import *
from fastai.metrics import error_rate
import os

app = Flask(__name__)

p = os.environ.get('PORT', 5000)
@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/take', methods=['GET', 'POST'])
def take():
    if(request.method == 'POST'):
        if request.files:
            print("image chosen")
            f = request.files['file']
            #f.save(f.filename)
            path = Path('')

            defaults.device = torch.device(device)
            img = open_image(f)
            learn = load_learner(path)
            
            ans, idx, outputs = learn.predict(img)
            ans = str(ans)
            
            d_food = {
                "food": ans
            }
            return jsonify(d_food)
if __name__ == "__main__":
    device = 'cpu'
    app.run(host='0.0.0.0', port=p, debug=True)
