from typing import Self
from flask import request
import scrapy
import json

class NtschoolsSpider(scrapy.Spider):
    name = "ntschools"
    start_urls = ["https://directory.ntschools.net/#/schools"]

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Host": "directory.ntschools.net",
        "Pragma": "no-cache",
        "Referer": "https://directory.ntschools.net/",
        "Sec-CH-UA": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "Fetch"
    }

    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'
        yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)
        
    def parse_api(self, response):
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw_data = response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school['itSchoolCode']
            school_url = base_url + school_code
            yield scrapy.Request(school_url, callback=self.parse_school, headers=self.headers)
    
    def parse_school(self, response):
        if response.status == 200:
            try:
                raw_data = response.body
                data = json.loads(raw_data)
                yield {
                    "schoolName": data.get('name'),
                    "Physical address": data['physicalAddress'].get('displayAddress') if data.get('physicalAddress') else None,
                    "Postal address": data['postalAddress'].get('displayAddress') if data.get('postalAddress') else None,
                    "Email": data.get('mail'),
                    "Phone Number": data.get('telephoneNumber'),
                    "Principal": data.get('principal'),
                    "Website": data.get('website')
                }
            except json.JSONDecodeError:
                self.logger.error(f"Failed to decode JSON for: {response.url}")
        else:
            self.logger.error(f"Failed to fetch data for: {response.url} with status {response.status}")

#RUN THIS COMMANDS IN THE TERMINAL FOR GET DATA
            #scrapy runspider ntschools.py
            #scrapy runspider flips.py -o ntschools.csv