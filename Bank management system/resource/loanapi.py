from model.loan import Loan
import json
import requests
from flask import Flask, request,Response, jsonify
from model.accounts import Accounts
#from resource.customerror import AccountAlreadyExistsError,errors,AccountDoesNotExists
#from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError


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
            return jsonify({"output":"you does not have any loans to update"}),404
    
    @app.route('/Loan/<customer_username>',methods=['DELETE'])
    def delete_loan(customer_username):
        customer=Loan.objects(username=customer_username)
        y=customer.count()
        if y>0:
            #delete the details in mongodb
            customer = Loan.objects(username=customer_username)
            customer.delete()
            return jsonify({"output":"loan has been removed"})
        else:
            return jsonify({"output":"you does not have any loans to delete"}),404

    @app.route('/Loan/<customer_username>',methods=['GET'])
    def get_loan(customer_username):
        # try:
            customer=Loan.objects(username=customer_username)
            # return Response(customer, mimetype="application/json", status=200)
            y=customer.count()
            if y>0:
                return jsonify(customer)
            else:
                # return Response({"output":"you does not have any loans to display"}, mimetype="application/json", status=404)
                return '',404
        # except DoesNotExist:
        #     raise AccountDoesNotExists


    #loan object id based
    
    # @app.route('/loans/<customer_object>',methods=['PUT'])
    # def updates_loan(customer_object):
    #     customer=Loan.objects(_id=customer_object)
    #     y=customer.count()
    #     if y>0:
    #         record = json.loads(request.data)
    #         customer = Loan.objects(username=customer_object)
    #         customer.update(loantype=record['loantype'],loanamount=record['loanamount'],date=record['date'],rateofinterest=record['rateofinterest'],durationofloan=record['durationofloan'],username=record['username'])
    #         return jsonify(customer)
    #     else:
    #         return jsonify({"output":"you does not have any loans to update"}),404
    
    # @app.route('/loans/<customer_object>',methods=['DELETE'])
    # def deletes_loan(customer_object):
    #     customer=Loan.objects(_id=customer_object)
    #     y=customer.count()
    #     if y>0:
    #         #delete the details in mongodb
    #         customer = Loan.objects(username=customer_object)
    #         customer.delete()
    #         return jsonify({"output":"loan has been removed"})
    #     else:
    #         return jsonify({"output":"you does not have any loans to delete"}),404

    @app.route('/loans/user/<objectid>',methods=['GET'])
    def gets_loan(objectid):
        customer =Loan.objects.with_id(objectid)
        if customer != None:
            return jsonify(Loan.objects.with_id(objectid))
        else:
            return '',404
    
    @app.route('/loans/user/<objectid>',methods=['PUT'])
    def updates_loan(objectid):
        record = json.loads(request.data)
        customer =Loan.objects.with_id(objectid)
        if customer != None:
            customer.update(loantype=record['loantype'],loanamount=record['loanamount'],date=record['date'],rateofinterest=record['rateofinterest'],durationofloan=record['durationofloan'],username=record['username'])
            return jsonify({"output":"Loan has been updated"})
        else:
            return '',404
    
    @app.route('/loans/user/<objectid>',methods=['DELETE'])
    def deletes_loan(objectid):
        customer =Loan.objects.with_id(objectid)
        if customer != None:
            customer.delete()
            return jsonify({"output":"Loan has been deleted"})
        else:
            return '',404

