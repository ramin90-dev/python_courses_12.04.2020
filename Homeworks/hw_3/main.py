from flask import Flask,request
from db import run_query, ordering

app = Flask(__name__)

@app.route('/names/')
def names():
    query = '''
    Select count(distinct FirstName) from customers;
    '''
    return str(run_query(query))

@app.route('/tracks/')
def tracks():
    query = '''
    Select count(*) from tracks;
    '''
    return str(run_query(query))

@app.route('/tracks-sec/')
def tracks_sec():
    query = '''
    Select Name,(Milliseconds/1000) from tracks;
    '''
    return str(run_query(query))

@app.route('/customers/')
def customers():
    query = '''
    Select * from customers
    '''
    country = request.args.get('country')
    if country:
        param = f" where country = '{country}'"
        query+=param

    id = request.args.get('id')
    if id:
        param = f" where CustomerId ='{id}'"
        query+=param

    order = request.args.get('ordering')
    if order:
        param = f" Order by '{ordering(order)}'"
        query+=param

    query+= ';'
    return str(run_query(query))


if __name__=='__main__':
    app.run(port=5050)
