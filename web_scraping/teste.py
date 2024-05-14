from pprint import pp

urls = [
    "https://fbref.com/pt/comps/24/2023/stats/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/keepersadv/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/shooting/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/passing/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/passing_types/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/gca/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/possession/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/playingtime/2023-Serie-A-estatisticas", 
    "https://fbref.com/pt/comps/24/2023/misc/2023-Serie-A-estatisticas"
]

table_ids = [
    "stats_standard", 
    "stats_passing", 
    "stats_keeper_adv", 
    "stats_shooting", 
    "stats_passing", 
    "stats_passing_types", 
    "stats_gca", 
    "stats_possession", 
    "stats_playing_time", 
    "stats_misc"
]

d = {}
for i in range(len(urls)):
    d[i] = {
        'url': urls[i],
        'table_id': table_ids[i]
    }
    
pp(d)