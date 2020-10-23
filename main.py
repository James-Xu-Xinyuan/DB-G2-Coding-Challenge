from flask import Flask, render_template, request, Response, redirect, url_for
import json
import requests
import DAO_G2
app = Flask(__name__)


def get_data_from_data_gen():
    r = requests.get('http://localhost:8090/getDashboardDisplayDataWeb')
    return json.loads(r.text)

def change_arr_format(arr):
    if arr[0] is None:
        arr[0] = 0
    if arr[1] is None:
        arr[1] = 0
    arr[0] = float(arr[0])
    arr[1] = float(arr[1])
    return arr


@app.route('/')
def hello_world():
    return render_template("sign-in-page.html")


@app.route('/dash', methods=['GET', 'POST'])
def dashboard():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        authenticate = DAO_G2.user_auth(username, password)

        if not authenticate:
            return render_template("error.html")

    data = get_data_from_data_gen()

    avg_buy_all = data['avg_buy_all']
    avg_sell_all = data['avg_sell_all']

    a_buy_sell = list(DAO_G2.get_instrument_latest_avg("Astronomica"))
    a_buy_sell = change_arr_format(a_buy_sell)
    b_buy_sell = list(DAO_G2.get_instrument_latest_avg("Borealis"))
    b_buy_sell = change_arr_format(b_buy_sell)
    c_buy_sell = list(DAO_G2.get_instrument_latest_avg("Celestial"))
    c_buy_sell = change_arr_format(c_buy_sell)
    d_buy_sell = list(DAO_G2.get_instrument_latest_avg("Deuteronic"))
    d_buy_sell = change_arr_format(d_buy_sell)
    e_buy_sell = list(DAO_G2.get_instrument_latest_avg("Eclipse"))
    e_buy_sell = change_arr_format(e_buy_sell)
    f_buy_sell = list(DAO_G2.get_instrument_latest_avg("Floral"))
    f_buy_sell = change_arr_format(f_buy_sell)
    g_buy_sell = list(DAO_G2.get_instrument_latest_avg("Galactia"))
    g_buy_sell = change_arr_format(g_buy_sell)
    h_buy_sell = list(DAO_G2.get_instrument_latest_avg("Heliosphere"))
    h_buy_sell = change_arr_format(h_buy_sell)
    i_buy_sell = list(DAO_G2.get_instrument_latest_avg("Interstella"))
    i_buy_sell = change_arr_format(i_buy_sell)
    j_buy_sell = list(DAO_G2.get_instrument_latest_avg("Jupiter"))
    j_buy_sell = change_arr_format(j_buy_sell)
    k_buy_sell = list(DAO_G2.get_instrument_latest_avg("Koronis"))
    k_buy_sell = change_arr_format(k_buy_sell)
    l_buy_sell = list(DAO_G2.get_instrument_latest_avg("Lunatic"))
    l_buy_sell = change_arr_format(l_buy_sell)

    realized_profit = data['realized_profit']
    expected_profit = data['expected_profit']
    realized_loss = data['realized_loss']
    expected_loss = data['expected_loss']

    historical = DAO_G2.get_latest_deals()
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
