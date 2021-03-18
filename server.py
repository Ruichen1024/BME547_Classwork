from flask import Flask, request, jsonify
from blood_test import analyze_HDLdata


app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def server_status():
    return "The server is on."


@app.route("/info", methods=["GET"])
def information():
    output = "This server will allow user to request blood analysis"
    return output


@app.route("/HDL", methods=["POST"])
def HDl_request():
    """
        input_info: {"HDL": 60}
    """
    in_data = request.get_json()
    print(in_data)
    HDL = in_data["HDL"]
    result = analyze_HDLdata(HDL)
    # return "The blood HDL level of {} is {}.".format(HDL, result)
    answer = {"HDL": HDL, "Analysis": result}
    if answer != "Normal":
        return "Bad HDL", 400
    return jsonify(answer)


@app.route("/say_hello/<person>/<age>", methods=["GET"])
def say_hello(person, age):
    next_age = int(age) + 1
    output = "Hello there, {}! You will be {} years old next year"\
        .format(person, next_age)
    return output

if __name__ == "__main__":
    app.run()
