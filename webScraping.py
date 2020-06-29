from bs4 import BeautifulSoup
import requests
import csv
for i in range(1,12): 
    src = requests.get('https://www.adverts.ie/for-sale/q_nes+games/page-'+str(i)).text
    soup = BeautifulSoup(src,'lxml')
    
    csv_file = open('NesDescriptionScrap.csv', 'a')#write results to this file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['title','price','location'])

    for t in soup.find_all('div',class_='item-details'):
        title = t.find('div',class_='title').a.text
        print(title)
        price = t.find('div',class_='price').a.text
        print(price)
        location = t.find('div',class_='location').a.text
        print(location)
        csv_writer.writerow([title,price,location])#pass variables to headers in csv file
csv_file.close()