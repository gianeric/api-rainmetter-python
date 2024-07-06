import os
import requests
import logging
import pytz
from dotenv import load_dotenv
from datetime import datetime, timedelta


load_dotenv()

token = os.getenv('X_AUTH_TOKEN')
competitionIds = os.getenv('COMPETITION_IDS')

def get_header():
    return {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }

def get_match_params():
    today = datetime.now().strftime('%Y-%m-%d')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    params = {
        'competitions': competitionIds,
        'dateFrom': today,
        'dateTo': tomorrow
    }

    return params

def convert_utc_to_brt(utc_date):
    utc_time = datetime.strptime(utc_date, '%Y-%m-%dT%H:%M:%SZ')
    brt_time = utc_time.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('America/Sao_Paulo'))
    return brt_time.strftime('%H'+'h')

def get_max_size_from_short_name(matches):
    home = max(len(match['homeTeam']['shortName']) for match in matches)
    away = max(len(match['awayTeam']['shortName']) for match in matches)
    return max(home,away)

def request_matches():
    response = None

    try:
        headers = get_header()
        params = get_match_params()

        logging.info('Enviando requisição para api ...')
        response = requests.get('https://api.football-data.org/v4/matches',
                                 headers=headers,
                                 params=params)

        response.raise_for_status()
        
        logging.info('Requisição enviada com sucesso.')

        if 'matches' in response.json():
            matches = response.json()['matches']
            size_short_name = get_max_size_from_short_name(matches)
            
            with open("E:\\Projetos\\api-rainmetter-python\\football\\football.txt", "w", encoding="utf-8") as f:
                for match_data in matches:
                    utc_date   = convert_utc_to_brt(match_data['utcDate'])
                    home_team  = match_data['homeTeam']['shortName']
                    away_team  = match_data['awayTeam']['shortName']
                    score_home = match_data['score']['fullTime']['home'] if 'score' in match_data and 'fullTime' in match_data['score'] else None
                    score_away = match_data['score']['fullTime']['away'] if 'score' in match_data and 'fullTime' in match_data['score'] else None
                    
                    scoreHome_str = str(score_home) if score_home is not None else '0'
                    scoreAway_str = str(score_away) if score_away is not None else '0'
                    
                    text = f"{home_team} {scoreHome_str} x {scoreAway_str} {away_team}"
                    text = f"{home_team.ljust(size_short_name)} {scoreHome_str} x {scoreAway_str} {away_team.ljust(size_short_name)}"

                    f.write(f"{text}\n")

        return response
    except requests.exceptions.RequestException as e:
        if response is not None:

            if response.status_code != (500):
                raise Exception(response.json())
            else:
                raise Exception(f'Erro ao ler os dados da api de futebol.{e}')

        else:
            raise Exception(f'Erro ao ler os dados da api de futebol.{e}')

if __name__ == "__main__":
    request_matches()
