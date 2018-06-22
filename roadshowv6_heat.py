#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:34:38 2018

@author: niels
"""


import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from functions import model_value, x_values, Table
'''
Construct data
'''

df = pd.read_excel("data.xlsx")

df["procentage"] = float() 


def test (x,y):
    return x*y


'''
The dash Board
OBS!!!!
Styled for 1024x768

'''



app = dash.Dash()



y=np.array([10, 12, 15, 19, 28, 25, 31, 33, 43])
color=np.array(['rgb(255,255,255)']*y.shape[0])
color[y<20]='rgb(204,204, 205)'
color[y>=20]='rgb(130, 0, 0)'


colors = {
        'background': 'white',
        'text': '#333333',
        'header': '#cf7719'
        }

app.layout = html.Div(
        style={'backgroundColor': colors["background"], 'font-family': "Arial" }, children =[
                
                html.H1(style={'text-align':'left', 'font-family': "Arial", 'backgroundColor':'#F5F5F5', 'padding':'25px 30px'},
                        children = "Machine Learning og Etik",
                        ),
                
                html.Div(style={'backgroundColor': colors["background"],'float':'left', 'width':"35%", 'margin-left':'30px'},children= [
                
                    html.H2(style={'fontSize':'20', 'padding-bottom':'1px'},
                            children="Hvor vil du bruge data fra?"
                    ),
                    
                    html.Div (style={'backgroundColor': colors["background"]},
                                     children = dcc.Checklist(
                                             style={'margin-right':'8px', 'width':'50%', 'margin-left':'10px'},
                                             id="data_valg",
                                             options=[
                                                {"label":"Virk", "value": 0.5},
                                                {"label":"CVR", "value":1},
                                                {"label":"CPR", "value": 1.5},
                                                {"label":"Beskæftigelsedata","value":2},
                                                {"label":"Bankoplysninger","value":2.5},
                                                {"label":"Teledata","value":3},
                                                {"label":"FaceBook","value":3.5}],
                                            values = [0.5, 1, 1.5, 2, 2.5 , 3, 3.5,],
                                            labelStyle={'display':'block', 'margin-bottom':'5px'}
                                                )
                                     ),
                                    
                    html.H3(style={'fontSize':'20', 'padding-bottom':'1px', 'margin-top':'40px'},
                            children="Hvor klog skal comuteren være?"),
                    
                    html.Div (style={'backgroundColor': colors["background"]}, 
                                     children = dcc.RadioItems(style={'width':'50%', 'margin-left':'10px'},
                                             id="model_valg",
                                             options= [
                                                     {"label": "Fuld Forklaring", "value": 0.5},
                                                     {"label": "Fuld Forklaring ich", "value": 1},
                                                     {"label": "Black Box (fatter Hat)", "value": 1.5}],
                                                     value=1,
                                                     labelStyle={'display':'block', 'margin-bottom':'5px'}
                                            
                                                )
                                     ),
                    html.H3(style={'fontSize':'20', 'margin-top':'40px'}, children='something something'),
                    html.Div (id='penge'),
                    html.H3(style={'fontSize':'20', 'margin-top':'40px'}, children='something something'),
                    html.Div (id='telefon')

                    ]),
                                                                 
                html.Div (style={'backgroundColor': colors["background"], 'float':'right', 'overflow':'auto',
                                 'width':"60%", 'font-family': "Arial"},
                                 children = [
                                         html.Div(style={'padding-left':'250px','text-align':'center',
                                                         'border-bottom':'dashed'},
                                                  children = 'Den bekræftede værdi (Sandhed)'),
                                         html.Div(children=[
                                                 html.Div(style={'float':'right','width':'20%'},
                                                          children ='positiv'),
                                                          
                                                 html.Div(style={'padding-left':'250px','width':'10%'},
                                                          children ='negativ')]),
                                        
                                        html.Div(children=[
                                                html.Div(style={'float':'right', 'width':'70%'},
                                                         id="confusion"),
                                                         
                                                html.Div(style={'float':'left', 'width':'20%', 'height':'20%', 'padding-top':'20px',
                                                                'border-right':'dashed', 'padding-right':'1px', 
                                                                'margin-right':'1px', 'margin-top':'13px'},
                                                         children = 'Værdi forudset af ML model (Modellen tror)'),
                                                         
                                                html.Div(style={'float':'left', 'width':'1%', 
                                                                'margin-left':'125px', 'margin-top':'15px', 
                                                                'padding-left':'1px', 'position':'absolute'},
                                                         children ='positiv'),
                                                         
                                                html.Div(style={'float':'left', 'width':'1%', 
                                                                'padding-top':'68px', 'margin-left':'1px'
                                                                },
                                                         children ='negativ')]),
                                         
                                         
                                         html.Div (style={'backgroundColor': colors["background"], 'margin-top':'150px'},
                                             children =[
                                             html.Div(style={'text-align':'center'}, children = 'Data Fordeling'),
                                             html.Div(dcc.Graph(id='fig')),
                                             html.Div(
                                                     dcc.Slider(id = "slider",
                                                                min=0,
                                                                max=100,
                                                                step=0.1,
                                                                value = 50,
                                                                )),
                                             html.Div(style={'text-align':'center'},children = 'Threashold')]
                                             )
                                         ]
                                 )
                        
                ]
            )


'''
Calback to Grahp
'''

@app.callback(
    dash.dependencies.Output('fig', 'figure'),
    [dash.dependencies.Input('data_valg', 'values'),
     dash.dependencies.Input('slider', 'value'),
     dash.dependencies.Input('model_valg','value')])



def update_graph(data_valg_values, slider_value, model_valg_value):
    
    print(sum(data_valg_values)+model_valg_value)
    
    
    
    df["total"]= df[data_valg_values].sum(axis=1)
    

    total = x_values(data_valg_values, model_valg_value)
    
    totalliste = []
    for i in total:
        totalliste.append(i)
    
    
    df["x"]=totalliste       
   
    
    pro= (slider_value/100)    
    
    df["x"]=df["x"].astype(float)
    
    X =df["x"].quantile(q=pro) 
    


    ylow= df["total"].min()
    yhigh= df["total"].max()
    
    
    return {
            'data': [go.Scatter(
            x=df[df["navn"]==i]["x"],
            y=df[df["navn"]==i]["total"],
            text=df["navn"],
            mode='lines',
            fill='tozeroy',
            line = dict(shape='spline'),
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}}, 
            
            
                    
            )
    for i in df.navn.unique()
    ],
            'layout': go.Layout(
                xaxis=dict(
                        autorange= True,
                        showgrid = False,
                        zeroline = False,
                        showline = False,
                        autotick=True,
                        ticks = '',
                        showticklabels = False,
                       ),
                yaxis=dict(
                        autorange= False,
                        showgrid = False,
                        zeroline = False,
                        showline = False,
                        autotick=True,
                        ticks = '',
                        showticklabels = False,
                        range = [ylow,yhigh]
                       ),
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest',
                showlegend = False,
                paper_bgcolor = colors["background"],
                plot_bgcolor = colors["background"],
                shapes = [{"type" : "line",
                          "xref": "x",
                          "yref": "y",
                          "x0" : X,
                          "y0" : ylow,
                          "x1" : X,
                          "y1" : yhigh,
                          "line": {
                                  "color": "rgb(0,0,0)",
                                  "width":3} 
                              }],
            height = 300
            
                        )
            
        
            #dir(go.Layout())
            }


                                        
'''
Callback to BAR
'''

'''                
@app.callback(
        dash.dependencies.Output('bar', "figure"),
        [dash.dependencies.Input('model_valg', 'value'),
         dash.dependencies.Input('data_valg', 'values'),
         dash.dependencies.Input('slider', 'value')]) 

def show_bar (model_valg_value, data_valg_values, slider_value):
    
    df["total"]= df[data_valg_values].sum(axis=1)
    
    total = x_values(data_valg_values, model_valg_value)
    
    totalliste = []
    for i in total:
        totalliste.append(i)
    
    
    df["x"]=totalliste 
    
    tp=[]
    fp=[]
    tn=[]
    fn=[]
    
    
    pro= (slider_value/100)    
    X =df["x"].quantile(q=pro) 

    for index,row in df.iterrows():
        if row["tag"] == 0:
            if X>row["x"]:
                tn.append(1)
            elif X<row["x"]:
                fn.append(1)
        if row["tag"] == 1:
            if X<row["x"]:
                tp.append(1)
            elif X>row["x"]:
                fp.append(1)
    
    
    #fp.extend(tp[0:fpcount])
    #fn.extend(fp[0:fncount])
    #tp = tp[fpcount:]
    #fp = fp[fncount:]
    
    if X>df[df["tag"]==0]["x"].max():
        tn = tn+fn
        fn = []     
    elif X<df[df["tag"]==1]["x"].min():
        tp = tp+fp
        fp = [] 
    
    
    
    return {
            'data': [go.Bar(
                    x = ['Lovlydige', 'Falske Svindlere', 'Falske Lovlydige',  'Svindlere'],
                    y = [len(tn), len(fn), len(fp), len(tp)],
                    marker = dict(color=['green','red', 'red', 'green']),
                    text=y,
                    textposition='inside',
                    textfont=dict(color='white', size=20)

                    
                    
                    )],
            'layout': go.Layout(
                    paper_bgcolor = colors["background"],
                    plot_bgcolor = colors["background"],
                    height = 700,
                    showlegend = False,
                    xaxis=dict(
                        autorange= True,
                        showgrid = False,
                        zeroline = False,
                        showline = False,
                        autotick=True,
                        ticks = '',
                        showticklabels = False,
                       ),
                yaxis=dict(
                        autorange= True,
                        showgrid = False,
                        zeroline = False,
                        showline = False,
                        autotick=True,
                        ticks = '',
                        showticklabels = True,
                       ),
                images = [dict(
                        source = 'pics/penge.png',
                        sizex = 1,
                        sizey = 1
                        )
                        ]
                
                        
                    
                    
                    
                    )
            
                     
            
            }

'''
'''
Callback to confusion
'''



@app.callback(
        dash.dependencies.Output('confusion', "children"),
        [dash.dependencies.Input('model_valg', 'value'),
         dash.dependencies.Input('data_valg', 'values'),
         dash.dependencies.Input('slider', 'value')])

def confusion (model_valg_value, data_valg_values, slider_value):
    
    df["total"]= df[data_valg_values].sum(axis=1)
    total = x_values(data_valg_values, model_valg_value)
    
    totalliste = []
    for i in total:
        totalliste.append(i)
    
    
    df["x"]=totalliste 
    
    tp=[]
    fp=[]
    tn=[]
    fn=[]
    
    
    pro= (slider_value/100)    
    X =df["x"].quantile(q=pro) 

    for index,row in df.iterrows():
        if row["tag"] == 0:
            if X>row["x"]:
                tn.append(1)
            elif X<row["x"]:
                fn.append(1)
        if row["tag"] == 1:
            if X<row["x"]:
                tp.append(1)
            elif X>row["x"]:
                fp.append(1)
    
    
    #fp.extend(tp[0:fpcount])
    #fn.extend(fp[0:fncount])
    #tp = tp[fpcount:]
    #fp = fp[fncount:]
    
    if X>df[df["tag"]==0]["x"].max():
        tn = tn+fn
        fn = []     
    elif X<df[df["tag"]==1]["x"].min():
        tp = tp+fp
        fp = []  
    
    
    
    con = pd.DataFrame({
        'Positive': ['TP = True Positive (Stoppet Svindelere) {}'.format(len(tp)*20),'FN = False Negative (Succesfuld svindlere) {}'.format(len(fp)*20)],
        'Negative':['FP = False Positive (Unødvendigt bebyrdede borgere) {}'.format(len(fn)*20),'TN = True Negative (Borgere) {}'.format(len(tn)*20) ]
        
        })
                
       
    
    return Table(con)
     
     

@app.callback(
        dash.dependencies.Output('penge', "children"),
        [dash.dependencies.Input('model_valg', 'value'),
         dash.dependencies.Input('data_valg', 'values'),
         dash.dependencies.Input('slider', 'value')]) 

def Skatte (model_valg_value, data_valg_values, slider_value):
    
    df["total"]= df[data_valg_values].sum(axis=1)
    
    total = x_values(data_valg_values, model_valg_value)
    
    totalliste = []
    for i in total:
        totalliste.append(i)
    
    
    df["x"]=totalliste 
    
    tp=[]
    fp=[]
    tn=[]
    fn=[]
    
    
    pro= (slider_value/100)    
    X =df["x"].quantile(q=pro) 

    for index,row in df.iterrows():
        if row["tag"] == 0:
            if X>row["x"]:
                tn.append(1)
            elif X<row["x"]:
                fn.append(1)
        if row["tag"] == 1:
            if X<row["x"]:
                tp.append(1)
            elif X>row["x"]:
                fp.append(1)
    
    
    #fp.extend(tp[0:fpcount])
    #fn.extend(fp[0:fncount])
    #tp = tp[fpcount:]
    #fp = fp[fncount:]
    
    if X>df[df["tag"]==0]["x"].max():
        tn = tn+fn
        fn = []     
    elif X<df[df["tag"]==1]["x"].min():
        tp = tp+fp
        fp = []

    return 'Skatte Gab {} mio. kr.'.format((len(fp)*20)*1.4)


@app.callback(
        dash.dependencies.Output('telefon', "children"),
        [dash.dependencies.Input('model_valg', 'value'),
         dash.dependencies.Input('data_valg', 'values'),
         dash.dependencies.Input('slider', 'value')]) 

def Telefontid (model_valg_value, data_valg_values, slider_value):
    
    df["total"]= df[data_valg_values].sum(axis=1)
    
    total = x_values(data_valg_values, model_valg_value)
    
    totalliste = []
    for i in total:
        totalliste.append(i)
    
    
    df["x"]=totalliste 
    
    tp=[]
    fp=[]
    tn=[]
    fn=[]
    
    
    pro= (slider_value/100)    
    X =df["x"].quantile(q=pro) 

    for index,row in df.iterrows():
        if row["tag"] == 0:
            if X>row["x"]:
                tn.append(1)
            elif X<row["x"]:
                fn.append(1)
        if row["tag"] == 1:
            if X<row["x"]:
                tp.append(1)
            elif X>row["x"]:
                fp.append(1)
    
    
    #fp.extend(tp[0:fpcount])
    #fn.extend(fp[0:fncount])
    #tp = tp[fpcount:]
    #fp = fp[fncount:]
    
    if X>df[df["tag"]==0]["x"].max():
        tn = tn+fn
        fn = []     
    elif X<df[df["tag"]==1]["x"].min():
        tp = tp+fp
        fp = []
    
    tid = (len(fn)*40)*2.5
    
    return 'Sagsbehandlings tid {} i timer og procent af et årsværk {}%'.format(tid, (tid/1500))



if __name__ == '__main__':
    app.run_server()
            

