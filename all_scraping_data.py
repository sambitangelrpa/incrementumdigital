from client import RestClient
from serpapi import GoogleSearch
import time

def DataForSeo(keyword,region):
    
    # You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
    client = RestClient("sambitbehera2016@gmail.com", "f6d7619675cf7139")


    post_data = dict()
    # simple way to set a task
    post_data[len(post_data)] = dict(
        location_name=region,
        keywords=[keyword]


    )
    # POST /v3/keywords_data/google_ads/search_volume/live
    # the full list of possible parameters is available in documentation
    response = client.post("/v3/keywords_data/google_ads/search_volume/live", post_data)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        #print(response)
        dataforseo_result=response
        return dataforseo_result
        # do something with result
    else:
        #print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))



def serpapi(keyword,region):
    params = {
        "q": keyword,
        "location": region,
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key":'0d5970797e0ee1514a46e562e4d302bb86d9f922e199958f9cbaa8fbc2ed1f10'
          }
    search = GoogleSearch(params)
    results = search.get_dict()
#     li_organic=[]
#     for res1,res2 in zip(results["organic_results"],results["shopping_results"]):
#         tech_dict = {}
#         tech_dict['Position'] = res1['position']
#         tech_dict['Title'] = res1['title']
#         tech_dict['Link'] = res1['link']
#         tech_dict['Position_Shopping'] = res2['position']
#         tech_dict['Title_Shopping'] = res2['title']
#         tech_dict['Link_Shopping'] = res2['link']
#         li_organic.append(tech_dict)
        
    return results
    
    
    

def main_output(keyword,region):
    dataforseo_result=DataForSeo(keyword,region)
    serpapi_results=serpapi(keyword,region)
    
    time.sleep(2)
    # if 'shopping_results' not in serpapi_results.keys():
    #     statistic_information=dataforseo_result['tasks'][0]['result'][0]
    #     organic_results=serpapi_results['organic_results']
    #     # shopping_results=serpapi_results['shopping_results']

    #     output_dict={keyword:{'scraping_result':{'organic_results':organic_results},'statistic_information':statistic_information}}
    
    #     return output_dict

    
    statistic_information=dataforseo_result['tasks'][0]['result'][0]
    organic_results=serpapi_results['organic_results']
    shopping_results=serpapi_results['shopping_results']
    
    output_dict={keyword:{'scraping_result':{'organic_results':organic_results,'shopping_results':shopping_results},'statistic_information':statistic_information}}
    
    return output_dict
    

