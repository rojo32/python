import scrapy
import csv
import json
import sqlite3

class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["https://cve.mitre.org"]
    start_urls = ["https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        conexion=sqlite3.connect('vuln.db')
        tabla='CREATE TABLE vulns(exploit TEXT, cve TEXT)'
        cursor= conexion.cursor()
        cursor.execute(tabla)
        conexion.commit()
        
        for child in response.xpath('//table'):
            if len(child.xpath('tr'))>100:
                table=child
                break
        
        count=0
        #data={}
        #csv_file=open('vulnerabilidades.csv','w')
        #json_file=open('vulnerabilidades.json','w')
        #write=csv.writer(csv_file)
        #dividmos el archivo en dos columnas
        #write.writerow(['exploit id','cve id'])
              
            
            
        for row in table.xpath('//tr'):
            try:
                exploit_id =row.xpath('td//text()')[0].extract()
                cve_id=row.xpath('td//text()')[2].extract()
                #write.writerow([exploit_id,cve_id])
                #data[exploit_id]=cve_id
                cursor.execute('INSERT INTO vulns (exploit, cve) VALUES(?,?)',(exploit_id,cve_id))
                conexion.commit()
                
                count+=1                
                
            except IndexError:
                pass
        
        #csv_file.close()
        #json.dump(data,json_file)
        #json_file.close()
            
