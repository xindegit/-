import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = f"https://www.cnblogs.com/AggSite/AggSitePostList"
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
    'Content-Type': 'application/json; charset=UTF-8'
}
datas = []
for page in range(1, 201):
    print(f"正在爬取，{page}页")
    data = {
        'CategoryId': 808,
        'CategoryType': "SiteHome",
        'ItemListActionName': "AggSitePostList",
        'PageIndex': page,
        'ParentCategoryId': 0,
        'TotalPostCount': 4000,
    }
    r = requests.post(url, json.dumps(data), headers=head)

    # print(r.status_code)

    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    sections = soup.findAll('section', {'class': 'post-item-body'})
    for section in sections:
        # print(section)
        titles = section.find('a', {'class': 'post-item-title'})
        title = titles.string
        href = titles['href']
        authors = section.find('a', {'class': 'post-item-author'})
        author = authors.string
        icon_digg = 0
        icon_comment = 0
        icon_views = 0
        for a in section.findAll('a'):
            if 'icon_digg' in str(a):
                icon_digg = a.find('span').string
            if 'icon_comment' in str(a):
                icon_comment = a.find('span').string
            if 'icon_views' in str(a):
                icon_views = a.find('span').string

        datas.append([title, href, author, icon_digg, icon_comment, icon_views])

# print(datas)
df = pd.DataFrame(datas)
df.to_csv('博客园200页热点文章.csv', index=False, header=False)
