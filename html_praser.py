import requests
from bs4 import BeautifulSoup
from googletrans import Translator

html = requests.get('http://www.varzishtv.tj/tj/')

bs = BeautifulSoup(html.text, 'lxml')

#find all programs list
all_programs_list = bs.div.find_all('div' , attrs={'class' : 'tv-prog pb-md'})

#dictionary consist of all programs schedule
all_programs_dict = {}

#list of program of one day
programs_of_a_day = []

for program in all_programs_list:
        if ('Футбол' in program.get_text()) or ('LIVE' in program.get_text()):
            
            games_prog = program.get_text().replace("\n", " ").rstrip()
            
            programs_of_a_day.append(games_prog)

            #add all LIVE or football program to dictionary
            all_programs_dict[program.parent.h4.get_text()] = programs_of_a_day

print(all_programs_dict)
translated_all_programs_dict = {}
translated_all_programs_list = []

for date in all_programs_dict.keys():
    translated_date = Translator().translate(str(date)).text
    print(translated_date)

    for item in all_programs_dict[date]:
        translated_item = Translator().translate(item).text
        print(translated_item)
        translated_all_programs_list.append(translated_item)
        translated_all_programs_dict[translated_date] = translated_all_programs_list

print(translated_all_programs_dict)