import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash_table import DataTable
import pandas as pd
from numpy import *

########### Define your variables

def generate_defaults():
    global prain,pdetector,pmold,psugar,risktol,riskave,nonbcase,\
    bcase,bottles,salesthin,salesnow,salesbulk,sales25,sales20,\
    sales07,salesb,repdamage,repb,costdata,costspores,pacid
    
    prain=0.666667
    pacid=0.8
    pdetector=0.8
    pmold=0.4
    psugar=0.5
    risktol=72000
    riskave=1/risktol
    nonbcase=1000
    bcase=700
    bottles=12
    salesthin=20
    salesnow=29
    salesbulk=10
    sales25=35
    sales20=30
    sales07=25
    salesb=80
    repdamage=250000
    repb=150000
    costdata=10000
    costspores=100000
    
def generate_valuetables():
    global sporesonlytable,dataonlytable,sporesanddatatable,harvestnowtable,\
    nosporesnodatatable
    
    sporesonlytable = []
    sporesonlytable.append(bcase*bottles*salesb+repb-costspores)
    #sporesonlytable.append(nonbcase*bottles*salesbulk-costspores)
    #sporesonlytable.append(0-costspores)
    #sporesonlytable.append(nonbcase*bottles*salesthin-costspores-repdamage)  
    sporesonlytable.append(nonbcase*bottles*sales25-costspores)
    sporesonlytable.append(nonbcase*bottles*sales20-costspores)
    sporesonlytable.append(nonbcase*bottles*sales07-costspores)
    
    dataonlytable = []
    dataonlytable.append(bcase*bottles*salesb+repb-costdata)
    dataonlytable.append(nonbcase*bottles*salesbulk-costdata)
    dataonlytable.append(0-costdata)
    dataonlytable.append(nonbcase*bottles*salesthin-costdata-repdamage)  
    dataonlytable.append(nonbcase*bottles*sales25-costdata)
    dataonlytable.append(nonbcase*bottles*sales20-costdata)
    dataonlytable.append(nonbcase*bottles*sales07-costdata)
    
    sporesanddatatable = []
    sporesanddatatable.append(bcase*bottles*salesb+repb-costspores-costdata)
    #sporesanddatatable.append(nonbcase*bottles*salesbulk-costspores-costdata)
    #sporesanddatatable.append(0-costdata-costspores)
    #sporesanddatatable.append(nonbcase*bottles*salesthin-costdata-costspores-repdamage)  
    sporesanddatatable.append(nonbcase*bottles*sales25-costdata-costspores)
    sporesanddatatable.append(nonbcase*bottles*sales20-costdata-costspores)
    sporesanddatatable.append(nonbcase*bottles*sales07-costdata-costspores)
    
    nosporesnodatatable = []
    nosporesnodatatable.append(bcase*bottles*salesb+repb)
    nosporesnodatatable.append(nonbcase*bottles*salesbulk)
    nosporesnodatatable.append(0-costdata)
    nosporesnodatatable.append(nonbcase*bottles*salesthin-repdamage)  
    nosporesnodatatable.append(nonbcase*bottles*sales25)
    nosporesnodatatable.append(nonbcase*bottles*sales20)
    nosporesnodatatable.append(nonbcase*bottles*sales07)
    
    harvestnowtable = []
    harvestnowtable.append(nonbcase*bottles*salesnow)
    
    global valuetable
    valuetable = sporesonlytable + dataonlytable + sporesanddatatable + \
    nosporesnodatatable + harvestnowtable
    
def generate_utables():
    global usporesonlytable,udataonlytable,usporesanddatatable,uharvestnowtable,utable,\
    unosporesnodatatable

    usporesonlytable = []
    usporesonlytable.append(-exp(-(bcase*bottles*salesb+repb-costspores)*riskave))
    #usporesonlytable.append(-exp(-(nonbcase*bottles*salesbulk-costspores)*riskave))
    #usporesonlytable.append(-exp(-(0-costspores)*riskave))
    #usporesonlytable.append(-exp(-(nonbcase*bottles*salesthin-costspores-repdamage)*riskave))
    usporesonlytable.append(-exp(-(nonbcase*bottles*sales25-costspores)*riskave))
    usporesonlytable.append(-exp(-(nonbcase*bottles*sales20-costspores)*riskave))
    usporesonlytable.append(-exp(-(nonbcase*bottles*sales07-costspores)*riskave))
    
    udataonlytable = []
    udataonlytable.append(-exp(-(bcase*bottles*salesb+repb-costdata)*riskave))
    udataonlytable.append(-exp(-(nonbcase*bottles*salesbulk-costdata)*riskave))
    udataonlytable.append(-exp(-(0-costdata)*riskave))
    udataonlytable.append(-exp(-(nonbcase*bottles*salesthin-costdata-repdamage)*riskave))
    udataonlytable.append(-exp(-(nonbcase*bottles*sales25-costdata)*riskave))
    udataonlytable.append(-exp(-(nonbcase*bottles*sales20-costdata)*riskave))
    udataonlytable.append(-exp(-(nonbcase*bottles*sales07-costdata)*riskave))
    
    usporesanddatatable = []
    usporesanddatatable.append(-exp(-(bcase*bottles*salesb+repb-costspores-costdata)*riskave))
    #usporesanddatatable.append(-exp(-(nonbcase*bottles*salesbulk-costspores-costdata)*riskave))
    #usporesanddatatable.append(-exp(-(0-costspores-costdata)*riskave))
    #usporesanddatatable.append(-exp(-(nonbcase*bottles*salesthin-costspores-costdata-repdamage)*riskave))
    usporesanddatatable.append(-exp(-(nonbcase*bottles*sales25-costspores-costdata)*riskave))
    usporesanddatatable.append(-exp(-(nonbcase*bottles*sales20-costspores-costdata)*riskave))
    usporesanddatatable.append(-exp(-(nonbcase*bottles*sales07-costspores-costdata)*riskave))
    
    unosporesnodatatable = []
    unosporesnodatatable.append(-exp(-(bcase*bottles*salesb+repb)*riskave))
    unosporesnodatatable.append(-exp(-(nonbcase*bottles*salesbulk)*riskave))
    unosporesnodatatable.append(-exp(-(0-costdata)*riskave))
    unosporesnodatatable.append(-exp(-(nonbcase*bottles*salesthin-repdamage)*riskave))
    unosporesnodatatable.append(-exp(-(nonbcase*bottles*sales25)*riskave))
    unosporesnodatatable.append(-exp(-(nonbcase*bottles*sales20)*riskave))
    unosporesnodatatable.append(-exp(-(nonbcase*bottles*sales07)*riskave))
    
    uharvestnowtable = []
    uharvestnowtable.append(-exp(-(nonbcase*bottles*salesnow)*riskave))
    
    utable = []
    utable = usporesonlytable + udataonlytable + usporesanddatatable + \
    unosporesnodatatable + uharvestnowtable
        
    global normusporesonlytable
    normusporesonlytable = []
    i = 0
    while i < len(usporesonlytable):
        normusporesonlytable.append((usporesonlytable[i]-min(utable))/(max(utable)-min(utable)))
        i+=1
        
    global normudataonlytable
    normudataonlytable = []
    i = 0
    while i < len(udataonlytable):
        normudataonlytable.append((udataonlytable[i]-min(utable))/(max(utable)-min(utable)))
        i+=1
        
    global normusporesanddatatable
    normusporesanddatatable = []
    i = 0
    while i < len(usporesanddatatable):
        normusporesanddatatable.append((usporesanddatatable[i]-min(utable))/(max(utable)-min(utable)))
        i+=1
        
    global normunosporesnodatatable
    normunosporesnodatatable = []
    i = 0
    while i < len(unosporesnodatatable):
        normunosporesnodatatable.append((unosporesnodatatable[i]-min(utable))/(max(utable)-min(utable)))
        i+=1
        
    global normuharvestnowtable
    normuharvestnowtable = []
    normuharvestnowtable.append((uharvestnowtable[0]-min(utable))/(max(utable)-min(utable)))
    
    global normutable
    normutable = normusporesonlytable + normudataonlytable + normusporesanddatatable +\
                                 normunosporesnodatatable + normuharvestnowtable

def generate_CEs():
    global ubuydata,ubuyspores,ubuydataandspores,ubuynothing,uharvestnow,\
    buydata,buyspores,buydataandspores,buynothing,harvestnow,valueresults
    
    ubuyspores = []
    ubuyspores.append(prain*usporesonlytable[0]+(1-prain)*(pacid*(psugar*\
                     (usporesonlytable[1])+(1-psugar)*(usporesonlytable[2]))\
                     +(1-pacid)*(usporesonlytable[3])))
    ubuydata = []
    ubuydata.append(pdetector*(pmold*(udataonlytable[0])+(1-pmold)*(max(udataonlytable[1],udataonlytable[2],udataonlytable[3])))\
    +(1-pdetector)*(pacid*(psugar*(udataonlytable[4])+(1-psugar)*(udataonlytable[5]))+(1-pacid)*(udataonlytable[6])))

    ubuydataandspores = []
    ubuydataandspores.append(pdetector*usporesanddatatable[0]+(1-pdetector)*(pacid*(psugar*\
                     (usporesanddatatable[1])+(1-psugar)*(usporesanddatatable[2]))\
                     +(1-pacid)*(usporesanddatatable[3])))
    
    ubuynothing = []
    ubuynothing.append(prain*(pmold*(unosporesnodatatable[0])+(1-pmold)*\
                (max(unosporesnodatatable[1],unosporesnodatatable[2],unosporesnodatatable[3])))\
                +(1-prain)*(pacid*(psugar*(unosporesnodatatable[4])+(1-psugar)*\
                (unosporesnodatatable[5]))+(1-pacid)*(unosporesnodatatable[6])))
    
    uharvestnow = []
    uharvestnow.append(uharvestnowtable[0])
    
    buyspores = -risktol*log(-ubuyspores[0])
    buydata = -risktol*log(-ubuydata[0])
    buydataandspores = -risktol*log(-ubuydataandspores[0])
    buynothing = -risktol*log(-ubuynothing[0])
    harvestnow = -risktol*log(-uharvestnow[0])
    
    valueresults = [str(int(round(harvestnow))),str(int(round(buynothing))),\
                    str(int(round(buyspores))),str(int(round(buydata))),str(int(round(buydataandspores)))]



def generate_means():
    global Ebuydata,Ebuyspores,Ebuydataandspores,Ebuynothing,Eharvestnow,Evalueresults
    
    Ebuyspores = prain*sporesonlytable[0]+(1-prain)*(pacid*(psugar*\
                     (sporesonlytable[1])+(1-psugar)*(sporesonlytable[2]))\
                     +(1-pacid)*(sporesonlytable[3]))
        
    Ebuydata = pdetector*(pmold*(dataonlytable[0])+(1-pmold)*(max(dataonlytable[1],dataonlytable[2],dataonlytable[3])))\
    +(1-pdetector)*(pacid*(psugar*(dataonlytable[4])+(1-psugar)*(dataonlytable[5]))+(1-pacid)*(dataonlytable[6]))

    Ebuydataandspores = pdetector*sporesanddatatable[0]+(1-pdetector)*(pacid*(psugar*\
                     (sporesanddatatable[1])+(1-psugar)*(sporesanddatatable[2]))\
                     +(1-pacid)*(sporesanddatatable[3]))
    
    Ebuynothing = prain*(pmold*(nosporesnodatatable[0])+(1-pmold)*\
                (max(nosporesnodatatable[1],nosporesnodatatable[2],nosporesnodatatable[3])))\
                +(1-prain)*(pacid*(psugar*(nosporesnodatatable[4])+(1-psugar)*\
                (nosporesnodatatable[5]))+(1-pacid)*(nosporesnodatatable[6]))
    
    Eharvestnow = harvestnowtable[0]
    Evalueresults = [str(round(Eharvestnow)),str(round(Ebuynothing)),\
                     str(round(Ebuyspores)),str(round(Ebuydata)),str(round(Ebuydataandspores))]

def generate_dataframe(Evalueresults,valueresults):
    Row1 = ['Average Profit']
    Row2 = ['Certain Equivalent']
    Row1 = Row1 + Evalueresults
    Row2 = Row2 + valueresults
    return pd.DataFrame([Row1, Row2])

generate_defaults()
generate_valuetables()
generate_utables() 
generate_CEs()
generate_means()
df = generate_dataframe(Evalueresults,valueresults)

global col
col = [
    {"id": '0', "name": " "},
    {"id": '1', "name": "Harvest Now"},
    {"id": '2', "name": "Buy Nothing and Wait"},
    {"id": '3', "name": "Buy Spores Only"},
    {"id": '4', "name": "Buy Data Only"},
    {"id": '5', "name": "Buy Data and Spores"}]

tabtitle='Decision Support Tool'
myheading='AK and Partners Consulting'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H4(myheading),
    html.Div(id='prain-container',children='Probability of Rain: 0.66'),
    dcc.Slider(
        id='prain-slider',
        min=0,
        max=1,
        step=0.01,
        value=0.66,
    ),
    html.Div(id='risktol-container',children='Risk Tolerance: $72000'),
    dcc.Slider(
        id='risktol-slider',
        min=1,
        max=1000000,
        step=1000,
        value=72000,
    ),
    
    html.H4(children='Decision Visualization'),
    dcc.Graph(
        id='coagraph',
        figure={
            'data': [
                {'x': ["Harvest Now","Buy Nothing and Wait","Buy Spores Only",\
                      "Buy Data Only","Buy Data and Spores"], 'y': valueresults,\
                    'type': 'bar', 'name': 'Certain Equivalent'},
               {'x': ["Harvest Now","Buy Nothing and Wait","Buy Spores Only",\
                      "Buy Data Only","Buy Data and Spores"], 'y': Evalueresults,\
                   'type': 'bar', 'name': 'Average Payoff'},
            ],
            'layout': {
                'title': ' '
            }
        }
    ),
    html.H4(children='Decision Matrix'),
    
    DataTable(
    id='table',
    columns = col,
    data = df.to_dict('rows')
    ),

    html.A('www.github.com/mdm4061/dashproject', href='www.github.com/mdm4061/dashproject'),
    html.Br(),
    ]
)

@app.callback(
    Output('prain-container', 'children'),
    [Input('prain-slider', 'value')])
def update_rain(value):
    return 'Probability of Rain: {}'.format(value)

@app.callback(
    Output('risktol-container', 'children'),
    [Input('risktol-slider', 'value')])
def update_rain(value):
    return 'Risk Tolerance: ${}'.format(value)

@app.callback(
    Output('coagraph', 'figure'),
    [Input('prain-slider', 'value'),
     Input('risktol-slider', 'value')])
def update_graph(prain1,risktol):
    global riskave
    riskave=1/risktol
    global prain
    prain=prain1
    generate_valuetables()
    generate_utables() 
    generate_CEs()
    generate_means()
    df = generate_dataframe(Evalueresults,valueresults)
    return {
            'data': [
                {'x': ["Harvest Now","Buy Nothing and Wait","Buy Spores Only",\
                      "Buy Data Only","Buy Data and Spores"], 'y': valueresults,\
                    'type': 'bar', 'name': 'Certain Equivalent'},
               {'x': ["Harvest Now","Buy Nothing and Wait","Buy Spores Only",\
                      "Buy Data Only","Buy Data and Spores"], 'y': Evalueresults,\
                   'type': 'bar', 'name': 'Average Payoff'},
            ],
            'layout': {
                'title': 'Decision Visualization'
            }}

@app.callback(
    [Output('table','data'),Output('table','columns')],
    [Input('prain-slider', 'value'),
     Input('risktol-slider', 'value')])
def update_table(prain1,risktol):
    global riskave
    riskave=1/risktol
    global prain
    prain=prain1
    generate_valuetables()
    generate_utables() 
    generate_CEs()
    generate_means()
    df = generate_dataframe(Evalueresults,valueresults)
    return df.to_dict('rows'), col

if __name__ == '__main__':
    app.run_server()
