from bs4 import BeautifulSoup
from rich import print
from rich.console import Console
console = Console()
import time
import requests
def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35").text
    soup = BeautifulSoup(html_text,"lxml")
    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    console.print("Enter some skill you are not familiar with",style="magenta")
    unknown_skill = input('>')
    print("Filtering.......")
    print(" ")
    for job in jobs:
        posted_date = job.find('span',class_="sim-posted").text.replace(' ','')
        if "today" in posted_date:
            company_name = job.find('h3',class_="joblist-comp-name").text
            skills = job.find('span',class_ = "srp-skills").text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unknown_skill not in skills:
                console.print(f"Company Name: {company_name.strip()}",style="yellow")
                print("  ")
                console.print(f"Skills: {skills.strip()}",style="green")
                print("   ")
                print(f"More Information: {more_info}")
                print("   ")
                console.print(">>>>>>>>>>",style="red")
                console.print(">>>>>>>>>>Next Application<<<<<<<<<<<",style="green")
                console.print(">>>>>>>>>>",style="red")
                print("   ")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting time {time_wait} minutes....")
        time.sleep(time_wait*60)
      
      
