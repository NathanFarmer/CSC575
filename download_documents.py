from bs4 import BeautifulSoup
import requests
import urllib.request
import io
import os
import zipfile


def download_document(url, file_name):
    resp = urllib.request.urlopen(url + file_name)
    length = resp.getheader('content-length')
    if length:
        length = int(length)
        blocksize = max(4096, length//100)
    else:
        blocksize = 1000000

    buf = io.BytesIO()
    size = 0

    while True:
        buf1 = resp.read(blocksize)
        if not buf1:
            break
        buf.write(buf1)
        size += len(buf1)
        if length:
            prog_str = '{0:.0%}\r'.format(size/length) + 'Download ' + file_name + ' '
            print(prog_str, end='')
    print()

    with open(file_name, 'wb') as out_file:
        out_file.write(buf.getvalue())

def unzip_document(file_name):
    file = dir_name + file_name

    with zipfile.ZipFile(file, 'r') as zip_ref:
        print('Unzip ' + file_name)
        zip_ref.extractall(dir_name)

if __name__ == '__main__':
    # Set working dir to location of this file
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    # Create data folder and change working dir to there
    dir_name = dir_name + '\\data\\'
    os.mkdir('data')
    os.chdir('data')

    # Identify, download, and unzip corpus files
    page = 'https://dmice.ohsu.edu/trec-gen/data/2006/documents/'
    source = requests.get(page).text
    soup = BeautifulSoup(source, 'html.parser')

    print('Downloading and unzipping files:')

    for link in soup.findAll('a', href=True):
        url = link['href']
        if url.endswith('.zip'):
            download_document(page, url)
            unzip_document(url)
        elif url.endswith('.txt'):
            download_document(page, url)

    # Delete extracted zip files
    list_dir = os.listdir(dir_name)
    for item in list_dir:
        if item.endswith(".zip"):
            os.remove(os.path.join(dir_name, item))
