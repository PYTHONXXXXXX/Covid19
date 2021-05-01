
from flask import Flask,render_template,request


from pyecharts import options as opts
from pyecharts.charts import Bar
import webbrowser

from updating import read_all_row,generate_all,generate_one_country
app = Flask(__name__, static_folder="templates")
country=generate_all(read_all_row(),0)
cases=generate_all(read_all_row(),1)
deaths=generate_all(read_all_row(),2)

def bar_base(country,cases,deaths,count) -> Bar:
    
    c = (
        Bar()
        .add_xaxis([next(country) for _ in range(count)])
        .add_yaxis("Cases", [next(cases) for _ in range(count)])
        .add_yaxis("Deaths", [next(deaths) for _ in range(count)])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Covid19", subtitle="covid19 information"))
    )
    return c


@app.route("/")
def index():
    return render_template("index_.html")


@app.route("/barChart")
def get_bar_chart():
    
    c = bar_base(country,cases,deaths,5)
    return c.dump_options_with_quotes()
@app.route("/barChart/pick")
def get_bar_chart_pick():
    country_=generate_one_country(request.values['Country'],0)
    cases_=generate_one_country(request.values['Country'],1)
    deaths_=generate_one_country(request.values['Country'],2)
    c = bar_base(country_,cases_,deaths_,1)
    return c.dump_options_with_quotes()
 

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000')
    app.run()
    