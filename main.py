from bs4 import BeautifulSoup
import requests
import os
import shutil

shutil.rmtree('posts')


print("skill which you are not familiar")

unfamiliar_skill = input('>')

html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')

os.mkdir("/Users/arbaj/PycharmProjects/BSLinkdineScrapper/posts")
def find_jobs():
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"company name :{company_name.strip()} \n")
                    f.write(f"required_skills :{skills.strip()} \n")
                    f.write(f"more_info :{more_info} \n")

                print(f'file saved:{index}')


if __name__ == '__main__':
    find_jobs()
