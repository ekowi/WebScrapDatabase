import requests
from bs4 import BeautifulSoup

def get_data():
     url = "https://www.bmkg.go.id/"
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

     try:
          content = requests.get(url,   headers=headers)
          if content.status_code == 200:
               soup = BeautifulSoup(content.text,      'html.parser')

               waktu = soup.find(class_= 'waktu')
               waktu = waktu.text.split(',')
               tanggal = waktu[0]
               jam = waktu[1]

               data = soup.find(class_= 'col-md-4 md-margin-bottom-10')
               result = data.findChildren('li')
               for i in result:
                    print(i)

     except Exception:
               print('cek program')




get_data()
