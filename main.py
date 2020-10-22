from flask import Flask, render_template, request, Response, redirect, url_for
import json
import requests
app = Flask(__name__)


def get_data_from_data_gen():
    r = requests.get('http://localhost:8090/getDashboardDisplayDataWeb')
    return json.loads(r.text)



@app.route('/')
def hello_world():
    return render_template("sign-in-page.html")


@app.route('/dash', methods=['GET', 'POST'])
def dashboard():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

    data = get_data_from_data_gen()

    avg_buy_all = data['avg_buy_all']
    avg_sell_all = data['avg_sell_all']

    a_buy_sell = data['a_buy_sell']
    b_buy_sell = data['b_buy_sell']
    c_buy_sell = data['c_buy_sell']
    d_buy_sell = data['d_buy_sell']
    e_buy_sell = data['e_buy_sell']
    f_buy_sell = data['f_buy_sell']
    g_buy_sell = data['g_buy_sell']
    h_buy_sell = data['h_buy_sell']
    i_buy_sell = data['i_buy_sell']
    j_buy_sell = data['j_buy_sell']
    k_buy_sell = data['k_buy_sell']
    l_buy_sell = data['l_buy_sell']

    realized_profit = data['realized_profit']
    expected_profit = data['expected_profit']
    realized_loss = data['realized_loss']
    expected_loss = data['expected_loss']

    historical = data['historical']
    deal_data = data['deal_data']

    return render_template("dashboard.html", avg_buy_all=avg_buy_all, avg_sell_all=avg_sell_all,
                           a_buy_sell=a_buy_sell, b_buy_sell=b_buy_sell, c_buy_sell=c_buy_sell,
                           d_buy_sell=d_buy_sell, e_buy_sell=e_buy_sell, f_buy_sell=f_buy_sell,
                           g_buy_sell=g_buy_sell, h_buy_sell=h_buy_sell, i_buy_sell=i_buy_sell,
                           j_buy_sell=j_buy_sell, k_buy_sell=k_buy_sell, l_buy_sell=l_buy_sell,
                           realized_profit=realized_profit, expected_profit=expected_profit,
                           realized_loss=realized_loss, expected_loss=expected_loss,
                           historical=historical, deal_data=deal_data)


# @app.route('/dashboardDisplay')
# def dashboard_display():
#     return render_template("dashboard.html")


@app.route('/user')
def user_Data():
    return render_template("user_Data.html")


@app.route('/testConnection')
def testConn():
    # r = requests.get('http://localhost:8090/client/testservice')
    # return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

    r = requests.get('http://localhost:8090/printHelloWorldWeb')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")


if __name__ == "__main__":
    app.run(debug=True)
