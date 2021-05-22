# valStatus/Region.py
"""
MIT License

Copyright (c) 2020 - 2021 D3crypt360 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
import http.client

class Region:
    def __init__(self, region):
        self.region = region
        
    def request(self):
        conn = http.client.HTTPSConnection("valorant.secure.dyn.riotcdn.net")
        conn.request("GET", f"/channels/public/x/status/{self.region.casefold()}.json")
        r = conn.getresponse()
        json_data = json.loads(r.read())
        if r.status == 200:
            return json_data
        else:
            return
   
    def get_status(self):
        status = self.request()
        return {
                'issue':status['incidents'] or status['maintenances'],
                'incidents':status['incidents'],
                'maintenances':status['maintenances']
               }
    
    def get_status_issue(self):
        if self.get_status()['issue'] != []:
            return True
        else:
            return False
                
    def incident_title(self):
        try:
            return self.get_status()["incidents"][0]['titles'][0]['content']
        except IndexError:
            return
        
    def incident_date(self):
        try:
            return self.get_status()['incidents'][0]['updates'][0]['created_at'][:10]
        except IndexError:
            return
        
    def incident_reason(self):
        try:
            return self.get_status()['incidents'][0]['updates'][0]['translations'][0]['content']
        except IndexError:
            return
        
    def maintenance_title(self):
        try:
            return self.get_status()["maintenances"][0]['titles'][0]['content']
        except IndexError:
            return
        
    def maintenance_date(self):
        try:
            return self.get_status()['maintenances'][0]['updates'][0]['created_at'][:10]
        except IndexError:
            return
        
    def maintenance_reason(self):
        try:
            return self.get_status()['maintenances'][0]['updates'][0]['translations'][0]['content']
        except IndexError:
            return
        
    def maintenence_check(self):
        if self.get_status()['maintenances'] != []:
            return True
        else:
            return False
        
    def incident_check(self):
        if self.get_status()['incidents'] != []:
            return True
        else:
            return False
