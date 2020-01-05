from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

df = pd.read_csv('C:/Users/Administrator.USER-20190824NZ/PycharmProjects/flask1/all.csv', encoding='gbk')
regions_available = list(df.country.dropna().unique())
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/map', methods=['GET'])
def map():
    return render_template('render.html')


@app.route('/', methods=['GET'])
def money():
    data_str = df.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/search', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df.query("country=='{}'".format(the_region))
    df_summary = dfs.groupby("country").agg({"country": "count", "2018年年收入": "sum", "2018年人口总数": "mean"}).sort_values(
        by="country", ascending=False)
    print(df_summary.head(5))  # 在后台检查描述性统计
    ## user select
    # print(dfs)
    # 交互式可视化画图
    fig = dfs.iplot(kind="bar", x="country", y="2018年生产总值", asFigure=True)
    py.offline.plot(fig, filename="example.html", auto_open=False)
    with open("example.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    # plotly.offline.plot(data, filename='file.html')
    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

@app.route('/', methods=['GET'])
def hu_run_2019():
    data_str = df.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/tochart', methods=['POST'])
def region_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df.query("country=='{}'".format(the_region))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )
if __name__ == '__main__':
    app.run(debug=True, port=8000)

