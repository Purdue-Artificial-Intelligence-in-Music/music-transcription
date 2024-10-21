import requests
import os
from git import Repo
from run_project import queue_project

def get_repo_links():
    res = requests.request(method="get", url="https://script.google.com/macros/s/AKfycbzZPlrQeFyhngnc5faAyS-GUmzxFDCGSwIm29KLZaIDHZeMr4YDGO9I79WGPGkxUWhC/exec")
    json = res.json()
    return json["values"]

def main():
    links_ids = get_repo_links
    
    prev_job = ""
    
    for (link, id) in links_ids:
        if os.path.exists(f'./{id}'):
            print(f"Pulling from origin on ./{id}")
            repo = Repo(f'./{id}')
            repo.remote("origin").pull()
        else:
            print(f"Cloning: {link} to ./{id}")
            Repo.clone_from(link, f'./{id}')
            
        print("Running Project: " + id)
        queue_project(f'./{id}', dependency=prev_job)
        
if __name__ == "__main__":
    main()