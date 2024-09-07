import requests
from requests import Response, RequestException

def check_status(url: str) -> None:
    try:
        response = requests.get(url)

        #info
        status_code = response.status_code
        headers = response.headers
        content_type = headers.get('Content-Type', 'Unkown')
        server = headers.get('Server', 'Unkown')
        response_time = response.elapsed.total_seconds()
        
        #print info
        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')

    except RequestException as e:
        print(f'Error: {e}')

def main() -> None:
    url_to_check = 'https://www.wikipedia.org'
    check_status(url_to_check)

if __name__ == "__main__":
    main()