from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/math/<int:a>/<int:b>', methods = ['GET' , 'POST'] )
def math(a,b):
    result = {"Sum is " : a+b,
              "Sub is " : a-b,
              "Product is ": a*b,
             }
    return jsonify(result) 


   

@app.route('/fact/<int:n>', methods = ['GET' , 'POST'] )
def fact(n):
    result = {"Factorial is" : fact_call(n),}

    return jsonify(result)

  
def fact_call(n):
    if(n==1):
        return n
    else:
        return n*(fact_call(n-1))




if __name__== "__main__":
    app.run(debug=True)



  