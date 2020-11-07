from model.loan import Loan
import json
import requests
from flask import Flask, request, jsonify
from model.accounts import Accounts

def loan_api(app):
    
    @app.route('/Loan',methods=['POST'])
    def create_loan():
            record = json.loads(request.data)
            x=Accounts.objects(username=record['username'])
            y=x.count()
            if y>0:
                customer = Loan(loantype=record['loantype'],loanamount=record['loanamount'],date=record['date'],rateofinterest=record['rateofinterest'],durationofloan=record['durationofloan'],username=record['username'])
                return jsonify(customer.save())
            else:
                return jsonify({"output":"Username does not exists. please register to apply loan"}),404

    @app.route('/Loan',methods=['GET'])
    def get_loans():
        return jsonify(Loan.objects())
    
    @app.route('/Loan/<customer_username>',methods=['PUT'])
    def update_loan(customer_username):
        customer=Loan.objects(username=customer_username)
        y=customer.count()
        if y>0:
            record = json.loads(request.data)
            customer = Loan.objects(username=customer_username)
            customer.update(loantype=record['loantype'],loanamount=record['loanamount'],date=record['date'],rateofinterest=record['rateofinterest'],durationofloan=record['durationofloan'],username=record['username'])
            return jsonify(customer)
        else:
            return jsonify({"output":"you does not have any loans to update"})
    
    @app.route('/Loan/<customer_username>',methods=['DELETE'])
    def delete_loan(customer_username):
        customer=Loan.objects(username=customer_username)
        y=customer.count()
        if y>0:
            #delete the details in mongodb
            customer = Loan.objects(username=customer_username)
            customer.delete()
            return jsonify(customer)
        else:
            return jsonify({"output":"you does not have any loans to delete"}),404

    @app.route('/Loan/<customer_username>',methods=['GET'])
    def get_loan(customer_username):
        customer=Loan.objects(username=customer_username)
        y=customer.count()
        if y>0:
            return jsonify(customer)
        else:
            return jsonify({"output":"you does not have any loans to display"}),404
    
