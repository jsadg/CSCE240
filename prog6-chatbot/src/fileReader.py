#File reused from Tarun Ramkumar
from bs4 import BeautifulSoup
import requests
class FileReader:

    def scrapeFile(self,company):
        if(company == "Coinbase"):
            url = "https://www.sec.gov/Archives/edgar/data/1679788/000167978823000031/coin-20221231.htm"
            file = open("data/Coinbase.txt","w", encoding = "utf-8")

        elif(company == "Campbell"):
            url = "https://www.sec.gov/Archives/edgar/data/16732/000001673223000109/cpb-20230730.htm"
            file = open("data/Campbell.txt","w", encoding = "utf-8")

        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        }
        website = requests.get(url = url, headers = headers)
        html = website.content.decode("utf-8")
        parser = BeautifulSoup(html,"html.parser")
        start = False
        headers = []
        count = 0
        for i in parser.stripped_strings:
            line = str(i)

            if "Item 1." in i and start == False and count != 0:
                start = True
            if "Item 1." in i and count == 0:
                count+=1
            if(start):
                if(len(line) > 1):
                    file.write(line+"\n")
                    

        file.close










