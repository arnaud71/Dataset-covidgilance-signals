# Dataset-covidgilance-signals
Research datasets about top signals for covid 19 (coronavirus) for study into  Google Trends (GT) and with SEO metrics

## Website

The study is currently published on https://covidgilance.org website (in french)

## Datasets description

`covid signals -> |selection| -> 4 dataset -> |serp.py| -> 4 serp datasets -> |aggregate_serp.pl| -> 4 aggregated dataset of serp -> |prepare datasets| -> 4 ranked top seo dataset` 

### Original lists of signals (mainly covid symptoms) - dataset

**Description:** contain the original relevant list of signals for covid19 (here list of queries where you can see, in GT, a relevant signal during the covid 19 period of time)  
**Name:** covid_signal_list.tsv  
    
**List of content:**    
    
**- id:** unique id for the topic  
**- topic-fr:** name of the topic in French  
**- topic-en:** name of the topic in English  
**- topic-id:** GT topic id  
**- keyword fr:** one or several keywords in French for GT  
**- keyword en:** one or several keywords in English for GT  
**- fr-topic-url-12M:** link to 12-months French query topic in GT in France  
**- en-topic-url-12M:** link to 12-months English query topic in GT in US  
**- fr-url-12M:** link to 12-months French queries in GT in France  
**- en-url-12M:** link to 12-months English queries topic in GT in US  
**- fr-topic-url-5M:** link to 5-months French query topic in GT in France  
**- en-topic-url-5M:** link to 5-months English query topic in GT in US  
**- fr-url-5M:** link to 5-months French queries in GT in France   
**- en-url-5M:** link to 5-months English queries topic in GT in US   

### Tool to get SERP of covid signals - tool 

**Description:** query google with a list of covid signals and obtain a list of serps in csv (tsv in fact) file format  
**Name:** serper.py  

`python serper.py`

### SERP files - datasets


**Description** Serp results for 4 datesets of queries
**Names:**
simple version of covid signals from google.ch in French: serp_signals_20_ch_fr.csv  
simple version of covid signals from google.com in English: serp_signals_20_en.csv  
amplified version of covid signals from google.ch in French: serp_signals_covid_20_ch_fr.csv  
amplified version of covid signals from google.com in English: serp_signals_covid_20_en.csv  

amplified version means that for each query we create two queries one with the keywords "covid" and one with "coronavirus"

### Tool to aggregate SERP results - tool

**Description:** load csv serp data and aggregate the data to create a new csv file where each line is a website and each column is a query.
**Name:**   aggregate_serp.pl

`perl aggregate_serp.pl> aggregated_signals_20_en.csv


### datasets of top website from the SERP results - dataset

**Description** a aggregated version of the SERP where each line is a website and each column a query  
**Names:**  
aggregated_signals_20_ch_fr.csv  
aggregated_signals_20_en.csv  
aggregated_signals_covid_20_ch_fr.csv  
aggregated_signals_covid_20_en.csv  

**List of content:** 

**- domain:** domain name of the website  
**- signal 1:** Position of the query 1 (signal 1) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- signal ...:** Position of the query (signal) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- signal n:** Position of the query n (signal n) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- total:** average position (total of all position /divided by the number of queries)  
**- missing:** Total number of missing results in the SERP for this website  


### datasets ranked top seo - dataset

**Description** a ranked (by weighted average position) version of the aggregated version of the SERP where each line is a website and each column a query.
TOP 20 have more information about the type and HONcode validity (from the date of collect: September 2020) 

**Names:**  
ranked_signals_20_ch_fr.csv  
ranked_signals_20_en.csv   
ranked_signals_covid_20_ch_fr.csv   
ranked_signals_covid_20_en.csv   

**List of content:** 

**- domain:** domain name of the website  
**- signal 1:** Position of the query 1 (signal 1) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- signal ...:** Position of the query (signal) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- signal n:** Position of the query n (signal n) in the SERP where 30 indicates arbitrary that this website is not present in the SERP  
**- avg position:**	average position (total of all position /divided by the number of queries)  
**- nb missing:** Total number of missing results in the SERP for this website  
**- % presence:** % of presence  
**- weighted avg postion:** combination of avg position and % of presence for final ranking  
**- honcode:** status of the Honcode certificate for this website (none/valid/expired)  
**- type:** type of the website (health, gov, edu or media)  






