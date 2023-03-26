from bs4 import BeautifulSoup
import requests

with open("D:\\Learning only\\abc.html") as htmlfile:
    soup=BeautifulSoup(htmlfile,"html.parser")
print(soup.prettify())
print("title of the html web page is:- ")
print(soup.title) #returns the first title tag in the document
print("Only text of title is:- ")
print(soup.title.text) #return text of title tag
print("\n")
print(soup.div) #prints first div that it finds

print(soup.find("div",class_="school")) #finds the div with class ="school"
print(soup.find(class_="city")) #finds the element with class ="city"  #as class is a special keyword in python
                                #hence class_ is used to differentiate from the normal class keyword
print(soup.find(id="program")) #finds the element with id="program"

print("\n\n")

name=soup.find(class_="name") #find according to tag,class_,id but find only one or 1st tag
print(name)

print("\n\n")

textname=name.h1.a.text
print(textname)

print("\n\n")

name1=name.p.text
print(name1)

#find multiple tags that match the description
divlist=soup.find_all('div')
print(divlist)

for h1 in soup.find_all('div'):
    print(h1.h1.text)



