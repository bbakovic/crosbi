from bs4 import BeautifulSoup
import csv, urllib2, codecs, re, operator
broj_krivih=0
zapis=codecs.open("cro1.txt",'w','utf-8')
for a in range(99,150):

    try:
        response = urllib2.urlopen("http://beta.bib.irb.hr/"+str(a))
        soup = BeautifulSoup(response,"lxml")
        try:
            bib = soup.find_all('div', class_='container')
            bib2=bib[2].find_all('p', class_='item-label')
            zapis.write("BibID \t" + str(a) + '\n')
            for x in bib2:
                #print x,"++++++"
                #print type(x)
                tag=x.find('strong')
                text=re.findall("br/>(.+?)</p", str(x).replace('\n',''))

                zapis.write(str(tag).lstrip("<strong>").rstrip("</strong>")+'\t'+str(text[0]).strip()+'\n')
            zapis.write("\nnew_DB_entry\n")
                #print str(tag).lstrip("<strong>").rstrip("</strong>"), text[0]
        except AttributeError:
            broj_krivih += 1
    except urllib2.HTTPError, error:
        contents = error.read()
    print a

