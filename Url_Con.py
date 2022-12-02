import requests
from bs4 import BeautifulSoup



def getUrlPage():
    URL = "https://realpython.github.io/fake-jobs"
    page = requests.get(URL)
    return page

def getUrlContent():
    soup = BeautifulSoup(getUrlPage().content, "html.parser")
    results = soup.find(id="ResultsContainer")
    return results

def getDivs():
    job_elements=getUrlContent().find_all("div",class_="card-content")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

def getPythonJobs():
    python_jobs=getUrlContent().find_all("h2",string=lambda text:"python" in text.lower())

    for python_job in python_jobs:
        # title_element = python_job.find("h2", class_="title is-5")
        print(python_job.text.strip())
