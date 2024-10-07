from math import ceil

import requests
from bs4 import BeautifulSoup
from ..models import Headline

URL = "https://news.ycombinator.com/?p={page}"
ITEMS_PER_PAGE = 30


def _clean_only_numbers(title_no: str):
    return int(''.join(filter(str.isdigit, title_no)))


def _clean_comments(comment):
    no_comments = ''.join(filter(str.isdigit, comment))
    if no_comments:
        return int(no_comments)
    return 0


def handle(response):
    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")
        trs = soup.find_all('tr', class_='athing')
        entries = [tr['id'] for tr in trs]
        headlines = []
        for entry in entries:
            title_no = soup.select(f'tr[id="{entry}"] > td > span')
            td_title_no = BeautifulSoup(repr(title_no[0]), "html.parser")
            title = soup.select(f'tr[id="{entry}"] span.titleline a:nth-of-type(1)')
            tr_title = BeautifulSoup(repr(title[0]), "html.parser")
            points = soup.find('span', id=f'score_{entry}')
            comment = soup.select(f'tr[id="{entry}"] + tr > td > span > a')
            a_comment_last = comment[-1] if len(comment) >= 3 else None
            a_comment = BeautifulSoup(repr(a_comment_last), "html.parser")
            print(f"{entry} {_clean_only_numbers(td_title_no.string)} "
                  f"{tr_title.string} "
                  f"{_clean_only_numbers(points.string) if points else 0} "
                  f"{_clean_comments(a_comment.string) if a_comment else 0}")
            position = _clean_only_numbers(td_title_no.string)
            points = _clean_only_numbers(points.string) if points else 0
            comments = _clean_comments(a_comment.string) if a_comment else 0
            headline = Headline(
                news_id=entry, position=position, title=tr_title.string,
                points=points, comments=comments
            )
            headlines.append(headline)
        Headline.objects.bulk_create(
            headlines,
            update_conflicts=True,
            update_fields=['title', 'position', 'points', 'comments', 'updated_date'],
            unique_fields=['news_id'],
            batch_size=30,
        )
    else:
        print("Error fetching the page. Status code:", response.status_code)


def run(*args):
    """
    Process to load Hacker News (news.ycombinator.com) headlines to DB
    :param args: pages (int)
    :return: None
    """
    pages_arg = int(args[0]) if args and args[0].isdigit() else ITEMS_PER_PAGE
    pages = pages_arg if pages_arg >= 1 else 1
    for index in range(pages):
        url = URL.format(page=index + 1)
        print(f'----> PROCESS FOR {url}')
        response = requests.get(url)
        try:
            handle(response)
        except Exception as e:
            print(f"ERROR: \n{e}\n{e.args}")
            continue
    print('PROCESS COMPLETE')
