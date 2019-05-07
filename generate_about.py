import horoscope
from generate_index import save_page, generate_footer

topics_list = ['Времена дня:', 'Глаголы', 'События:']
events_list = [horoscope.times, horoscope.advices, horoscope.promises]
description = 'Генератор гороскопов на основе случайных комбинаций из следующих списков:'
img_linc = '<img width="100" alt="Знаки зодиака" src="zodiac.jpg"></img>'

def generate_paragraphs():
    paragraph = []
    p = '''
        <ol>'''
    for i in range(3):
        p = f'''{p}
        <li>
            {topics_list[i]}
        </li>
        <ul>''' 
        for j in events_list[i]:
            p = f'''{p}
            <li>
            {j}
            </li>'''
        p = f'''{p}
        </ul>'''
    p = f'''{p}
    </ol>'''
    paragraph.append(p) 
    return paragraph

def main():
    paragraphs = [img_linc, description]
    paragraphs.append(generate_paragraphs()[0])
    save_page(
        title = 'О чем всё это',
        header = 'О чем всё это',
        paragraphs = paragraphs,
        footer = generate_footer('index.html', 'На главную'),
        output = 'about.html'
    )

main()