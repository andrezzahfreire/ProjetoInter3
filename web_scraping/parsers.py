import math

def toStr(text):
    if type(text) != str: return None
    return text.strip()

def toFloat(text):
    if type(text) in [float, int]:
        if math.isnan(text): return None
        return text
    text = text.strip().upper()
    if len(text) == 0: return None
    return float(text)

def toInt(text):
    if type(text) in [float, int]:
        if math.isnan(text): return None
        return text
    text = text.strip().upper()
    if len(text) == 0: return None
    return int(text)

def payload_standard(dado):
    return {
        # "Class.": toFloat(dado["Class."]),
        "jogador": toStr(dado["Jogador"]),
        "nacionalidade": toStr(dado["Nação"]),
        "posicao": toStr(dado["Pos."]),
        "equipe": toStr(dado["Equipe"]),
        "idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        
        "indices": {
            "MP": toFloat(dado["MP"]),
            "Inícios": toFloat(dado["Inícios"]),
            "Min.": toFloat(dado["Min."]),
            "90s": toFloat(dado["90s"]),
            "Gols": toFloat(dado["Gols"]),
            "Assis.": toFloat(dado["Assis."]),
            "G+A": toFloat(dado["G+A"]),
            "G-PB": toFloat(dado["G-PB"]),
            "PB": toFloat(dado["PB"]),
            "PT": toFloat(dado["PT"]),
            "CrtsA": toFloat(dado["CrtsA"]),
            "CrtV": toFloat(dado["CrtV"]),
            "xG": toFloat(dado["xG"]),
            "npxG": toFloat(dado["npxG"]),
            "xAG": toFloat(dado["xAG"]),
            "npxG+xAG": toFloat(dado["npxG+xAG"]),
            "PrgC": toFloat(dado["PrgC"]),
            "PrgP": toFloat(dado["PrgP"]),
            "PrgR": toFloat(dado["PrgR"]),
            "Gols.1": toFloat(dado["Gols.1"]),
            "Assis..1": toFloat(dado["Assis..1"]),
            "G+A.1": toFloat(dado["G+A.1"]),
            "G-PB.1": toFloat(dado["G-PB.1"]),
            "G+A-PB": toFloat(dado["G+A-PB"]),
            "xG.1": toFloat(dado["xG.1"]),
            "xAG.1": toFloat(dado["xAG.1"]),
            "xG+xAG": toFloat(dado["xG+xAG"]),    
            "npxG.1": toFloat(dado["npxG.1"]),
            "npxG+xAG.1": toFloat(dado["npxG+xAG.1"]),
        },
        # "Partidas": "Partidas",
    }   

def payload_passing(dado):
    return {
        "Class.": toFloat(dado["Class."]),
        "Jogador": toStr(dado["Jogador"]),
        "Nação": toStr(dado["Nação"]),
        "Pos.": toStr(dado["Pos."]),
        "Equipe": toStr(dado["Equipe"]),
        "Idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        "indices": {
            "90s": toFloat(dado["90s"]),
            "Cmp": toInt(dado["Cmp"]),
            "Att": toInt(dado["Att"]),
            "Cmp%": toFloat(dado["Cmp%"]),
            "DistTot": toFloat(dado["DistTot"]),
            "DistPrg": toInt(dado['DistPrg']),
            
            "Cmp.1": toInt(dado["Cmp.1"]),
            "Att.1": toInt(dado["Att.1"]),
            "Cmp%.1": toFloat(dado["Cmp%.1"]),
            
            "Cmp.2": toInt(dado["Cmp.2"]),
            "Att.2": toInt(dado["Att.2"]),
            "Cmp%.2": toFloat(dado["Cmp%.2"]),
            
            "Cmp.3": toInt(dado["Cmp.3"]),
            "Att.3": toInt(dado["Att.3"]),
            "Cmp%.3": toFloat(dado["Cmp%.3"]),
            
            "Assis.": toInt(dado["Assis."]),
            "xAG": toFloat(dado["xAG"]),
            "xA": toFloat(dado["xA"]),
            "A-xAG": toFloat(dado["A-xAG"]),
            "KP": toInt(dado["KP"]),
            "1/3": toInt(dado["1/3"]),
            "PPA": toInt(dado["PPA"]),
            "CrsPA": toInt(dado["CrsPA"]),
            "PrgP": toInt(dado["PrgP"]),
        },
        # "Partidas": "Partidas",
    }   
    
def payload_keepersadv(dado): 
    return {
        "Class.": toFloat(dado["Class."]),
        "jogador": toStr(dado["Jogador"]),
        "nacionalidade": toStr(dado["Nação"]),
        "posicao": toStr(dado["Pos."]),
        "equipe": toStr(dado["Equipe"]),
        "idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        "indices": {
            "90s": toFloat(dado["90s"]),
            "GC": toInt(dado["GC"]),
            "GPC": toInt(dado["GPC"]),
            "TD": toInt(dado["TD"]),
            "GC.1": toInt(dado["GC.1"]),
            "OG": toInt(dado["OG"]),
            
            "PSxG": toFloat(dado["PSxG"]),
            "PSxG/SoT": toFloat(dado["PSxG/SoT"]),
            "PSxG+/-": toFloat(dado["PSxG+/-"]),
            "/90": toFloat(dado["/90"]),
            
            "Cmp": toInt(dado["Cmp"]),
            "Att": toInt(dado["Att"]),
            "Cmp%": toInt(dado["Cmp%"]),
            
            "Tent. de passes (Gol.)": toInt(dado["Tent. de passes (Gol.)"]),
            "Lançamentos%": toFloat(dado["Lançamentos%"]),
            "CompMéd": toFloat(dado["CompMéd"]),
            
            "Att.1": toInt(dado["Att.1"]),
            "Lançamentos%.1": toFloat(dado["Lançamentos%.1"]),
            "CompMéd.1": toFloat(dado["CompMéd.1"]),
            
            "Oponente": toInt(dado["Oponente"]),
            "Stp": toInt(dado["Stp"]),
            "Stp%": toFloat(dado["Stp%"]),
            
            "#OPA": toInt(dado["#OPA"]),
            "#OPA/90": toFloat(dado["#OPA/90"]),
            "DistMéd": toFloat(dado["DistMéd"]),
        }
    }

def payload_shooting(dado): 
    return {
        "Class.": toFloat(dado["Class."]),
        "jogador": toStr(dado["Jogador"]),
        "nacionalidade": toStr(dado["Nação"]),
        "posicao": toStr(dado["Pos."]),
        "equipe": toStr(dado["Equipe"]),
        "idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        "indices": {
            "90s": toFloat(dado["90s"]),
            
            "Gols" : toInt(dado["Gols"]),
            "TC": toInt(dado["TC"]),
            "CaG": toInt(dado["CaG"]),
            "SoT%": toFloat(dado["SoT%"]),
            "Sh/90": toFloat(dado["SoT%"]),
            "SoT/90": toFloat(dado["SoT/90"]),
            "G/Sh": toFloat(dado["G/Sh"]),
            "G/SoT": toFloat(dado["G/SoT"]),
            "Dist": toFloat(dado["Dist"]),
            "FK": toInt(dado["FK"]),
            "PB": toInt(dado["PB"]),
            "PT": toInt(dado["PT"]),
            
            "xG": toFloat(dado["xG"]),
            "npxG": toFloat(dado["npxG"]),
            "npxG/Sh": toFloat(dado["npxG/Sh"]),
            "G-xG": toFloat(dado["G-xG"]),
            "np:G-xG": toFloat(dado["np:G-xG"])
        }
    }
    
def payload_passing_types(dado): 
    return {
        "Class.": toFloat(dado["Class."]),
        "jogador": toStr(dado["Jogador"]),
        "nacionalidade": toStr(dado["Nação"]),
        "posicao": toStr(dado["Pos."]),
        "equipe": toStr(dado["Equipe"]),
        "idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        "indices": {
            "90s": toFloat(dado["90s"]),
            "Att": toInt(dado["Att"]),
            
            "Em jogo": toInt(dado["Em jogo"]),
            "Parado": toFloat(dado["Parado"]),
            "FK": toInt(dado["FK"]),
            "TB": toInt(dado["TB"]),
            "Sw": toInt(dado["Sw"]),
            "Crz": toInt(dado["Crz"]),
            "TI": toInt(dado["TI"]),
            "CK": toInt(dado["CK"]),
            
            "In": toInt(dado["In"]),
            "Fora": toInt(dado["Fora"]),
            "Reto": toInt(dado["Reto"]),
            
            "Cmp": toInt(dado["Cmp"]),
            "Desativado": toInt(dado["Desativado"]),
            "Bloqueios": toInt(dado["Bloqueios"]),       
    }
}


def payload_gca(dado): 
    return {
        "Class.": toFloat(dado["Class."]),
        "jogador": toStr(dado["Jogador"]),
        "nacionalidade": toStr(dado["Nação"]),
        "posicao": toStr(dado["Pos."]),
        "equipe": toStr(dado["Equipe"]),
        "idade": toInt(dado["Idade"]),
        "nascimento": toInt(dado["Nascimento"]),
        "indices": {
            "90s": toFloat(dado["90s"]),
            
            "SCA": toFloat(dado["SCA"]),
            "SCA90": toFloat(dado["SCA90"]),
         
            "Passe em jogo": toInt(dado["Passe em jogo"]),   
            "Passe de bola parada": toInt(dado["Passe de bola parada"]),   
            "TO": toInt(dado["TO"]),   
            "TC": toInt(dado["TC"]),   
            "FltsP": toInt(dado["FltsP"]),   
            "Def": toInt(dado["Def"]),   
            
            "GCA": toInt(dado["GCA"]),   
            "GCA90": toInt(dado["GCA90"]),
               
            "Passe em jogo.1": toInt(dado["Passe em jogo.1"]),   
            "SCA": toInt(dado["SCA"]),   
            "SCA": toInt(dado["SCA"]),   
            "SCA": toInt(dado["SCA"]),   
            "SCA": toInt(dado["SCA"]),   
        }
    }