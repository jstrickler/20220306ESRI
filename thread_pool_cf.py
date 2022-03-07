import time
import concurrent.futures
import requests

URLS = ['https://www.python.org/',
        'https://www.cnn.com/',
        'https://europe.wsj.com/',
        'https://www.google.com/',
        'http://www.cja-tech.com/',
        'https://www.bbc.co.uk/',
        'https://www.msnbc.com/',
        'https://www.nasa.gov/',
        'https://www.esri.com/',
        'https://www.imdb.com/',
        'https://www.xkcd.com/',
        'https://www.johnstrickler.com/']

def main():
    serial_time = get_time(get_urls_serial)
    print(f"serial function took {serial_time:.1f} seconds\n")
    concurrent_time = get_time(get_urls_concurrent)
    print(f"concurrent function took {concurrent_time:.1f} seconds\n")

def get_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def load_url_data(url, timeout):
    """
    Retrieve contents of one URL.
    """
    with requests.get(url, timeout=timeout) as response:
        if response.status_code != requests.codes.OK:
            raise Exception("Unable to reach URL")
        return response.text

def get_urls_serial():
    """
    Retrieve data from URLs one at a time
    """
    print("** SERIAL **")
    for url in URLS:
        try:
            data = load_url_data(url, 60)
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
        else:
            print(f'{url} page is {len(data)} bytes')

def get_urls_concurrent():
    """
    Retrieve data from URLs concurrently
    """
    print("** CONCURRENT **")
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url_data, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{url} generated an exception: {exc}')
            else:
                print(f'{url} page is {len(data)} bytes')


if __name__ == '__main__':
    main()
