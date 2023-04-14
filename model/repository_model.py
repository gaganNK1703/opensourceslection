import mysql.connector
import requests
import json

api_key = '24e2ede14665b0c6c80b86ad839e7f8c'
class repository_model():
    #constructor
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="root12345",database="opensource")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection successful")
        except:
            print("Connection failed")
    def repository_search(self,data):
        platform=data["platform"]
        keyword=data["keyword"]
        licenses=data["licenses"]
        sort=data["sort"]
        order=data["order"]
        keyword=keyword.split(',')
        licenses=licenses.split(',')
  

        response = requests.get('https://libraries.io/api/search', params={'api_key': api_key, 'platform': platform, 'q':keyword,'licenses':licenses,'sort':sort,'order':order})
        # response = requests.get('https://libraries.io/api/search', params={'api_key': api_key, 'platform': 'npm', 'q':['FasterXML jackson','jackson-annotations'],'licenses':['MIT','Apache-2.0'],'sort':'stars','order':'desc'})
        
        search_result=json.loads(response.text)

        for repo in search_result[:10]:
                # print(repo['name'],"->",repo['description'],"->",repo['homepage'],'->',repo['latest_release_number'],'->',repo['repository_license'])
                name=repo['name']
                description=repo['description']
                dependencies_count=int(repo['dependents_count'])
                stars=int(repo['stars'])
                forks=int(repo['forks'])
                language=repo['language']
                latest_download_url=repo['latest_download_url']
                repository_url=repo['repository_url']
                latest_stable_release_published_at=repo["latest_stable_release_published_at"]
                latest_stable_release_number=repo['latest_stable_release_number']
                self.cur.execute(f"INSERT INTO repository ( name, description, dependencies_count, stars, forks, language, latest_download_url, latest_stable_release_number, repository_url, latest_stable_release_published_at) VALUES ( '{name}', '{description}', '{dependencies_count}', '{stars}', '{forks}', '{language}', '{latest_download_url}', '{latest_stable_release_number}', '{repository_url}', '{latest_stable_release_published_at}')")
                print("inserted")

                
                
        return "hello"

        

