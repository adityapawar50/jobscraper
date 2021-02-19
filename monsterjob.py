import bs4, requests, time
from selenium import webdriver
#from selenium.webdriver import Safari

#goes on monster for dallas and lists all software jobs
def scrapeMonster():
    url='https://www.monster.com/jobs/search/?q=Software-Developer&where=Dallas'
    page=requests.get('https://www.monster.com/jobs/search/?q=Software-Developer&where=Dallas')
    print(page.raise_for_status)

    soup=bs4.BeautifulSoup(page.text, 'html.parser')
    results=soup.find(id='ResultsContainer')


    jobElems=results.find_all('section', class_ = 'card-content')

    for jobElem in jobElems:
        title=jobElem.find('h2', class_='title')
        company=jobElem.find('div',class_='company')
        location= jobElem.find('div', class_='location')
        if None in (title, company, location):
            continue
        print(title.text.strip())
        print(company.text.strip())
        print(location.text.strip())
        print('')









    
