from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)
k_v_store = {}
@app.route("/key-value-store/<key>", methods = ["GET", "DELETE", "PUT"])

def respond_request(key):
    #handle GET requests
    if request.method =="GET":
        if key in k_v_store:
            return make_response(jsonify(message = "Retrieved Successfully", doesExist = True, value=k_v_store[key]))
        else:
            return make_response(jsonify(message = "Retreived Unsuccesfully ", doesExist = False, value=k_v_store[key]))


    # handle PUT requests
    elif request.method == "PUT":
        if 'value' not in request.get_json():
            return make_response(jsonify(message= "Error in PUT", error = "value is missing"), 400)
        if len(key) > 50:
            return make_response(jsonify(message="Error in PUT", error = "key too long"), 400)

        value = request.get_json()['value']
        if key in k_v_store:
            k_v_store[key] = value
            return make_response(jsonify(message = "updated Successfully", replaced = True), 200)
        else:
            k_v_store[key] = value
            return make_response(jsonify(message = "added Successfully", replaced = False), 201)

    # handle DELETE requests
    elif request.method == "DELETE":
        if key in k_v_store:
            k_v_store.pop(key,None)
            return make_response(jsonify(message = "Deleted Successfully", doesExist = True), 200)
        else:
            return make_response(jsonify(message = "Error in DELETE", doesExist = "False", error = "Key does not Exist"), 404)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)

