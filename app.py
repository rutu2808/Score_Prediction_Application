import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import ml
from flask import Flask, render_template, request

COUNT=0
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global COUNT

    h0=float(request.form.get('hours0'))
    s0= ml.predicts(h0)
    goal=float(request.form.get('goal'))
    diff=goal-s0
    s0=round(s0, 2)
    diff=round(diff, 2)
    msg=""
    if diff>0:
        msg="Sorry, not enough to reach your goal..Boost yourself! 💪"
    else:
        msg="Great going!! Keep it up.."

    data = {'Your goal': goal, 'Predicted': s0}
    d = list(data.keys())
    score = list(data.values())
    # creating the bar plot
    plt.bar(d, score, color='#c8d5b9', ec="black")

    plt.ylabel("Scores")
    plt.title("Goal Vs. Predicted score")
    plt.tight_layout()


    plt.savefig('static/{}.jpg'.format(COUNT))
    imgname='{}.jpg'.format(COUNT)
    plt.close()
    COUNT += 1
    return render_template("result.html",scores=s0,diff=diff,msg=msg,hour=h0,filename=imgname)

if __name__ == '__main__':
    app.run(debug=True)
