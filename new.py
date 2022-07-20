from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route('/shalini1',methods=['POST'])
def math_post_():
    if(request.method=='POST'):
        name=request.json['name']
        email = request.json['email']
        phoneno = request.json['phoneno']

        return jsonify(name+email+str(phoneno))
@app.route('/first',methods=['POST'])
def new():
    if(request.method=='POST'):
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        s=num1*num2
        return jsonify(s)
@app.route('/ss')
def hello_world():
    return 'This is my first API call!'

if __name__=='__main__':
    app.run()


