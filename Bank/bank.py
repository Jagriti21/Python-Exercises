import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'accountsdb',
    'host': 'mongodb://localhost:27017/accountsdb',
    
}
db = MongoEngine()
db.init_app(app)

class Accounts(db.Document):
    name=db.StringField()
    username=db.StringField()
    password=db.StringField()
    address=db.StringField()
    state=db.StringField()
    country=db.StringField()
    email=db.StringField()
    pan=db.StringField()
    contact=db.StringField()
    DOB=db.StringField()
    accounttype=db.StringField()


class Loan(db.Document):
    loantype=db.StringField()
    loanamount=db.StringField()
    date=db.StringField()
    rateofinterest=db.StringField()
    durationofloan=db.IntField()
    username=db.StringField()#user_id

@app.route('/')
def basic():
    return "welcome to the bank management system"

@app.route('/Account',methods=['POST','GET'])
def register_customer():
    if request.method == 'POST':
        record = json.loads(request.data)
        x=Accounts.objects(username=record['username'])
        y=x.count()
        if y>0:
            return jsonify({"output":"Username already exists.please provide another!!"}),403
        else:
            customer = Accounts(name=record['name'],username=record['username'],password=record['password'],address=record['address'],state=record['state'],country=record['country'],email=record['email'],pan=record['pan'],contact=record['contact'],DOB=record['DOB'],accounttype=record['accounttype'])
            return jsonify(customer.save())
    else:
        return jsonify(Accounts.objects())

@app.route('/Account/<customer_id>',methods=['GET','PUT','DELETE'])
def account_details(customer_id):
    # record = json.loads(request.data)
    x=Accounts.objects(username=customer_id)
    y=x.count()
    if y>0:
        if request.method == 'PUT':
            #update the details in mongodb
            record = json.loads(request.data)
            customer = Accounts.objects(username=customer_id)
            customer.update(name=record['name'],username=record['username'],password=record['password'],address=record['address'],state=record['state'],country=record['country'],email=record['email'],pan=record['pan'],contact=record['contact'],DOB=record['DOB'],accounttype=record['accounttype'])
            return jsonify(customer)
        elif request.method == 'DELETE':
            #delete the details in mongodb
            customer = Accounts.objects(username=customer_id)
            customer.delete()
            return jsonify(customer)
        else:
            #get the updated details of single resource
            return jsonify(Accounts.objects(username=customer_id))
    else:
        #customer not found
        return "user does not exists",404

@app.route('/Loan',methods=['POST','GET'])
def apply_loan():
    if request.method == 'POST':
        record = json.loads(request.data)
        x=Accounts.objects(username=record['username'])
        y=x.count()
        if y>0:
            customer = Loan(loantype=record['loantype'],loanamount=record['loanamount'],date=record['date'],rateofinterest=record['rateofinterest'],durationofloan=record['durationofloan'],username=record['username'])
            return jsonify(customer.save())
        else:
            return jsonify({"output":"Username does not exists. please register to apply loan"})
    else:
        return jsonify(Loan.objects())


@app.route('/Loan/<customer_username>',methods=['GET'])
def user_loan(customer_username):
    customer=Loan.objects(username=customer_username)
    y=customer.count()
    if y>0:
        return jsonify(customer)
    else:
        return jsonify({"output":"you does not have any loans to display"}),404


@app.route('/Loan/<customer_username>',methods=['DELETE'])
def delete_loan(customer_username):
    #delete the details in mongodb
    customer = Loan.objects(username=customer_username)
    y=customer.count()
    if y>0:
        customer.delete()
        return jsonify(customer)
    else:
        return jsonify({"output":"loan don't exist"}),404


if __name__ == "__main__":
    app.run(debug=True)