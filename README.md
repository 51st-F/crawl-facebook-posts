# Crawl-Facebook-Posts

Crawl facebook groups posts.

## Getting Started

- Git clone repo 

- Activate selenium grid server

```
$ docker-compose -f docker-compose-standalone-chrome.yml up -d
```

- Crawler can be restarted repeatedly

```
$ docker-compose -f docker-compose-crawler.yml up -d
```

## Linux Tree

- Build some empty file marked * to meet coding conventions required.

```
.
├── demo.csv
├── docker-compose-crawler.yml
├── docker-compose-standalone-chrome.yml
├── * docs
│   ├── * some_document.doc
│   └── * some_manual.pdf
├── README.md
├── requirements.txt
├── src
│   └── selenium-remote-standalone-chrome
│       └── script_1.py
└── * tests
    ├── * test_name_1
    │   ├── * README.md
    │   └── * test_1.py
    └── * test_name_2
        ├── * README.md
        └── * test_1.py
```
