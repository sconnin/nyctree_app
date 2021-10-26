# -*- coding: utf-8 -*-

"""
Created on Sun Oct 24 10:30:44 2021

@author: sean connin
"""

import pandas as pd
import numpy as np
import json
import plotly.express as px
import dash 
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

#Set background to black, white font

url=pd.read_json('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?').fillna(0)

tree_species=list(url['spc_common'].unique())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


# initiate app

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout=html.Div(style={'backgroundColor': colors['background']}, children=[
    
    
    html.Div([
        html.H1("Health Status of Tree Species in NYC",
                style={'color':' #FFFFFF'}),
        
        html.H5('Background:', 
                style={'font-size':24,
                       'color':'#A9CCE3',
                       'padding':'0px', 'margin':'5px 25px'})

        ]),  
        
# add description paragraph
    html.Div(children=[
        html.I('This application provides arborists in NYC a use-friendly reference for\
               monitoring the health of trees across NYC boroughs. The data consist of \
              Street Tree Census observations collected annually since 2015 by volunteers\
              and staff of the NYC Parks & Recreation and partner organizations.Three figures \
              are included in the tabs below. The first allows users to assess the health status\
              of a selected tree species across each borough. The second allows users \
              to assess the health status of tree species within a selected obrough.\
              And the third compares the overall status of tree health in\
              relation to the number of tree stewards per borough. Note that some \
              species names have been exluded from the X-axis of Figure 2\
              to declutter the plot. Use hover to identify select columns.')],
              
              style={'font-size':16,
                      'color':'#FFFFFF',
                      'height':140, 'width':900,
                      'padding':'0px', 
                      'margin-left':'25px',
                      'margin-bottom':'25x'}),
            
# add reference links

     html.Div(children=[
            
            html.I('For information related to this dataset please refer to the following websites:')],
               
               style={'font-size':18,
                      'color':'#A9CCE3',
                      'height':20, 'width':900,
                      'padding':'0px', 
                      'margin-top':'60px',
                      'margin-left':'25px'}
               ),
        
        html.Ol(children=[
            
            html.A("NYC OpenData", href='https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh', target="_blank"),
            html.Br(),
            html.A("Socrata API", href='https://dev.socrata.com/data/', target="_blank")],
        
               style={'font-size':14,
                      '#color':'#A9CCE3',
                      'height':60, 'width':900,
                      'margin-top':'25px',
                      'margin-left':'25px'}),


    dcc.Tabs([
        
        #Create first tab set
        
        dcc.Tab(label='Tree Species', children = [
            #dropdown for species selection
            html.Div([
                html.H5('Figure 1. Select a Tree Species from the Drop-down List',
                style={'font-size':24,
                       'color':'#A9CCE3',
                       'padding':'0px', 
                       'margin-top':'40px',
                       'margin-left':'10px'}
                ),
            dcc.Dropdown(id='species_input',
                value='pin oak',
                options=[{'label':tree, 'value':tree}
                      for tree in tree_species],  # see fxn line 23
                style={
                'width':'180px',
                'margin-left':'10px',
                'margin-top':'25px',
                'verticalAlign':'middle'
            }
        ),
            
        #Graph container for species by borough
            
        html.Div(
        
            dcc.Graph(id='fig1_graph',
                style={'width':'200vh', 
                       'height': '120vh'}))
        ]),
          
     ]), #end of tab 1
        
        
        #Create second tab set
  
        dcc.Tab(label='Borough', children = [
            
        # Dropdown for borough selection
         
        html.Div([
             html.H5('Figure 2. Select a Borough from the Drop-down List',
                     style={'font-size':24,
                            'color':'#A9CCE3',
                            'padding':'0px',
                            'margin-top':'40px',
                            'margin-left':'10px'
                            }),
         dcc.Dropdown(id='borough_input',
            value='Brooklyn',
            options=[
                {'label':"Brooklyn", 'value':'Brooklyn'},
                {'label':'Manhattan', 'value':'Manhattan'},
                {'label':'Bronx', 'value':'Bronx'},
                {'label':'Queens', 'value':'Queens'},
                {'label':'Staten Island', 'value':'Staten Island'}],
            style={
                'width':'180px',
                'margin-left':'10px',
                'margin-top':'25',
                'verticalAlign':'middle'
                }
            ),
        
    #Graph container for species by borough 

        html.Div(
            
            dcc.Graph(id='fig2_graph',
                style={'width':'200vh', 
                       'height': '125vh'}))        
        
        ])
        ]), # end of tab 2
        
        # Create third tab set 
        
        dcc.Tab(label='Borough/Stewardship', children = [
            
        html.Div([
            html.H5('Figure 3. Select a Borough from the Drop-down List:', 
                    style={'font-size':24,
                       'color':'#A9CCE3',
                       'margin-left':'10px',
                       'margin-top':'40px'}),
  
 #placeholder
 # Dropdown for borough selection
            #html.Div([
                #html.H5('Select a Borough from the Drop-down List',
                    #style={'font-size':16,
                           #'color':'#A9CCE3',
                           #'padding':'0px', 'margin':'5px 25px'}),
            dcc.Dropdown(id='borough_input2',
                value='Brooklyn',
                options=[
                    {'label':"Brooklyn", 'value':'Brooklyn'},
                    {'label':'Manhattan', 'value':'Manhattan'},
                    {'label':'Bronx', 'value':'Bronx'},
                    {'label':'Queens', 'value':'Queens'},
                    {'label':'Staten Island', 'value':'Staten Island'}],
                style={
                    'width':'180px',
                    'margin-left':'10px',
                    'margin-bottom':'40px',
                    'verticalAlign':'middle'
                    }
                ),
            
            
    #Graph container for species by borough 

            html.Div(
            dcc.Graph(id='fig3_graph'))
            
        ]),
        
    # Narrative to follow graph 
        
            html.Div(children=[
                
                html.I('Common to the physical sciences, ternary plots can be used to display the\
                ratios of the three variables as positions in an equilateral triangle.\
                The figure above displays three levels of tree species health (Good, Fair, Poor)\
                in relation to different levels of stewardship (indicated by color) for a\
                selected borough. It is clear from the results that tree stewards have had\
                little net affect on tree health. And that the majority of trees are in \
                good health')],
               
               style={'font-size':16,
                      'color':'#FFFFFF',
                      'height':130, 'width':900,
                      'margin-left':'10px',
                      'margin-top':'40px',
                      'margin-bottom':'10px'}),

         html.Div(children=[
            
            html.I('For information on how to interpret ternary plots, readers can find\
               helpful information at the following websites:')],
               
               style={'font-size':16,
                      'color':'#FFFFFF',
                      'height':30, 'width':900,
                      'margin-top':'60',
                      'margin-left':'10px'}),
        
            html.Ol([
            
                html.A("Wikipedia", href='https://en.wikipedia.org/wiki/Ternary_plot', target="_blank"),
                html.Br(),
                html.A("Grapher", href='http://grapherhelp.goldensoftware.com/Graphs/Reading_Ternary_Diagrams.htm', target="_blank"),
                html.Br(),
                html.A("Plotly", href='https://plotly.com/python/ternary-plots/', target="_blank")],
        
                style={'font-size':14,
                      '#color':'#FFFFFF',
                      'height':60, 'width':900,
                      'margin-top':'20px', 
                      'margin-left':'25px',
                      'margin-bottom':'20px'}),
            
        html.Div(children=[
            
            html.A('Contact The Author: Sean Connin', href='https://www.linkedin.com/feed/', target='_blank')],
            
                style={'font-size':16,
                      '#color':'#FFFFFF',
                      'height':60, 'width':900,
                      'margin-top':'20px', 
                      'margin-left':'25px',
                      'margin-bottom':'40px'}),
            
            
            ])#outer shell of tab 3 
        
    ]) #outer shell of tabs


]) #outer shell of layout
      

#call-back for borough plot

@app.callback(
              Output('fig1_graph', 'figure'),
              Input('species_input', 'value'))

#DEFINE FUNCTION for species-borough plot

def update_species_plot(species_input): 
    
    if species_input:
        url_spc = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?'+\
           '$select=boroname, health, count(spc_common)'+\
               '&$where=spc_common=\''+species_input+ '\''+\
                   '&$group=boroname, health').replace(' ', '%20')

    df2 = pd.read_json(url_spc).fillna(0)
    df2=pd.DataFrame(df2)


# configure dataframe to calculate species percentages

    df2_a = df2.groupby(['boroname', 'health']).agg({'count_spc_common': 'sum'})
    df2_b= df2.groupby(['boroname']).agg({'count_spc_common': 'sum'})
    df2=df2_a.div(df2_b, level='boroname') * 100
    df2=df2.reset_index().rename(columns={'count_spc_common':'unrounded'})
    df2=df2.dropna()
    df2['relative percent']=df2['unrounded'].round(1)
    df2.drop('unrounded', axis=1, inplace=True)

#build graph

    fig1_graph=px.bar(df2, x='boroname', y='relative percent', color='health', template='plotly_dark', color_discrete_sequence=px.colors.qualitative.Dark2, barmode   ='relative',
                         title='Health Status of ' + str(species_input) + ' by NYC Borough.' ,
                         labels={'relative percent':'Cumulative Percent',
                                 'boroname':'Borough'},
                         height=600)
    return fig1_graph        

# call-back for species plot

@app.callback(
              Output('fig2_graph', 'figure'),
              Input('borough_input', 'value'))

                                       
# DEFINE FUNCTION for borough-species plot-create df from api call

def update_species_plot(borough_input): 

    url_boro = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?'+\
            '$select=spc_common, health, count(spc_common)'+\
                '&$where=boroname=\''+borough_input+ '\''+\
                   '&$group=health, spc_common').replace(' ', '%20')

    df = pd.read_json(url_boro).fillna(0)
    df=pd.DataFrame(df)
    

# configure dataframe to calculate species percentages

    df_a = df.groupby(['spc_common', 'health']).agg({'count_spc_common': 'sum'})
    df_b= df.groupby(['spc_common']).agg({'count_spc_common': 'sum'})
    df=df_a.div(df_b, level='spc_common') * 100
    df=df.reset_index().rename(columns={'count_spc_common':'unrounded'})
    df=df.dropna()
    df['relative percent']=df['unrounded'].round(1)
    df.drop('unrounded', axis=1, inplace=True)


#build graph

    fig2_graph=px.bar(df, x='spc_common', y='relative percent', template='plotly_dark', color='health', barmode ='relative', color_discrete_sequence=px.colors.qualitative.Dark2,
                         title='Health of Trees in the Borough: ' + str(borough_input) + '.' ,
                         labels={'relative percent':'Cumulative Percent',
                                 'spc_common':'Species'},
                         height=600)
    return fig2_graph


# call-back for ternary plot

@app.callback(
              Output('fig3_graph', 'figure'),
              Input('borough_input2', 'value'))

                                       
# DEFINE FUNCTION for borough-species plot-create df from api call

def update_species_plot(borough_input2): 

    url_boro2 = ('https://data.cityofnewyork.us/resource/nwxe-4ae8.json?'+\
            '$select=spc_common, health, steward, count(health)'+\
                '&$where=boroname=\''+borough_input2+ '\''+\
                   '&$group=health, spc_common, steward').replace(' ', '%20')

    df3 = pd.read_json(url_boro2).fillna(0)
    df3=pd.DataFrame(df3)



# configure dataframe to calculate steward percentages

    df3_a = df3.groupby(['spc_common', 'health','steward']).agg({'count_health': 'sum'})
    df3_b= df3.groupby(['spc_common']).agg({'count_health': 'sum'})
    df3=df3_a.div(df3_b, level='spc_common') #* 100
    df3=df3.reset_index().rename(columns={'count_health':'unrounded'})
    df3.dropna()
    df3['relative_percent']=df3['unrounded'].round(2)#.astype(int)
    df3.drop('unrounded', axis=1, inplace=True)
    df3=df3.pivot_table(index=['spc_common', 'steward'],
        columns='health',
        values='relative_percent').reset_index()
    df3.steward.replace(['1or2', '3or4', '4orMore'], ['1-3', '1-3', '4+'], inplace=True)
    df3=df3.fillna(0)
    df3=df3.sort_values(['steward'])

#build graph

    fig3_graph=px.scatter_ternary(df3, a='Good', b='Fair', c='Poor', color='steward',
            title="Comparing Levels of Stewardship and Tree Health by Borough",
            height=600)
    return fig3_graph

       


                               
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)


