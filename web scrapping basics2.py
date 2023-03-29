from bs4 import BeautifulSoup
import requests
import csv


# print(soup.prettify())
csvfile=open("scrapped_data.csv",'w')

csv_writer=csv.writer(csvfile)
csv_writer.writerow(['headline','summary','Youtube link'])
for page in range(1,18):
    link=requests.get(f"https://coreyms.com/page/{page}").text

    soup=BeautifulSoup(link,"html.parser")

    for article in soup.find_all('article'):
        # print(article.prettify())
            headline=article.find(class_="entry-header").h2.a.text
            print(headline)

            summary=article.find(class_="entry-content").p.text
            print(summary)
            try:

                youtubevid=article.find(class_="youtube-player")['src']
                print(youtubevid)

                split1=youtubevid.split("/")
            # print(a)
                videoid=split1[4].split("?")[0]
                print(videoid)
                mainlink=f"https://www.youtube.com/watch?v={videoid}"
                print(mainlink)

            except Exception as message:
                    youtubevid=None
                    print(youtubevid)
                    mainlink=youtubevid
            print()
            csv_writer.writerow([headline,summary,mainlink])
csvfile.close()
