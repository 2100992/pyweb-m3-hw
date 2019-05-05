# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_head(title):
    head = f'''<head>
        <meta charset = "utf-8">
        <title>{title}</title>
        <head>'''
    return head

def generate_body(header, paragraphs, footer):
    body = f'<h1>{header}</h1>'
    for i in paragraphs:
        body = f'''{body}
        <p>{i}</p>'''
    return f'''<body>
        {body}
        {footer}
        </body>'''

def generate_page(head, body):
    page = f'''<html>
        {head}
        {body}
        </html>'''
    return page

def generate_footer(link, description):
    footer = f'''<hr/>
        <a href="{link}">
            {description}
        </a>'''
    return footer

def save_page(title, header, paragraphs, footer, output = 'index.html'):
    fp = open(output, 'w', encoding='utf8')
    #today = dt.now().date()
    page =  generate_page(
        head = generate_head(title),
        body = generate_body(header = header, paragraphs = paragraphs, footer = footer)
        )
    print(page, file = fp)
    fp.close()

def main():
    today = dt.now().date()
    save_page(
        title = 'Гороскоп на сегодня',
        header = 'Что день ' + str(today) + ' готовит',
        paragraphs = generate_prophecies(total_num=3, num_sentences=4),
        footer = generate_footer('about.html', 'О реализации'),
    )

main()