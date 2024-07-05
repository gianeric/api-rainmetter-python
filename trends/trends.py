from pytrends.request import TrendReq
import unicodedata


pytrends = TrendReq(hl='pt-BR', tz=360)

daily_trending_searches = pytrends.trending_searches(pn='brazil')

# Função para remover acentos e caracteres especiais
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

with open("E:\\Projetos\\api-rainmetter-python\\trends\\trends.txt", "w", encoding="utf-8") as f:
    for i, row in daily_trending_searches.iterrows():
        cleaned_trend = remove_accents(row[0])  # Remove acentos e caracteres especiais
        f.write(f"{i + 1}. {cleaned_trend}\n")
