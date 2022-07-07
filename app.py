from flask import Flask ,jsonify,request

app = Flask(__name__)
@app.route("/")
def helloWorld():
    return "Hello World"

tasks = [
    {
        'Contact':"9987644456",
        'Name':'Raju',
        'done':false,
        'id':1
    },
    {
        'Contact':"9876543222",
        'Name':'Rahul',
        'done':false,
        'id': 2      
    }
]

@app.route("/add-data")
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'contact':request.json['contact'],
        'name':request.json.get('name'"")
    }
    tasks.append(task)
    return jsonify({
        "status":"Sucess",
        "message":"Task added successfully"
    })

@app.route("/get-data")
def getTask():
    return jsonify({
        "data":tasks
    })

if __name__ == "__main__":
    app.run(debug = True)

