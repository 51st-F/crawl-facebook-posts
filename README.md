# Crawl-facebook-posts

Crawl facebook groups posts.

## Getting Started

Clone repo from Github and active selenium grid server.
```
git clone https://github.com/51st-F/crawl-facebook-posts.git &&
cd crawl-facebook-posts &&
docker-compose -f docker-compose-standalone-chrome.yml up -d
```

Active crawler
```
docker-compose -f docker-compose-crawler.yml up -d
```


### Prerequisites

* [Docker-desktop](https://www.docker.com/products/docker-desktop/)

## Authors

* [Ivan Wu](https://github.com/51st-F) - *Initial work* 
## Acknowledgments

* Those articles I search from Google
* Those videos I search from Youtube
* etc
