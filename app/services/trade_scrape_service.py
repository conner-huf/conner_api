import requests
from bs4 import BeautifulSoup
from datetime import datetime

from app.models.trade_scrape.trade import Trade

class TradeScrapeService:
    
    @staticmethod
    def parse_filed_after(filed_after_str: str) -> int:
        return int(filed_after_str.replace("days", "").strip())

    @staticmethod
    async def get_trades_by_person(url):
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if not table:
            print("Failed to retrieve the table")
            return []
        
        rows = table.find('tbody').find_all('tr')
        trades = []

        for row in rows:
            cells = row.find_all('td')
            if len(cells) != 7:
                continue

            name = cells[0].find('h3', class_='issuer-name').get_text().strip()
            ticker = cells[0].find('span', class_='issuer-ticker').get_text().strip()
            published = cells[1].find('div', class_='text-size-3 font-medium').get_text().strip() + ' ' + cells[1].find('div', class_='text-size-2 text-txt-dimmer').get_text().strip()
            traded = cells[2].find('div', class_='text-size-3 font-medium').get_text().strip() + ' ' + cells[2].find('div', class_='text-size-2 text-txt-dimmer').get_text().strip()
            filed_after = TradeScrapeService.parse_filed_after(cells[3].get_text().strip())
            trade_type = cells[4].get_text().strip()
            size = cells[5].get_text().strip()

            trade_url_tag = cells[6].find('a')
            trade_url = f"https://www.capitoltrades.com{trade_url_tag['href']}"

            trade_data = {
                'issuer_name': name,
                'issuer_ticker': ticker,
                'published': published,
                'traded': traded,
                'filed_after_business_days': filed_after,
                'type': trade_type,
                'size': size,
                'trade_url': trade_url
            }
            
            trades.append(trade_data)
        
        return trades
