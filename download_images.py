# Google Images Downloader
# Search and download images from Google Images.
# Install: pip install simple_image_download
# Input keywords and number of images to download
from simple_image_download import simple_image_download as simp
import unittest

# Create a response object
response = simp.Downloader

# keywords = ['cat', 'dog', 'car', 'flower', 'fruit', 'animal']
keywords = ['dog']

# Pull 100 images for each keyword
for kw in keywords:
    response().download(kw, 100)

# Or for URL scraping:
# Pull URLs of images for each keyword, with LIMIT
# response.search_urls('bear supermario', limit=15)
# for url in response.cache:
#     print(url)
