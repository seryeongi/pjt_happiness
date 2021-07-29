import json
import xml

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import User
from matplotlib import pyplot as plt
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns
# from .forms import LoginForm


from config.settings import DATA_DIRS

df = pd.read_csv(DATA_DIRS[0]+'/data04.csv')
df_exp = pd.read_csv(DATA_DIRS[0]+'/data_express.csv')
df11 = pd.read_csv(DATA_DIRS[0]+'/country11.csv')
df_mp = pd.read_csv(DATA_DIRS[0]+'/pwrinx.csv')
df_il = pd.read_csv(DATA_DIRS[0]+'/raw_literacy.csv')
df_il2 = pd.read_csv(DATA_DIRS[0]+'/literacy_all.csv')
df_illow = pd.read_csv(DATA_DIRS[0]+'/literacy_lowest.csv')
df_mp2 = pd.read_csv(DATA_DIRS[0]+'/happiness_pwrindx.csv')
df_cov = pd.read_csv(DATA_DIRS[0]+'/covid_piechart.csv')
df_cov2 = pd.read_csv(DATA_DIRS[0]+'/covid_monthly_con6.csv')
df_cov3 = pd.read_csv(DATA_DIRS[0]+'/case rate2.csv')
power10 = pd.read_csv(DATA_DIRS[0]+'/country11_literacy.csv')

# Create your views here.
def home(request):

	return render(request, 'index.html')
def index(request):
	context = {}
	if request.method == 'GET':
		fig = plot(px.choropleth(df, locations='country', locationmode='country names',
								 color='score',
								 animation_frame='year',
								 basemap_visible=True,
								 color_continuous_scale='Tropic'
								 ), output_type='div')
		context['plot_div'] = fig
		return render(request,'index.html',context)
		context['login_session'] = False

	elif request.method == 'POST':
		context['login_session'] = False
		id = request.POST.get('user_id')
		pw = request.POST.get('user_pw')
		infos = User.objects.all()
		msg = 'id 혹은 password가 존재하지 않습니다.'
		for info in infos:
			if info.user_id == id and info.user_pw==pw:
				name=info.user_name
				msg = name + '님, 환영합니다.'
				context['login_session'] = True




		context['msg'] = msg
	else:
		context['login_session'] = False
	fig = plot(px.choropleth(df, locations='country', locationmode='country names',
						color='score',
						animation_frame='year',
						basemap_visible=True,
						color_continuous_scale='Tropic'
						),output_type='div')
	context['plot_div'] = fig
	return render(request, 'index.html', context)
def dashboard(request):

	return render(request, 'dashboard.html')
def information(request):

	return render(request, 'information.html')
def info(request):

	return render(request, 'info.html')
def logout(request):
	request.session.flush()
	return render(request, 'index.html')
def test(request):
	fig4 = plot(px.histogram(df, x='social_support_std', nbins=20, animation_frame='year',
							 title='Social support histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="social_support_std", animation_frame='year', color='region',
				  title='Regional social support boxplot', facet_col='region')
	fig3.update_layout(yaxis_range=[-3.2, 2])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')




	return render(request, "test.html",context={'plot_div5': fig3,'plot_div6': fig4})

def table(request):

	return render(request, 'table.html')
def datatable(request):

	return render(request, 'datatable.html')
def regi_done(request):

	return render(request, 'regi_done.html')
def chart(request):

	return render(request, 'chart.html')
def authregister(request):
	if request.method == 'GET':
		return render(request, 'authregister.html')

	elif request.method == 'POST':
		user_id = request.POST.get('id',' ')
		user_pw = request.POST.get('pw', ' ')
		user_pw_confirm = request.POST.get('pw_confirm', ' ')
		user_name = request.POST.get('name', ' ')
		user_email = request.POST.get('email', ' ')

		if(user_id or user_pw or user_pw_confirm or user_name or user_email) == ' ':
			messages.info(request, '입력되지 않은 부분이 존재합니다.')
			return render(request, 'authregister.html')
		elif user_pw != user_pw_confirm:
			return render(request, 'authregister.html')
			messages.info(request, '입력하신 Password가 동일하지 않습니다.')
		else:
			user = User(
				user_id = user_id,
				user_pw = user_pw,
				user_name=user_name,
				user_email=user_email,
			)
			user.save()
		return redirect('/regi_done')

def authforgotpassword(request):

	return render(request, 'authforgotpassword.html')
def summary(request):

	return render(request, 'summary.html')
def social(request):
	fig4 = plot(px.histogram(df, x='social_support_std', nbins=20, animation_frame='year',
                    title='Social support histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="social_support_std", animation_frame='year', color='region',
				  title='Regional social support boxplot', facet_col='region')
	fig3.update_layout(yaxis_range=[-3.2, 2])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df01 = df11[['year', 'country', 'social_support_std']]
	fig1 = plot(
		px.bar(df01, x="social_support_std", y="country", animation_frame="year", color="country", orientation="h",
                    		title='Country11'),output_type='div')
	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							 color='social_support_std',
							 animation_frame='year',
							 basemap_visible=True,
							 color_continuous_scale='Tropic',
                    		title=('World social support map')
							 ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="socialsupport", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title=('Regional social support scatter plot')), output_type='div')
	sss = pd.DataFrame(df_exp['socialsupport'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="socialsupport", animation_frame="year", color="region", barmode="group",
                    		title=('Regional social support bar plot')),
			   output_type='div')
	return render(request, 'social.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def health(request):
	fig4 = plot(px.histogram(df, x='health_std', nbins=20, animation_frame='year',title='Health histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="health_std", animation_frame='year', color='region',
					   title='Regional health boxplot', facet_col='region', )
	fig3.update_layout(yaxis_range=[-3.2, 2])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df02 = df11[['year', 'country', 'health_std']]
	fig1 = plot(px.bar(df02, x="health_std", y="country", animation_frame="year", color="country", orientation="h",
                    		title='Country11'),
				output_type='div')
	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							  color='health_std',
							  animation_frame='year',
							  basemap_visible=True,
							  color_continuous_scale='Tropic',
                    		title='World health map'
							  ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="health", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title='Regional health scatter plot'), output_type='div')
	sss = pd.DataFrame(df_exp['health'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="health", animation_frame="year", color="region", barmode="group",
                    		title=('Regional health bar plot')),
			   output_type='div')
	return render(request, 'health.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def gdp(request):
	fig4 = plot(px.histogram(df, x='gdp_std', nbins=20, animation_frame='year',title='Gdp histogram'), output_type='div')
	fig3 = px.box(df, x='region', y="gdp_std", animation_frame='year', color='region', title='Regional gdp boxplot',
			   facet_col='region')
	fig3.update_layout(yaxis_range=[-3, 3.3])
	fig3.update_xaxes(showticklabels=True, matches=None)
	fig3 = plot(fig3, output_type='div')
	df03 = df11[['year', 'country', 'gdp_std']]
	fig1 = plot(px.bar(df03, x="gdp_std", y="country", animation_frame="year", color="country",title='Country11', orientation="h"),
				output_type='div')

	fig2 = plot(px.choropleth(df, locations='country', locationmode='country names',
							  color='gdp_std',
							  animation_frame='year',
							  basemap_visible=True,
							  color_continuous_scale='Tropic',
                    		title='World Gdp map'
							  ), output_type='div')
	plot_div = plot(
		px.scatter(df_exp, x="gdp", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10],
                    		title='Regional Gdp scatter plot'), output_type='div')
	sss = pd.DataFrame(df_exp['gdp'].groupby([df_exp['year'], df_exp['region']]).mean()).reset_index()
	fig = plot(px.bar(sss, x="region", y="gdp", animation_frame="year", color="region", barmode="group",
                    		title=('Regional gdp bar plot')),
			   output_type='div')
	return render(request, 'gdp.html', context={'plot_div': plot_div,'plot_div2': fig,'plot_div3': fig2,'plot_div4': fig1,'plot_div5': fig3,'plot_div6': fig4})
def etc(request):
	plot_div1 = plot(
		px.scatter(df_exp, x="freedom", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div2 = plot(
		px.scatter(df_exp, x="trust", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	plot_div3 = plot(
		px.scatter(df_exp, x="generosity", y="score", animation_frame="year", animation_group="country", color="list",
				   hover_name="country", facet_col="region",size="area",
				   log_x=False, size_max=30, range_x=[-3, 3], range_y=[0, 10]), output_type='div')
	return render(request, 'etc.html',context={'plot_div1': plot_div1,'plot_div2': plot_div2,'plot_div3': plot_div3,})
def info2(request):

	return render(request, 'info2.html')
def covid19(request):
	df = df_cov[['region', 'cumulative_cases', 'cumulative_cases2', 'pop']]
	fig1 = plot(px.pie(df, values='cumulative_cases', names='region',title="2020 cumulative cases by continent"), output_type='div')

	fig2 = plot(px.pie(df, values='cumulative_cases2', names='region',title="2021 cumulative cases by continent"), output_type='div')

	fig3 = plot(px.area(df_cov2, x="month", y="monthly_cumulative_cases", color="country", line_group="country", title="Country6 monthly cumulative cases"
				  ), output_type='div')


	fig4 = plot(px.area(df_cov2, x="month", y="monthly_cumulative_deaths", color="country", line_group="country", title="Country6 monthly cumulative deaths "
				 ), output_type='div')
	fig5 = plot(px.bar(df_cov3, x="country", y="rate_cases", color="country", title="Case Rate Top 30"), output_type='div')
	fig6 = plot(px.scatter(df_cov3, x="rate_cases", y="score", color="country", title="Case Rate Top 30 scatter plot"), output_type='div')
	fig7 = plot(px.scatter(df_cov3, x="cumulative_cases", y="score", color="country", title="Cumulative cases Top 30 scatter plot"),
				output_type='div')
	return render(request, 'covid19.html', context={'plot_div1': fig1,'plot_div2': fig2,'plot_div3': fig3,'plot_div4': fig4,'plot_div5': fig5,'plot_div6': fig6,'plot_div7': fig7})
def militarypower(request):
	fig2 = px.bar(df_mp2[df_mp2['year'] == 2021].head(10), x="mililtarypower", y="country", color="country",
				  orientation="h",
				  title="2021 PowerIndex Top 10")
	fig2 = plot(fig2, output_type='div')

	fig1 = plot(px.choropleth(df_mp2, locations='country', locationmode='country names',
							  color='mililtarypower',
							  animation_frame='year',
							  basemap_visible=True,
							  color_continuous_scale='armyrose',
							  title=('World military power map')
							  ), output_type='div')


	fig3 = plot(px.scatter(df_mp2, x="total_area", y="mililtarypower", color="country", title="Area~PowerIndex"), output_type='div')

	fig4 = plot(px.scatter(df_mp2, x="pop", y="mililtarypower", color="country", title="Population~PowerIndex"), output_type='div')
	fig5 = plot(px.scatter(power10, x="pwridx", y="score", color="country", title="Population~PowerIndex"), output_type='div')
	fig6 = plot(px.scatter(df_mp2[df_mp2['score'] > df_mp2['score'].mean()], x="mililtarypower", y="score", color="country",
					 title="Powerindex with Upper Happiness Score"), output_type='div')


	fig7 = plot(px.scatter(df_mp2[df_mp2['score'] < df_mp2['score'].mean()], x="mililtarypower", y="score", color="country",
					 title="Powerindex with Lower Happiness Score"), output_type='div')


	return render(request, 'militarypower.html',context={'plot_div1': fig1,'plot_div2': fig2,'plot_div3': fig3,'plot_div4': fig4,'plot_div5': fig5,'plot_div6': fig6,'plot_div7': fig7})
def illiteracyrate(request):
	fig2 = px.bar(df_illow, x='literacy', y='country',
				  orientation='h', color='country',
				  title='LITERACY THE LOWEST 10 (%)'
				  )

	fig2 = plot(fig2, output_type='div')

	fig3 = plot(px.scatter(df_il2, x="literacyrate", y="score", color="region", hover_data=['country'],
						   animation_frame='year'), output_type='div')

	fig1 = plot(px.choropleth(df_il, locations='country', locationmode='country names',
							  color='rate',
							  basemap_visible=True,
							  color_continuous_scale='Tropic',
							  title=('World illiteracy map')

							  ), output_type='div')

	return render(request, 'illiteracyrate.html',context={'plot_div1': fig1,'plot_div2': fig2,'plot_div3': fig3,})
def summary2(request):

	return render(request, 'summary2.html')

# def highchart(request):
#     return HttpResponse(json.dumps(data), content_type='application/json');
