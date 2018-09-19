#!/user/bin/env python3

import requests
from bs4 import BeautifulSoup

'translate a given list to text by Google translator'
def translate_list(my_list):
    from googletrans import Translator
    
    'translate list to Google translator object'
    translated_my_list = Translator().translate(my_list)
    'convert tranlation object to english text'
    for i in range(len(translated_my_list)):
        translated_my_list[i] = translated_my_list[i].text
    return translated_my_list

def get_html():
    try:
        html = requests.get('http://www.varzishtv.tj/')
    except ConnectionError :
        print('''Occured "Conecction Error"\nBe relax cause I'm here at service of you ;)''')
        get_html()

    bs = BeautifulSoup(html.text, 'lxml')

    'find all programs list'
    all_programs_list = bs.find_all(name='div', attrs='tv-prog pb-md')
    #print(all_programs_list)

    dates_list = []
    text_all_program_list = [] 

    dup_dates_list = []
    for program in all_programs_list:

        'get text of all programs'
        text_all_program_list.append(program.get_text().replace("\n", " "))

        'get text of programs of one day'
        dates = program.parent.h4.get_text()
        
        'add date to date list'
        if dates not in dates_list:
            dates_list.append(dates)
        dup_dates_list.append(dates)

    'traslate date list'
    translated_date_list = translate_list(dates_list)

    'traslate text all program list'
    translated_text_all_program_list = translate_list(text_all_program_list)

    'schedule dict consist of dates and programs'
    all_programs_dict = {}
    n = 0
    for i in range(len(dates_list)):
        m = dup_dates_list.count(dates_list[i])
        all_programs_dict[translated_date_list[i]] = translated_text_all_program_list[n:m+n]
        n += m

    for date in all_programs_dict.keys():
        print(date)

        for program in all_programs_dict[date]:
            print(program)
        print()

if __name__ == "__main__":
    get_html()
