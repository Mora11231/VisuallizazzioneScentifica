import pandas as pd
import plotly.express as px

def graficoTortaF2PvsP2P():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
 
    serie = df.F2P.value_counts()

    fig = px.pie(values=serie,names=['F2P','P2P'],color_discrete_sequence=['#1b9e77','#d95f02'])

    fig.update_layout(
        font_family="Calibri",
        title = "F2P / P2P",
        template="plotly_white",
        
        legend_title = "Leggenda:",
        
        font=dict( 
            size=15, 
            color="#000000" 
        )
    )


    fig.show()


def checkSoftware(x):
    if x.find('Software') != -1:
        return True
    return False

def replaceNaN(x):
    if x!=x:
        return ""
    return x

def graficoTortaAppEGiochi():
    df = pd.read_csv('CodicePerGrafici/fileAggiornatoF2P.csv')
    df['Genres'] = df['Genres'].apply(lambda x: replaceNaN(x))
    df['App'] = df['Genres'].apply(lambda x: checkSoftware(x))
    n_app = sum(df['App'])
    n_giochi = len(df)-n_app

    fig = px.pie(values=(n_app,n_giochi),names=['APP','Giochi'],color_discrete_sequence=['#7b3294','#008837'])

    fig.update_layout(
        font_family="Calibri",
        title = "Applicazioni / Giochi",
        template="plotly_white",
        
        legend_title = "Leggenda:",
        
        font=dict( 
            size=15, 
            color="#000000" 
        )
    )

    fig.show()


graficoTortaAppEGiochi()