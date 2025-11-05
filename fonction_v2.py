from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import warnings
import re
from io import BytesIO
import zipfile

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from matplotlib.patches import Arc
from matplotlib.patches import ConnectionPatch

import io
from PIL import Image

def draw_pitch_horizontal():
    # focus on only half of the pitch
    #Pitch Outline & Centre Line
    fig=plt.figure() #set up the figures
    fig.set_size_inches(10, 7)
    ax=fig.add_subplot(1,1,1)
    
    Pitch = Rectangle([0,0], width = 120, height = 70, fill = False)
    essai1 = Rectangle([0,0], width = 10, height = 70, fill = False, color='gray',hatch='/')
    essai2 = Rectangle([110,0], width = 1070, height = 70, fill = False, color='gray',hatch='/')
    en_but1 = ConnectionPatch([10,0], [10,80], "data", "data")
    en_but2 = ConnectionPatch([110,0], [110,70], "data", "data")
    cinq_metres1 = ConnectionPatch([15,0], [15,70], "data", "data",ls='--',color='gray')
    cinq_metres2 = ConnectionPatch([105,0], [105,70], "data", "data",ls='--',color='gray')
    midline = ConnectionPatch([60,0], [60,70], "data", "data")
    vingtdeux_metres1 = ConnectionPatch([32,0], [32,70], "data", "data")
    vingtdeux_metres2 = ConnectionPatch([88,0], [88,70], "data", "data")
    dix_metres1 = ConnectionPatch([50,0], [50,70], "data", "data",ls='--',color='gray')
    dix_metres2 = ConnectionPatch([70,0], [70,70], "data", "data",ls='--',color='gray')
    centreCircle = plt.Circle((60,35),0.5,color="black", fill = True)
    poteau1a = plt.Circle((10,32.2),0.5,color="black", fill = True)
    poteau1b = plt.Circle((10,37.8),0.5,color="black", fill = True)
    poteau2a = plt.Circle((110,32.2),0.5,color="black", fill = True)
    poteau2b = plt.Circle((110,37.8),0.5,color="black", fill = True)

    element = [essai1, essai2, Pitch, en_but1, en_but2, cinq_metres1, cinq_metres2, midline, vingtdeux_metres1, 
    vingtdeux_metres2,centreCircle,poteau1a,poteau1b,poteau2a,poteau2b,dix_metres1,dix_metres2]
    for i in element:
        ax.add_patch(i)

    rectangle1 = Rectangle([88,60],width= 22, height = 10, fill = True, color='darkred',alpha=0.5)
    rectangle2 = Rectangle([100,10],width= 10, height = 50, fill = True, color='darkred',alpha=0.5)
    rectangle3 = Rectangle([88,0],width= 22, height = 10, fill = True, color='darkred',alpha=0.5)
    
    for rect in [rectangle1, rectangle2, rectangle3]:
        ax.add_patch(rect)

    rectangle1 = Rectangle([10,0],width= 78, height = 10, fill = True, color='darkblue',alpha=0.15)
    rectangle2 = Rectangle([10,60],width= 78, height = 10, fill = True, color='darkblue',alpha=0.15)

    for rect in [rectangle1, rectangle2]:
        ax.add_patch(rect)

    return fig,ax

def draw_pitch_horizontal_v2():

    fig=plt.figure() 
    fig.set_size_inches(10, 7)
    ax=fig.add_subplot(1,1,1)
    
    Pitch = Rectangle([0,0], width = 120, height = 70, fill = False)
    essai1 = Rectangle([0,0], width = 10, height = 70, fill = False, color='gray',hatch='/')
    essai2 = Rectangle([110,0], width = 1070, height = 70, fill = False, color='gray',hatch='/')
    en_but1 = ConnectionPatch([10,0], [10,80], "data", "data")
    en_but2 = ConnectionPatch([110,0], [110,70], "data", "data")
    cinq_metres1 = ConnectionPatch([15,0], [15,70], "data", "data",ls='--',color='gray')
    cinq_metres2 = ConnectionPatch([105,0], [105,70], "data", "data",ls='--',color='gray')
    midline = ConnectionPatch([60,0], [60,70], "data", "data")
    vingtdeux_metres1 = ConnectionPatch([32,0], [32,70], "data", "data")
    vingtdeux_metres2 = ConnectionPatch([88,0], [88,70], "data", "data")
    dix_metres1 = ConnectionPatch([50,0], [50,70], "data", "data",ls='--',color='gray')
    dix_metres2 = ConnectionPatch([70,0], [70,70], "data", "data",ls='--',color='gray')
    centreCircle = plt.Circle((60,35),0.5,color="black", fill = True)
    poteau1a = plt.Circle((10,32.2),0.5,color="black", fill = True)
    poteau1b = plt.Circle((10,37.8),0.5,color="black", fill = True)
    poteau2a = plt.Circle((110,32.2),0.5,color="black", fill = True)
    poteau2b = plt.Circle((110,37.8),0.5,color="black", fill = True)

    element = [essai1, essai2, Pitch, en_but1, en_but2, cinq_metres1, cinq_metres2, midline, vingtdeux_metres1, 
    vingtdeux_metres2,centreCircle,poteau1a,poteau1b,poteau2a,poteau2b,dix_metres1,dix_metres2]
    for i in element:
        ax.add_patch(i)

    return fig,ax

dico_color = {

    "PIE": "lightsalmon", "PIE_9": "lightsalmon", "PIE_9, PIE": "lightsalmon","PIE_10": "lightsalmon","PIE_10, PIE": "lightsalmon",
    "PIE, PIE_9": "lightsalmon","PIE, PIE_10": "lightsalmon",

    "AIGLE": "black", "AIGLE_9": "black", "AIGLE_9, AIGLE": "black","AIGLE_10": "black","AIGLE_10, AIGLE": "black",
    "AIGLE, AIGLE_9": "black","AIGLE, AIGLE_10": "black","AIGLE, AIGLE_15": "black","AIGLE_15, AIGLE": "black", "AIGLE_15" : "black",

    "TOUCHE": "cadetblue", "TOUCHE_9": "cadetblue", "TOUCHE_9, TOUCHE": "cadetblue","TOUCHE_10": "cadetblue","TOUCHE_10, TOUCHE": "cadetblue",
    "TOUCHE, TOUCHE_9": "cadetblue","TOUCHE, TOUCHE_10": "cadetblue","TOUCHE, TOUCHE_15": "cadetblue","TOUCHE_15, TOUCHE": "cadetblue", "TOUCHE_15" : "cadetblue",

    "PHENIX": "mediumvioletred", "COLOMBE": "mediumvioletred", "COLOMBE, PHENIX": "mediumvioletred","PHENIX_10": "mediumvioletred",
    "PHENIX_10, PHENIX": "mediumvioletred","PHENIX, COLOMBE": "mediumvioletred","PHENIX, PHENIX_10": "mediumvioletred",

    "POULE":"tan",

    "ROLLER":"mediumblue",

    'GAP':'red'

}

def kicking_plot(dataset,dico_player):

    dataset = dataset[dataset.Row.str.contains('Jeu au pied',na=False)].reset_index(drop=True)
    dataset = dataset[dataset.Row.str.contains("Racing",na=False)].reset_index(drop=True)

    dataset['X'], dataset['Y'] = dataset['X'].astype('float'), dataset['Y'].astype('float')
    dataset['Distance X'] = dataset['X jap fin'] - dataset['X']
    dataset['Distance Y'] = (dataset['Y jap fin'] - dataset['Y'])*(-1)

    dataset[['New X','New Y']] = ''

    for i in range(len(dataset)):

        dataset['New X'][i] = dataset.X[i] + 10 
        dataset['New Y'][i] = 70 - dataset.Y[i] 

    (fig,ax) = draw_pitch_horizontal() 
    plt.ylim(-2, 72)
    plt.xlim(-2, 120.4)
    plt.axis('off')

    print(dataset)

    for i in range(len(dataset)):

        if dataset['Type de jeu au pied'][i] in ['PENALTOUCHE',"COUP D'ENVOI",'PENALTOUCHE, PENALTOUCHE','RENVOI EN BUT','PENALTOUCHE, GAP']:
            pass

        else:
            if dataset['Type de jeu au pied'][i] in list(dico_color.keys()):
                plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
                color = dico_color[dataset['Type de jeu au pied'][i]])
            else:
                plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
                color = 'grey')
                
            joueurs = dataset['Joueurs'][i]
            #initiales = joueurs[joueurs.index(' ')+1] + '.' + joueurs[0]  
            
            #if initiales == 'G.L':
            #    initiales = "N.LG"

            plt.annotate(str(dico_player[joueurs]),(dataset['New X'][i]-2,dataset['New Y'][i]))
        
    plt.title('Kicking Game - ' + dataset['Timeline'][i] + '\n\n' + "Racing 92" + '\n',fontweight='semibold',fontsize=11)
    
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)

    return img

def kicking_plot_players(dataset,list_player,liste_jap):

    dataset = dataset[dataset['Type de jeu au pied'].isin(liste_jap)].reset_index(drop=True)
    dataset['X'], dataset['Y'] = dataset['X'].astype('float'), dataset['Y'].astype('float')

    dataset['Distance X'] = dataset['X jap fin'] - dataset['X']
    dataset['Distance Y'] = (dataset['Y jap fin'] - dataset['Y'])*(-1)

    dataset[['New X','New Y']] = ''

    for i in range(len(dataset)):

        dataset['New X'][i] = dataset.X[i] + 10 
        dataset['New Y'][i] = 70 - dataset.Y[i] 

    (fig,ax) = draw_pitch_horizontal() 
    plt.ylim(-2, 72)
    plt.xlim(-2, 120.4)
    plt.axis('off')

    print(dataset)

    for i in range(len(dataset)):

        if dataset['Type de jeu au pied'][i] in list(dico_color.keys()):
            plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
            color = dico_color[dataset['Type de jeu au pied'][i]])
        else:
            plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
            color = 'grey')
                        
    plt.title('Kicking Game - ' + str(list_player),fontweight='semibold',fontsize=11)
    
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)

    return img

def kicking_plot_adv(dataset,opta):

    if opta == False:
        
        dataset = dataset[dataset.Row.str.contains('Jeu au pied',na=False)].reset_index(drop=True)
        dataset = dataset[dataset.Row.str.contains("Racing",na=False) == False].reset_index(drop=True)
        dataset['X'], dataset['Y'] = dataset['X'].astype('float'), dataset['Y'].astype('float')

        dataset['Distance X'] = dataset['X jap fin'] - dataset['X']
        dataset['Distance Y'] = (dataset['Y jap fin'] - dataset['Y'])*(-1)

    else:

        dataset['X'], dataset['Y'] = dataset['X'].astype('float'), dataset['Y'].astype('float')
        dataset['Distance X'] = dataset['X End'] - dataset['X']
        dataset['Distance Y'] = (dataset['Y End'] - dataset['Y'])*(-1)

    dataset[['New X','New Y']] = ''

    for i in range(len(dataset)):

        dataset['New X'][i] = dataset.X[i] + 10 
        dataset['New Y'][i] = 70 - dataset.Y[i] 

    (fig,ax) = draw_pitch_horizontal() 
    plt.ylim(-2, 72)
    plt.xlim(-2, 120.4)
    plt.axis('off')

    print(dataset)

    for i in range(len(dataset)):

        if dataset['Type de jeu au pied'][i] in ['PENALTOUCHE',"COUP D'ENVOI",'PENALTOUCHE, PENALTOUCHE','RENVOI EN BUT','PENALTOUCHE, GAP']:
            pass

        else:
            
            if dataset['Type de jeu au pied'][i] in list(dico_color.keys()):
                plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
                color = dico_color[dataset['Type de jeu au pied'][i]])
            else:
                plt.arrow(dataset['New X'][i],dataset['New Y'][i],dataset['Distance X'][i],dataset['Distance Y'][i],head_width = 1,width = 0.05,
                color = 'grey')
        
    if opta == False:
        plt.title('Kicking Game - ' + dataset['Timeline'][i] + '\n\n' + "Adversaire" + '\n',fontweight='semibold',fontsize=11)
    else:

        plt.title('Kicking Game - ' + list(dataset['Row'].unique())[0] + '\n',fontweight='semibold',fontsize=11)

    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    img = Image.open(buf)

    return img

def df_from_request(joueur,liste_url):

    df_global = pd.DataFrame()
    
    if type(liste_url) == str:
        
        url = liste_url
        numbers = re.findall('\d+', url)[0]
        url_international = f'https://www.itsrugby.fr/joueur-internationale-{numbers}.html'
        
        liste_url = [liste_url,url_international]
        
    for url in liste_url:
        
        response = requests.get(url)
        data = response.content

        soup = BeautifulSoup(data, 'lxml')

        div_element = soup.find('div', class_='table-responsive-md')

        if div_element:
            tbody = div_element.find('tbody')
            if tbody:

                df = pd.DataFrame()

                for tr in tbody.find_all('tr'):

                    liste_td = []

                    for td in tr.find_all('td'):

                        if td.text != '' : 

                            text = td.text.replace('\n\t\t\xa0\xa0','')
                            liste_td.append(text)  

                    if len(liste_td) == 13:

                        df1 = pd.DataFrame(liste_td).T
                        df = pd.concat([df,df1])

                    elif len(liste_td) == 11:

                        liste_td = ['',''] + liste_td
                        df1 = pd.DataFrame(liste_td).T
                        df = pd.concat([df,df1])
            else:
                print("No tbody found in the specified div.")
        else:
            print("No div with class 'table-responsive-md' found.")
            
        if len(df) > 0:

            df.columns = ['Saison','Club','Compétition','Pts','J.','Tit.','E.','P.','Dp.','Tr.','CJ','CR','Min.']

            df = df.replace('',np.nan).reset_index(drop=True)

            df['Saison'], df['Club'] = df['Saison'].ffill(),  df['Club'].ffill()

            df['Joueur'] = joueur

            df = df[['Joueur'] + list(df.columns)[:-1]]

            if 'internationale' in url:
                df.insert(4,'Club/Nation','Nation')
            else:
                df.insert(4,'Club/Nation','Club')

            df = df[df['Compétition'].str.contains('7') == False]
            
            df_global = pd.concat([df_global,df]).reset_index(drop=True)
        
    print(f'Données de {joueur} téléchargés.')
    
    df_global = df_global.replace('-',0)
            
    return df_global


def df_exp_compo(url):

    response = requests.get(url)
    data = response.content

    soup = BeautifulSoup(data, 'lxml')

    elements = soup.find_all(class_='col-5 text-center itsfontsize')

    liste_equipe = []

    for element in elements:

        text = element.get_text(strip=True)  
        if text : liste_equipe.append(text)

    table = soup.find_all('div',class_='table-responsive-md')
    compos = table[0]

    compos = compos.find_all('tr')

    hometeam, hometeam_ref, awayteam, awayteam_ref = [], [], [], []

    for elt in compos:

        player = elt.find('div')

        if player:

            players = elt.find_all('a')

            for i in range(len(players)):

                player = players[i]
                player_name = player.text
                player_href = 'https://www.itsrugby.fr/'+ player['href']

                if i == 0 : 

                    hometeam.append(player_name)
                    hometeam_ref.append(player_href)

                if i == 1 :

                    awayteam.append(player_name)
                    awayteam_ref.append(player_href)

    df_compo = pd.DataFrame({liste_equipe[0]:hometeam,liste_equipe[0]+'_Href':hometeam_ref,liste_equipe[1]:awayteam,liste_equipe[1]+'_Href':awayteam_ref})

    df_experience_match = pd.DataFrame()

    for equipe in liste_equipe:

        df_equipe = df_compo[[equipe,equipe+'_Href']].reset_index(drop=True)

        for i in range(len(df_equipe)):

            player, href = df_equipe[equipe][i], df_equipe[equipe+'_Href'][i]

            df_player = df_from_request(player,href)

            df_player['Equipe'] = equipe

            df_experience_match = pd.concat([df_experience_match,df_player]).reset_index(drop=True)
        
    for col in ['Pts','J.','Tit.','E.','P.','Dp.','Tr.','CJ','CR','Min.']:
    
        df_experience_match[col] = df_experience_match[col].astype('int')
    
    matchs_pro = df_experience_match.groupby('Equipe').sum()[['J.','Tit.']].T
    matchs_pro.index = ['Matchs Pros','Titularisations Pros']

    sélections_internationales = df_experience_match[df_experience_match['Club/Nation'] == 'Nation'].groupby('Equipe').sum()[['J.']].T
    sélections_internationales.index = ['Sélections internationales']

    matchs_top14 =  df_experience_match[df_experience_match['Compétition'] == 'Top 14'].groupby('Equipe').sum()[['J.']].T
    matchs_top14.index = ['Matchs Top 14']

    matchs_club = df_experience_match[df_experience_match['Club'] == df_experience_match['Equipe']].groupby('Equipe').sum()[['J.']].T
    matchs_club.index = ['Matchs au sein du club']

    df_summary = pd.concat([matchs_pro,sélections_internationales,matchs_top14,matchs_club])[liste_equipe]

    return df_experience_match, df_summary   

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def rearrange_name(name):
    parts = name.split()  
    if len(parts) > 1:
        return parts[-1] + ' ' + ' '.join(parts[:-1])  
    return name 

def keep_capitals(name):
    return ''.join([char for char in name if char.isupper()])

def function_df_match(df):
        
    ## filters
    df_match = df[df.Row == 'Jeu au Pied Racing'].reset_index(drop=True)
    df_match = df_match[df_match['Type de jeu au pied'] != "COUP D'ENVOI"].reset_index(drop=True)

    df_match = df_match[['Timeline','Period','Row','GameTime','Joueurs','Resultat jap','Résultat','Type de jeu au pied']]


    ## résultat processing
    df_match['Résultat'] = np.select([df_match['Résultat'] == "Positif"],[1],[-1])
    df_match['Résultat_Color'] = np.select([df_match['Résultat'] == 1],["#008001"],default="darkred")

    ## joueurs processing
    df_match['Joueurs'] = df_match['Joueurs'].apply(rearrange_name)
    df_match['Capitals'] = df_match['Joueurs'].apply(keep_capitals)

    ## type de jeu au pied
    '''
    df_match['Type de jeu au pied'] = df_match['Type de jeu au pied'].str.replace('PENALTOUCHE','PT')
    df_match['Type de jeu au pied'] = df_match['Type de jeu au pied'].str.replace('TOUCHE','T')
    df_match['Type de jeu au pied'] = df_match['Type de jeu au pied'].str.replace('RENVOI EN BUT','RENV')
    '''

    return df_match

def function_points_flow(df):
        
    df_points = df[df.Row.str.contains('Points')].reset_index(drop=True)
    df_points = df_points[['Timeline','Row','GameTime','Points']]
    df_points = df_points.sort_values(by='GameTime').reset_index(drop=True)

    df_points['Team'] = np.select([df_points['Row'] == "Points Racing"],['Racing 92'],['Adversaire'])

    df_points['Points_Number'] = np.select([df_points['Points'] == "CPP +",df_points['Points'] == "Essai",df_points['Points'] == "Transfo +"],[3,5,2],default=0)

    df_points['Points_Racing'] = np.select([df_points['Team'] == 'Racing 92'],[df_points['Points_Number']],default=0)
    df_points['Cumul_Points_Racing'] = np.cumsum(df_points['Points_Racing'])

    df_points['Points_Adversaire'] = np.select([df_points['Team'] == 'Adversaire'],[df_points['Points_Number']],default=0)
    df_points['Cumul_Points_Adversaire'] = np.cumsum(df_points['Points_Adversaire'])

    df_points['Ecart_Score'] = df_points['Cumul_Points_Racing'] - df_points['Cumul_Points_Adversaire']

    df_points = df_points[['GameTime','Ecart_Score']]

    debut = pd.DataFrame({'GameTime':[0],'Ecart_Score':[0]})
    fin = pd.DataFrame({'GameTime':[80],'Ecart_Score':[df_points['Ecart_Score'].iloc[-1]]})

    df_points = pd.concat([debut,df_points]).reset_index(drop=True)
    df_points = pd.concat([df_points, fin]).reset_index(drop=True)

    df_points['Ecart_Score'] = df_points['Ecart_Score']/abs(df_points['Ecart_Score']).max()

    return df_points

def function_points_flow2(df):
        
    df_points = df[df.Row.str.contains('Points')].reset_index(drop=True)
    df_points = df_points[['Timeline','Row','GameTime','Points']]
    df_points = df_points.sort_values(by='GameTime').reset_index(drop=True)

    df_points['Team'] = np.select([df_points['Row'] == "Points Racing"],['Racing 92'],['Adversaire'])

    df_points['Points_Number'] = np.select([df_points['Points'] == "CPP +",df_points['Points'] == "Essai",df_points['Points'] == "Transfo +"],[3,5,2],default=0)

    df_points['Points_Racing'] = np.select([df_points['Team'] == 'Racing 92'],[df_points['Points_Number']],default=0)
    df_points['Cumul_Points_Racing'] = np.cumsum(df_points['Points_Racing'])

    df_points['Points_Adversaire'] = np.select([df_points['Team'] == 'Adversaire'],[df_points['Points_Number']],default=0)
    df_points['Cumul_Points_Adversaire'] = np.cumsum(df_points['Points_Adversaire'])

    df_points['Ecart_Score'] = df_points['Cumul_Points_Racing'] - df_points['Cumul_Points_Adversaire']

    df_points = df_points[['GameTime','Ecart_Score']]

    debut = pd.DataFrame({'GameTime':[0],'Ecart_Score':[0]})
    fin = pd.DataFrame({'GameTime':[80],'Ecart_Score':[df_points['Ecart_Score'].iloc[-1]]})

    df_points = pd.concat([debut,df_points]).reset_index(drop=True)
    df_points = pd.concat([df_points, fin]).reset_index(drop=True)

    df_points['Ecart_Score'] = df_points['Ecart_Score']/abs(df_points['Ecart_Score']).max()

    return df_points

def gametime_graph1(df):

    df['GameTime'] = df['GameTime'].astype('string')
    df['Minutes'], df['Secondes'] = df['GameTime'].str[3:5].fillna('0'), df['GameTime'].str[6:8].fillna('0')
    df['Minutes'] = pd.to_numeric(df['Minutes'], errors='coerce').fillna(0).astype(int)
    df['Secondes'] = pd.to_numeric(df['Secondes'], errors='coerce').fillna(0).astype(float) / 60
    df.loc[(df['Period'] == 2) | (df['Period'] == '2'), 'Minutes'] = df['Minutes'] + 40
    df['GameTime'] = df['Minutes'] + df['Secondes']

    df_match = function_df_match(df)

    df_points = function_points_flow(df)

    fig, ax = plt.subplots(figsize=(15,6))  

    ax.axhspan(0.8, 1.2, xmin=0, xmax=80, facecolor='#008001', alpha=0.3)
    ax.axhspan(-1.2, -0.8, xmin=0, xmax=80, facecolor='darkred', alpha=0.3)
    
    ax.scatter(df_match['GameTime'],df_match['Résultat'],s=100,color=df_match['Résultat_Color'])
    ax.plot(df_match['GameTime'],df_match['Résultat'],color='darkgrey',linewidth=0.3)
    
    for i in range(len(df_match)):
        ax.annotate(df_match['Capitals'][i],(df_match['GameTime'][i] - 0.5,df_match['Résultat'][i] + 0.1),fontsize=6)
        if df_match['Type de jeu au pied'][i] == 'PENALTOUCHE':
            ax.annotate('PT',(df_match['GameTime'][i] - 0.35,df_match['Résultat'][i] + 0.05),fontsize=5)
        elif df_match['Type de jeu au pied'][i] == 'PIE':
            ax.annotate(df_match['Type de jeu au pied'][i],(df_match['GameTime'][i] - 0.35,df_match['Résultat'][i] + 0.05),fontsize=5)
        elif df_match['Type de jeu au pied'][i] == 'POULE':
            ax.annotate(df_match['Type de jeu au pied'][i],(df_match['GameTime'][i] - 0.9,df_match['Résultat'][i] + 0.05),fontsize=5)
        elif df_match['Type de jeu au pied'][i] == 'TOUCHE':
            ax.annotate(df_match['Type de jeu au pied'][i],(df_match['GameTime'][i] - 0.9,df_match['Résultat'][i] + 0.05),fontsize=5)
        elif df_match['Type de jeu au pied'][i] == 'RENVOI EN BUT':
            ax.annotate("RENVOI",(df_match['GameTime'][i] - 0.9,df_match['Résultat'][i] + 0.05),fontsize=5)
        elif df_match['Type de jeu au pied'][i] == 'AIGLE':
            ax.annotate(df_match['Type de jeu au pied'][i],(df_match['GameTime'][i] - 0.7,df_match['Résultat'][i] + 0.05),fontsize=5)
        else:
            ax.annotate(df_match['Type de jeu au pied'][i],(df_match['GameTime'][i] - 0.5,df_match['Résultat'][i] + 0.05),fontsize=6)
    
    ax.axhline(0,linewidth=0.5,color='darkgrey')
    ax.step(df_points['GameTime'],df_points['Ecart_Score'],color='black',where='post')
    
    ax.set_xlim(-1,81)
    ax.set_ylim(-1.2,1.2)

    try:
        title = df_match['Timeline'][0]
        title = title[:title.index('(') - 1]
    except:
        title = ''
    
    ax.set_title('\n' + title + '\n\n',fontsize=8,fontweight='semibold')
    ax.set_yticks([])
    
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    buf = io.BytesIO()
    fig.savefig(buf)  # Save the figure to the buffer
    buf.seek(0)
    img = Image.open(buf)

    return img

def gametime_graph2(df):

    df['GameTime'] = df['GameTime'].astype('string')
    df['Minutes'], df['Secondes'] = df['GameTime'].str[3:5].fillna('0'), df['GameTime'].str[6:8].fillna('0')
    df['Minutes'] = pd.to_numeric(df['Minutes'], errors='coerce').fillna(0).astype(int)
    df['Secondes'] = pd.to_numeric(df['Secondes'], errors='coerce').fillna(0).astype(float) / 60
    df.loc[(df['Period'] == 2) | (df['Period'] == '2'), 'Minutes'] = df['Minutes'] + 40
    df['GameTime'] = df['Minutes'] + df['Secondes']

    df_match = function_df_match(df)

    df_points = function_points_flow(df)

    fig, ax = plt.subplots(figsize=(15,6))  # Create figure and axis
    
    ax.axhspan(0, 1.0, xmin=0, xmax=80, facecolor='#008001', alpha=0.15)
    ax.axhspan(0, -1.0, xmin=0, xmax=80, facecolor='darkred', alpha=0.15)
    
    ax.scatter(df_match['GameTime'],[0 for value in df_match['GameTime']],s=100,color=df_match['Résultat_Color'])
    
    for i in range(len(df_match)):
        ax.annotate(df_match['Capitals'][i],(df_match['GameTime'][i] - 0.5,0.08),fontsize=6)
    
    ax.axhline(0,linewidth=0.5,color='darkgrey')
    ax.step(df_points['GameTime'],df_points['Ecart_Score'],color='black',where='post')
    
    ax.set_xlim(-1,81)
    ax.set_ylim(-1.05,1.1)

    try:
        title = df_match['Timeline'][0]
        title = title[:title.index('(') - 1]
    except:
        title = ''
    
    ax.set_title('\n' + title,fontsize=8,fontweight='semibold')
    ax.set_yticks([])
    
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    buf = io.BytesIO()
    fig.savefig(buf)  # Save the figure to the buffer
    buf.seek(0)
    img = Image.open(buf)

    return img

########################################################################################################################################
########################################################################################################################################
########################################################################################################################################


def from_match_time_to_min_and_sec(df_already_reduced : pd.DataFrame) -> pd.DataFrame:
    
    # Fonction qui prend en argument un pd.DataFrame qui contient au moins une colonne "Match Time" :
    # Entier de 1 à 5 chiffres : les 2 derniers chiffres correspondent aux secondes / les chiffres précédents correspondent aux minutes
    # La fonction renvoie le même pd.DataFrame avec 3 colonnes en plus :
    # "Minutes" = l'entier correspondant aux minutes de "Match Time"
    # "Secondes" = l'entier correspondant aux secondes de "Match Time"
    # "Match_Time_2" = un float à 2 décimales correspondant au temps décimal de Match Time (ex : Match Time = 4315 -> Match_Time_2 = 43,25)
    
    df_fonction = df_already_reduced.copy()
     
    # Seule condition pour que la fonction tourne : avoir une colonne "Match Time" dans le dataframe 
    if "Match Time" in df_already_reduced.columns:
                
        # Initialisation
        df_fonction['Minutes']= None
        df_fonction['Secondes'] = None
        df_fonction['Match_Time_2'] = None
        
        # Rendre la colonne "Match Time" traitable 
        df_fonction = df_fonction.sort_values("Match Time").reset_index(drop=True) # Trie + réinitialisation des index
        df_fonction["Match Time"] = df_fonction["Match Time"].astype(int) # Match Time = 3245.0 -> Match Time = 3245
        df_fonction["Match Time"] = df_fonction["Match Time"].astype('string')
        
        for i in range(len(df_fonction)) :
            
            # Match Time à 2 chiffres ou moins <=> 0 minute 
            if len(df_fonction.loc[i, "Match Time"]) <= 2 :
                df_fonction.loc[i, "Minutes"] = 0
                df_fonction.loc[i, "Secondes"] = df_fonction.loc[i, "Match Time"][0:2]
            # Match Time à 3 chiffres  <=> 1 minute <= Match Time < 10 minutes
            elif len(df_fonction.loc[i, "Match Time"]) == 3 :
                df_fonction.loc[i, "Minutes"] = df_fonction.loc[i, "Match Time"][0:1]
                df_fonction.loc[i, "Secondes"] = df_fonction.loc[i, "Match Time"][1:3]
            # Match Time à 4 chiffres  <=> 10 minutes <= Match Time < 100 minutes
            elif len(df_fonction.loc[i, "Match Time"]) == 4 :
                df_fonction.loc[i, "Minutes"] = df_fonction.loc[i, "Match Time"][0:2]
                df_fonction.loc[i, "Secondes"] = df_fonction.loc[i, "Match Time"][2:4]
            # Match Time à 5 chiffres  <=> 100 minutes <= Match Time
            elif len(df_fonction.loc[i, "Match Time"]) == 5 :
                df_fonction.loc[i, "Minutes"] = df_fonction.loc[i, "Match Time"][0:3]
                df_fonction.loc[i, "Secondes"] = df_fonction.loc[i, "Match Time"][3:5]
                
        df_fonction['Minutes'] = pd.to_numeric(df_fonction['Minutes'], errors='coerce').astype(int)
        df_fonction['Secondes'] = pd.to_numeric(df_fonction['Secondes'], errors='coerce').astype(int)
        df_fonction['Match_Time_2'] = df_fonction['Minutes'] + round(df_fonction['Secondes']/60.0 , 2)
    
        return df_fonction
    
    else :
        print(f"ERREUR (fonction 'from_match_time_to_min_and_sec') -> La colonne 'Match Time' n'est pas dans le dataframe donné en argument. \nPas possible de créer les colonnes 'Minutes', 'Secondes' et 'Match_Time_2'.\nFin de l'exécution.\n")
        
        return df_fonction


def from_df_match_to_kicking_game(df_match :pd.DataFrame) -> pd.DataFrame :
    
    
    list_columns_to_keep_opta = ["Start time","Player","Match Time","Period","Row","Kick Types"]
    list_columns_to_keep_analyst = ["Start time","Joueurs","Mi temps","Qualite de JAP"]
    
    for c1 in list_columns_to_keep_opta :
        if c1 not in  df_match.columns :
            return print(f"ERREUR (fonction 'from_df_match_to_kicking_game') -> La colonne '{c1}' n'est pas dans le dataframe donné en argument. \nPas possible de créer le df_kick_opta.\nFin de l'exécution.\n")
    
    for c2 in list_columns_to_keep_analyst :
        if c2 not in  df_match.columns :
            return print(f"ERREUR (fonction 'from_df_match_to_kicking_game') -> La colonne '{c2}' n'est pas dans le dataframe donné en argument. \nPas possible de créer le df_kick_analyst.\nFin de l'exécution.\n")
        
    main_label = "Row"
    name_racing_kick_opta = "Racing 92 Kicks"
    name_racing_kick_analyst = "Jeu au pied Racing"
    label_kick_type_opta = "Kick Types"
    name_not_to_consider_kick_opta = "Penalty Kick"
    
    ### EXTRACTION INFO OPTA ###
    df_kick_opta = df_match[(df_match[main_label]==name_racing_kick_opta) & (df_match[label_kick_type_opta]!=name_not_to_consider_kick_opta)].reset_index(drop=True)
    df_kick_opta = df_kick_opta[list_columns_to_keep_opta]
    
    if df_kick_opta.empty :
        print("ALERTE (fonction 'from_df_match_to_kicking_game') -> /!\ Attention df_kick_opta anormalement vide.\n")
    
    ### EXTRACTION INFO ANALYST ###
    df_kick_analyst = df_match[df_match[main_label]==name_racing_kick_analyst].reset_index(drop=True)
    df_kick_analyst = df_kick_analyst[list_columns_to_keep_analyst]
    
    if df_kick_analyst.empty :
        print("ALERTE (fonction 'from_df_match_to_kicking_game') -> /!\ Attention df_kick_analyst anormalement vide.\n")
    
    try :
        df_kick_analyst["Mi temps"] = df_kick_analyst["Mi temps"].str[0]
    except :
        return print("ALERTE (fonction 'from_df_match_to_kicking_game') -> /!\ Attention la colonne 'Mi temps' n'est pas du bon type (str).\nFin de l'exécution.\n")
    
    time_analyst = "Start time"
    time_opta = "Start time"
    label_mi_temps_analyst = "Mi temps"
    label_mi_temps_opta = "Period"
    label_kicker_analyst = "Joueurs"
    label_kicker_opta = "Player"
    label_match_time_opta = "Match Time"

    df1_sorted = df_kick_analyst.sort_values(time_analyst).reset_index(drop=True).copy()
    df2_sorted = df_kick_opta.sort_values(time_opta).reset_index(drop=True).copy()

    used_idx_df2 = set()
    match_time_list = []
    delta_list = []
    start_time_opta_list = []
    player_opta_list = []
    correspondance_city_list = []
    period_df2_list = []
    correspondance_period_list = []

    for idx1, row1 in df1_sorted.iterrows():
        # Filtrer df2 pour avoir une correspondance sur les Mi-temps
        df2_candidates = df2_sorted[
            (df2_sorted[label_mi_temps_opta] == row1[label_mi_temps_analyst]) &
            (~df2_sorted.index.isin(used_idx_df2))
        ]

        if not df2_candidates.empty:
            df2_candidates = df2_candidates.assign(delta=np.abs(df2_candidates[time_opta] - row1[time_analyst]))
            
            # Filtrage supplémentaire : ne garder que 1 < delta < 6
            df2_candidates = df2_candidates[(df2_candidates["delta"] > 1.0) & (df2_candidates["delta"] < 6.0)]

            # S’il reste des candidats valides, on prend le plus proche
            if not df2_candidates.empty:
                best_match = df2_candidates.loc[df2_candidates["delta"].idxmin()]         

            # Ajouter les informations
            match_time_list.append(best_match[label_match_time_opta])
            start_time_opta_list.append(best_match[time_opta])
            delta_list.append(round(best_match["delta"],2))
            player_opta_list.append(best_match[label_kicker_opta])
            correspondance_city_list.append(best_match[label_kicker_opta] == row1[label_kicker_analyst])
            period_df2_list.append(best_match[label_mi_temps_opta])
            correspondance_period_list.append(best_match[label_mi_temps_opta] == row1[label_mi_temps_analyst])

            used_idx_df2.add(best_match.name)
        else:
            match_time_list.append(np.nan)
            start_time_opta_list.append(np.nan)
            delta_list.append(np.nan)
            player_opta_list.append(np.nan)
            correspondance_city_list.append(np.nan)
            period_df2_list.append(np.nan)
            correspondance_period_list.append(np.nan)

    # Création de df3
    df3 = df1_sorted.copy()
    df3['Résultat_Color'] = np.select([df3['Qualite de JAP'] == 'Positif'],["#008001"],default="darkred")
    df3["Match Time"] = match_time_list
    df3["delta"] = delta_list
    df3["Player (OPTA)"] = player_opta_list
    df3["Correspondance Joueur"] = correspondance_city_list
    df3["Star time (OPTA)"] = start_time_opta_list
    
    # TRANSFORMATION DE LA COLONNE 'MATCH TIME' EN COLONNE 'MINUTES' & 'SECONDES' 
    df3 = from_match_time_to_min_and_sec(df3)
    
    # NETTOYAGE DES DONNEES :
    # ... raccourcir la partie décimale de 'Start time'
    df3[time_analyst] = round(df3[time_analyst],2)
    # ... Supprimer la ligne si "Qualite de JAP" == NaN
    df3 = df3.dropna(subset=["Qualite de JAP"])
    # ... Si la valeur "Joueurs" possède une "," alors prendre la valeur "Player (OPTA)"
    # df3["Joueurs"] = df3["Joueurs"].astype(str)
    # df3.loc[df3["Joueurs"].str.contains(",", na=False), "Joueurs"] = df3["Player (OPTA)"]
    # ... Réorganiser les colonnes :
    cols = ["Match Time","Match_Time_2","Minutes","Secondes","Qualite de JAP","Résultat_Color","Start time","Star time (OPTA)","delta","Correspondance Joueur","Joueurs","Player (OPTA)","Mi temps"]
    df3 = df3[cols]
        
    return df3


def extraction_df_point_game(big_df) :
    
    list_columns_to_keep = ["Row", "Match Time", "Event", "Goal Kick Type"]
    
    for c1 in list_columns_to_keep :
        if c1 not in  big_df.columns :
            return print(f"ERREUR (fonction 'extraction_df_point_game') -> La colonne '{c1}' n'est pas dans le dataframe donné en argument. \nPas possible de créer le df_point_game.\nFin de l'exécution.\n")
    
    
    # EXTRACTION DES COLONNES NECESSAIRES DU DATAFRAME DU MATCH
    list_columns_to_keep = ["Row", "Match Time", "Event", "Goal Kick Type"]
    df_point_game = big_df[((big_df["Event"]=="Try") | ((big_df["Event"]=="Goal Kick") & (big_df["Goal Kick Outcome"] == "Goal Kicked" ))) & (big_df["Row"].str.contains("Tries|Kicks", na=False)) ].reset_index(drop=True)
    df_point_game = df_point_game[list_columns_to_keep]
    
    # TRANSFORMATION DE LA COLONNE 'MATCH TIME' EN COLONNE 'MINUTES' & 'SECONDES' 
    df_point_game = from_match_time_to_min_and_sec(df_point_game)
    
    # CALCUL DE L'EVOLUTION DU SCORE
    df_point_game["evolution_score"] = None  
    delta_point = 0
    
    for i in range(len(df_point_game)) :
        if "Racing 92" in df_point_game.loc[i, "Row"] :
            if df_point_game.loc[i, "Event"] == "Try" :
                delta_point += 5
            elif (df_point_game.loc[i, "Event"] == "Goal Kick") & (df_point_game.loc[i, "Goal Kick Type"] == "Conversion") :
                delta_point += 2
            elif (df_point_game.loc[i, "Event"] == "Goal Kick") & (df_point_game.loc[i, "Goal Kick Type"] == "Penalty Goal") :
                delta_point += 3
            else :
                delta_point += 3
                
        else :
            if df_point_game.loc[i, "Event"] == "Try" :
                delta_point += -5
            elif (df_point_game.loc[i, "Event"] == "Goal Kick") & (df_point_game.loc[i, "Goal Kick Type"] == "Conversion") :
                delta_point += -2
            elif (df_point_game.loc[i, "Event"] == "Goal Kick") & (df_point_game.loc[i, "Goal Kick Type"] == "Penalty Goal") :
                delta_point += -3
            else :
                delta_point += -3
                
        df_point_game.loc[i, "evolution_score"] = delta_point  
        
            
    return df_point_game


def gametime_graph3(df_match_graph):
    
    df_point_game = extraction_df_point_game(df_match_graph)
    df_kicking_game = from_df_match_to_kicking_game(df_match_graph)
    
    fig, ax = plt.subplots(figsize=(15,6))  # Create figure and axis
    
    titre = df_match_graph.iloc[0]["Timeline"]

    # Ajouter le point initial pour partir de y=0
    x = [0] + df_point_game['Match_Time_2'].tolist()
    y = [0] + df_point_game['evolution_score'].tolist()

    # Ajouter un dernier point pour continuer jusqu'à x = 80
    x.append(80)
    y.append(y[-1])  # même niveau que le dernier score

    # Tracé en escalier
    ax.step(x, y, color='black', where='post')
        
    max_evolution_score = df_point_game['evolution_score'].max()
    min_evolution_score = df_point_game['evolution_score'].min()
    
    limit = 0
    if max_evolution_score < abs(min_evolution_score) : 
        limit =  abs(min_evolution_score) + 3
    else :
        limit =  max_evolution_score + 3
    
    if limit % 5 != 0 :
        limit +=  5 - limit % 5
        
        
    
    ax.axhspan(ymin = 0, ymax = limit, xmin=0, xmax=80, facecolor='#008001', alpha=0.15)
    ax.axhspan(ymax = 0, ymin = - limit, xmin=0, xmax=80, facecolor='darkred', alpha=0.15)
    ax.scatter(df_kicking_game['Match_Time_2'],[0 for value in df_kicking_game['Match_Time_2']],s=100,color=df_kicking_game['Résultat_Color'])

    ax.set_xlim(-1,81)
    ax.set_ylim(-limit,limit) 
    
   
    if limit <= 15:
        tick_interval = 3
    elif limit <= 30:
        tick_interval = 5
    else:
        tick_interval = 10
    n_ticks = int(np.ceil(limit/tick_interval))
    yticks = np.linspace(-n_ticks*tick_interval, n_ticks*tick_interval, 2*n_ticks+1, dtype=int)
    yticks = yticks[np.abs(yticks) <= limit]
    ax.set_yticks(yticks)
    
    for y in yticks:
        if y != 0 :
            ax.axhline(y=y, color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    
    ax.set_xlabel("Minutes Match")
    ax.set_ylabel("Ecart Score")
    ax.set_title(titre)

    buf = io.BytesIO()
    fig.savefig(buf)  # Save the figure to the buffer
    buf.seek(0)
    img = Image.open(buf)

    return img

