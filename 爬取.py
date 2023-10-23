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


###爬虫只是一种技术或工具，人们可以利用它去做有用的事，也能利用它去搞破坏。
1、恶意消耗别人的服务器资源，是一件不道德的事，恶意爬取一些不被允许的数据，还可能会引起严重的法律后果。
2、工具在你手中，如何利用它是你的选择。当你在爬取网站数据的时候，别忘了先看看网站的Robots协议是否允许你去爬取。
3、同时，限制好爬虫的速度，对提供数据的服务器心存感谢，避免给它造成太大压力，维持良好的互联网秩序，也是我们该做的事。
————————————————

