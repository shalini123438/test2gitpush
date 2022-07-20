from flask import Flask,render_template,request,jsonify
app=Flask(__name__)


@app.route('/via_ssj',methods=['POST'])
def math_postman():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if (operation == 'add'):
            r = num1 + num2
            res = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'sub'):
            r = num1 - num2
            res = 'the sub of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'mul'):
            r = num1 * num2
            res = 'the mul of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'div'):
            r = num1 / num2
            res = 'the div of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return jsonify(res)

if __name__=='__main__':
    app.run()


