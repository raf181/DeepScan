import pandas as pd
from elasticsearch import Elasticsearch

def fetch_logs():
    es = Elasticsearch(['http://localhost:9200'])
    query = {"query": {"match_all": {}}}
    result = es.search(index="server-logs-*", body=query, size=1000)
    
    # Convert Elasticsearch data to DataFrame
    log_data = pd.json_normalize([hit['_source'] for hit in result['hits']['hits']])
    log_data['timestamp'] = pd.to_datetime(log_data['timestamp'])
    log_data.fillna("", inplace=True)
    return log_data

if __name__ == "__main__":
    logs = fetch_logs()
    print(logs.head())
