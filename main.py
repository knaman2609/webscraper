from requests_html import AsyncHTMLSession
import schedule
import time
import asyncio

url1 = 'https://www.ketto.org/fundraiser/help-Juveca_Panda-raise-funds-for-covid-19-relief?payment=form'
url2 = 'http://binai.in/'

async def scrape_web ():
    asession = AsyncHTMLSession()
    r = await asession.get(url2)
    await r.html.arender()

    statusDiv = r.html.find('div.desc')
    outF = open("outFile.txt", "w")

    for el in statusDiv:
        print ("wrinting now")
        outF.write(el.text)

def runScrapper ():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrape_web())

schedule.every(10).seconds.do(runScrapper)

while 1:
    schedule.run_pending()
    time.sleep(1)

