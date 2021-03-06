from bs4 import BeautifulSoup
import urllib2, codecs, re, time
broj_krivih = 0


zapis = codecs.open("cro18.txt", 'w', 'utf-8')
for a in range(850001 , 900001):
    try:
        response = urllib2.urlopen("http://beta.bib.irb.hr/"+str(a))
        soup = BeautifulSoup(response, "lxml")
        try:
            bib = soup.find_all('div', class_='container')
            bib2 = bib[2].find_all('p', class_='item-label')
            zapis.write("BibID \t" + str(a) + '\n')
            for x in bib2:
                tag = x.find('strong')
                tag_f=str(tag).lstrip("<strong>").rstrip("</strong>")
                text = re.findall("br/>(.+?)</p", str(x).replace('\n', ''))
                if len(text) > 0:
                    text_f=str(text[0]).strip()
                    zapis.write(tag_f+'\t'+text_f+'\n')
            zapis.write("new_DB_entry\n")
        except AttributeError:
            broj_krivih += 1
    except urllib2.HTTPError, error:
        contents = error.read()
    if (a % 1000)==0:
        print a, time.strftime('%X %x %Z')