from flask import Flask,jsonify,request

app = Flask(__name__)
#@app.route('/')


#def hello_world():
   # return('HELLO WORLD')


tasks = [
    {
        'id':1,
        'title':u'buygroceries',
        'disciption':u'milk , pizza , fruit',
        'done':False
    },

    {
        'id':2,
        'title':u"learnpython",
        'disciption':u"needtofindgoodtutorial",
        'done':False
    }
]

@app.route('/add-data' , method = ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            'status':'Error',
            'Message':'Please provide data'
        }, 400)
    task = {
        'id':tasks[-1]['id'] +1,
       'title':request.json['title'],
       'discription':request.json.get('discription' , ''),
       'done':False
    } 
    tasks.append(task)
    return jsonify({
     'status':'Success',
     'Message': 'success'
    }
    )

@app.route('/get-data')

def get_task():
    return jsonify({
        'data':tasks
    })

if(__name__ == '__main__'):
    app.run(debug = True)
