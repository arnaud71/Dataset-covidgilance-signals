################################
#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# query google with a list of covid signals and
# obtain a list of serp in csv file format
#
# we used proxy service to query from US (no needed from CH)
################################
import pprint
import serpscrap

# 4 query input datasets for the google search
# please uncomment the one you want to use


# query dataset in english with signals (symptoms) + covid and cornavirus keywords
"""
keywords = [
    'fever covid',
    'chest pain covid',
    'cough covid',
    'coughing covid',
    'soreness covid',
    'thermometer covid',
    'sore throat covid',
    'throat pain covid',
    'shortness of breath covid',
    'dsypnea covid',
    'difficulty breathing covid',
    'diarrhea covid',
    'diarrea covid',
    'anosmia covid',
    'loss smell covid',
    'ageusia covid',
    'loss taste covid',
    'rhinorrhea covid',
    'runny nose covid',
    'running nose covid',
    'fever coronavirus',
    'chest pain coronavirus',
    'cough coronavirus',
    'coughing coronavirus',
    'soreness coronavirus',
    'thermometer coronavirus',
    'sore throat coronavirus',
    'throat pain coronavirus',
    'shortness of breath coronavirus',
    'dsypnea coronavirus',
    'difficulty breathing coronavirus',
    'diarrhea coronavirus',
    'diarrea coronavirus',
    'anosmia coronavirus',
    'loss smell coronavirus',
    'ageusia coronavirus',
    'loss taste coronavirus',
    'rhinorrhea coronavirus',
    'runny nose coronavirus',
    'running nose coronavirus'
]
"""

# query dataset in english with only signals (symptoms) s
"""
keywords = [
    'fever',
    'chest pain',
    'cough',
    'coughing',
    'soreness',
    'thermometer',
    'sore throat',
    'throat pain',
    'shortness of breath',
    'dsypnea',
    'difficulty breathing',
    'diarrhea',
    'diarrea',
    'anosmia',
    'loss smell',
    'ageusia',
    'loss taste',
    'rhinorrhea',
    'runny nose',
    'running nose'
]
"""
# query dataset in french with only signals (symptoms)
"""
keywords = [
    'fièvre',
    'douleur thoracique',
    'douleur thorax',
    'oppression thoracique',
    'mal thoracique',
    'toux',
    'tousse',
    'tousser',
    'courbature',
    'thermomètre',
    'mal de gorge',
    'maux de gorge',
    'dyspnée',
    'essouflement',
    'gene respiratoire',
    'gêne respiratoire',
    'mal à respirer',
    'diarrhée',
    'chiasse',
    'perte odorat',
    'anosmie',
    'perte de gout',
    'perte de goût',
    'agueusie',
    'rhinorrhée',
    'nez qui coule',
    'écoulement nasale',
    'éruption cutanée'
]
"""


# query dataset in french with signals (symptoms) + covid and cornavirus keywords

"""
keywords = [
    'fièvre covid',
    'douleur thoracique covid',
    'douleur thorax covid',
    'oppression thoracique covid',
    'mal thoracique covid',
    'toux covid',
    'tousse covid',
    'tousser covid',
    'courbature covid',
    'thermomètre covid',
    'mal de gorge covid',
    'maux de gorge covid',
    'dyspnée covid',
    'essouflement covid',
    'gene respiratoire covid',
    'gêne respiratoire covid',
    'mal à respirer covid',
    'diarrhée covid',
    'chiasse covid',
    'perte odorat covid',
    'anosmie covid',
    'perte de gout covid',
    'perte de goût covid',
    'agueusie covid',
    'rhinorrhée covid',
    'nez qui coule covid',
    'écoulement nasale covid',
    'éruption cutanée covid',
    'fièvre coronavirus',
    'douleur thoracique coronavirus',
    'douleur thorax coronavirus',
    'oppression thoracique coronavirus',
    'mal thoracique coronavirus',
    'toux coronavirus',
    'tousse coronavirus',
    'tousser coronavirus',
    'courbature coronavirus',
    'thermomètre coronavirus',
    'mal de gorge coronavirus',
    'maux de gorge coronavirus',
    'dyspnée coronavirus',
    'essouflement coronavirus',
    'gene respiratoire coronavirus',
    'gêne respiratoire coronavirus',
    'mal à respirer coronavirus',
    'diarrhée coronavirus',
    'chiasse coronavirus',
    'perte odorat coronavirus',
    'anosmie coronavirus',
    'perte de gout coronavirus',
    'perte de goût coronavirus',
    'agueusie coronavirus',
    'rhinorrhée coronavirus',
    'nez qui coule coronavirus',
    'écoulement nasale coronavirus',
    'éruption cutanée coronavirus'
]
"""

#configuration of the serpscraper
config = serpscrap.Config()
config_new = {
   'scrape_urls': False, #only serp is usefull here
   'cachedir': '/tmp/.serpscrap/', # keep cache
   'clean_cache_after': 24, # cache for 24 hours
   'database_name': '/tmp/serpscrap',
   'do_caching': True,
   'num_pages_for_keyword': 1, # one page of SERP
   'num_results_per_page': 20, # with 20 results
   'search_engines': ['google'], # on google
   # uncomment the google search you want to use ch or us (so depending of the data set)
#   'google_search_url': 'https://www.google.ch/search?hl=fr&',
   'google_search_url': 'https://www.google.com/search?hl=en&',
   'executable_path': '/usr/local/bin/chromedriver' # path to the chromedriver (could cause issues)
}

#init the config
config.apply(config_new)

#init the serpscraper
scrap = serpscrap.SerpScrap()
#run the serpscraper with list of queries
scrap.init(config=config.get(), keywords=keywords)
#uncomment the output csv file you want to have
scrap.as_csv('serp_signals_20_en')
#scrap.as_csv('serp_signals_20_ch_fr')
#scrap.as_csv('serp_signals_covid_20_en')
#scrap.as_csv('serp_signals_covid_20_ch_fr')
