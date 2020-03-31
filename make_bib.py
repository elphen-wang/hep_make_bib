from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as np
import urllib
import re
import os


print("Please input your keyword...");

keyword=input();
keyword=keyword.replace(' ','+')

#keyword="damping+signature+and+jhep";

print("Your are searching: ",keyword);
html = urlopen("http://old.inspirehep.net/search?ln=zh_CN&p="+keyword+"&of=hb&action_search=%E6%90%9C%E5%AF%BB&sf=earliestdate&so=d");
bsObj = BeautifulSoup(html, "lxml")
#print(bsObj)

record_body=bsObj.findAll("div", {"class":{"record_body"}});


#title_linklist=bsObj.findAll("a", {"class":{"titlelink"}})
#latex_us_linklist= bsObj.findAll("ul", {"class":{"tight_list"}})
#doi_linklist=bsObj.findAll("div", {"class":{"record_body"}})

#resultsnum= bsObj.find("td", {"class":{"searchresultsboxheader"},"align":{"center"}}).findAll("strong")[0];
#you will get a list, here just one element
#resultsnum=int(resultsnum.get_text());


resultsnum=len(record_body);
print("You got ",resultsnum," result(s)");
#print(title_linklist)
#print(latex_us_linklist)
#print(doi_linklist)

for i in range(0,resultsnum):
    
    #title_links.append(title_linklist[i].attrs['href']);
    #latex_us_links.append(latex_us_linklist[i].findAll("a")[2].attrs['href'])
    #title_links.append(record_body[i].findAll("a", {"class":{"titlelink"}})[0].attrs['href'])
    #latex_us_links.append(record_body[i].findAll("ul", {"class":{"tight_list"}})[0].findAll("a")[2].attrs['href'])
    
    #print(record_body[i].findAll("ul", {"class":{"tight_list"}})[0].findAll("a")[2].attrs['href'])
    #following code are for each record
    
    b_elements=record_body[i].findAll("b");
    href_list=record_body[i].findAll("a");
    #i=0;
    title_link="";
    latex_us_links="";
    doi_link="";
    arXiv_abs_link="";
    arXiv_pdf_link="";
    for link in href_list:
        #print(link,"----------------->",i)
        #i=i+1
        if("titlelink" in str(link)):
           title_link=link.attrs['href']
        elif("hlxu" in str(link)):
           latex_us_link=link.attrs['href']
        elif("doi" in str(link)):
           doi_link=link.attrs['href']
        elif("arXiv.org/abs" in str(link)):
           arXiv_abs_link=link.attrs['href']
        elif("arXiv.org/pdf" in str(link)):
           arXiv_pdf_link=link.attrs['href']
           
    #print(title_link,latex_us_link,doi_link,arXiv_abs_link)
    html_son = urlopen(latex_us_link);
    bsObj_son = BeautifulSoup(html_son, "lxml");
    old_latex=str(bsObj_son.find("pre").get_text());
    old_latex_set=old_latex.split("%``");
    cite_str=old_latex_set[0];#cite
    title_str=old_latex_set[1].split(",''")[0];#title
    end_str=old_latex_set[1].split(",''")[1].split(".  %%")[0];#paper(s)
    #print(old_latex)
    #print(title_str)
    #print(cite_str)
    #print(end_str)
    if("doi" in end_str):
       s0=end_str.find("doi");
       s1=0;
       for k in range(s0,len(end_str)):
           if(end_str[k]=="["):
              s1=k;break;
       mid_str=end_str[s0:s1]
       DOI=end_str[:s0]
       ARXIV=end_str[s1:]
       #print(DOI,ARXIV)
       new_latex=cite_str+"{\it{"+title_str+"}},{\color{blue}\href{"+doi_link+"}{"+DOI+"}\href{"+arXiv_abs_link+"}{"+ARXIV+"}[\href{"+title_link+"}{\scriptsize IN\\normalsize SPIRE}]}";
    else:
       new_latex=cite_str+"{\it{"+title_str+"}}, {\color{blue}\href{"+arXiv_abs_link+"}{["+end_str[2:]+"]}[\href{"+title_link+"}{\scriptsize IN\\normalsize SPIRE}]}";
    print("Index. ",i,", ---------->title: ",title_str);
    print(new_latex);
    print("\n");
    
    '''
    old_latex_set=old_latex.split(",");
    cite_str=old_latex_set[0];#cite
    title_str=old_latex_set[1][6:];#title
    arXiv_str=(old_latex_set[2].split("<br/>")[1][:-1]).replace(" ","");#arXiv
    print(cite_str,title_str,arXiv_str)
    '''
    #new
