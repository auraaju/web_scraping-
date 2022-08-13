from matplotlib.pyplot import text
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

rows = []
df = pd.DataFrame()
codeframe = pd.DataFrame()
url="https://www.dsebd.org/cbul.php"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
heading = soup.find_all('h2')[12].get_text()
x = heading.split('on')[1].strip().replace(" ", "_").replace(",","")
print('file_date '+x)
try: 
    circuit_table = soup.find('table', attrs='table table-bordered background-white text-center').find_all('tr')
    
    sl = []
    trade_code = []
    breaker_per = []
    ticker_size= []
    open_adj_price = []
    lower_limit = []
    upper_limit = []

    for i in range(1,len(circuit_table)):
        sl.append(circuit_table[i].find_all('td')[0].get_text().strip())
        trade_code.append(circuit_table[i].find_all('td')[1].get_text().strip())
        breaker_per.append(circuit_table[i].find_all('td')[2].get_text().strip())
        ticker_size.append(circuit_table[i].find_all('td')[3].get_text().strip())
        open_adj_price.append(circuit_table[i].find_all('td')[4].get_text().strip())
        lower_limit.append(circuit_table[i].find_all('td')[5].get_text().strip())
        upper_limit.append(circuit_table[i].find_all('td')[6].get_text().strip())

    
    d = {'SL':sl,'Trade Code':trade_code,'Breaker%':breaker_per,'Ticker Size':ticker_size,
            'Open Price':open_adj_price,'Lower Limit':lower_limit,'Upper Limit':upper_limit}
    code = {'Trade Code': trade_code}
    df = pd.DataFrame(d)
    codeframe = pd.DataFrame(code)
    
except:
    print('error occurred. ')

filepath1 = Path('dse_circuit/dse_circuit_'+x+'.csv')
filepath1.parent.mkdir(parents=True, exist_ok=True) 
df.to_csv(filepath1)
filepath2 = Path('./trade_code.csv')
filepath2.parent.mkdir(parents=True, exist_ok=True) 
codeframe.to_csv(filepath2)




