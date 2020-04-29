from flask import Flask, request
from requirements import requirements
from cosmonaut import numberaustro
from generate_users import users_addres
from csv_mean import avg


app = Flask(__name__)


@app.route('/reguirements/')
def read_txt():
    return requirements()

@app.route('/generate-users/')
def generate_users():
    leng = int(request.args['leng'])
    return users_addres(leng)



@app.route('/space/')
def cosmonaut():
    return str(numberaustro())


@app.route("/mean/")
def mean() -> str:
    result = avg().split(',')
    result = f'Medium height: {result[0]} \n Average weight: {result[1]}'
    return result


if __name__ == '__main__':
    app.run(port=5050)