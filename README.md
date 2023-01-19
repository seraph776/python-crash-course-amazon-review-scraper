<div id="top" align="center">

# Python Crash Course, 2nd Edition 
## Amazon Customer Review Scraper  

![made-with-Python](https://img.shields.io/badge/Python-blue?&logo=python&logoColor=yellow&label=Built%20with&style=flat&labelColor=black)
[![GitHub](https://img.shields.io/github/license/seraph776/seraph776?color=green&style=flat&labelColor=black&label=License)](https://github.com/seraph776/python-crash-course-amazon-review-scraper/blob/main/LICENSE)
[![Contribute](https://img.shields.io/badge/Contribute-black?&logo=github&logoColor=black&label=&flat&labelColor=yellow)](https://github.com/seraph776/webscrape_template/blob/main/CONTRIBUTING.md) [![Report Bugs](https://img.shields.io/badge/Report%20Bugz-black?&logo=github&logoColor=black&label=&flat&labelColor=red)](https://github.com/seraph776/python-crash-course-amazon-review-scraper/issues/new/choose)


    


_Show your support and give this repo a_ ⭐

</div>  


## ℹ️ Info

This repo contains a web scraper using `Python Scrapy` that will collect and store customer reviews for [Python Crash Course, 2nd Edition](https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280/) by Eric Matthes.

- **Objective**: The objective for this scraping system is to collect customer reviews for  our target keywords and store the results.
- **Target Data**: The following items will be extracted and stored from each product: `name`, `rating`, `review_title`, `review_data`, and `review_text`. 
- **Scale**: This will be a relatively small scale web scraper.
- **Data Storage**: The data will be store in `CSV` and `JSON` files.


## Requirements

This project was built using the `Python 3.10.1` and the following modules: 

| Required                 | Version | Purpose                                        |
|--------------------------|:-------:|------------------------------------------------|
| `Scrapy `                |  2.7.1  | A web-crawling framework.                      | 
| `csv`                    |    _    | Reads and writes tabular data in CSV format.   | 



## Setup Instructions

Instructions on how to create a `pipenv` virtual environment.

<details>

<summary>⚙️  Click to View </summary>

1. Download [zip file](https://github.com/seraph776/python-crash-course-amazon-review-scraper/archive/refs/heads/main.zip) 
2. Extract zip files
3. Change directory into projectFolder:

```python
>>> cd projectFolder
```

4. Install from Pipfile:

```python
>>> pipenv install  
```

5. Activate virtual environment

```python
>>> pipenv shell
```

6. CD into project app directory

```python
>>> cd projectName/projectName
```

7. Install requirements from `requirements.txt`

```python
>>> pipenv install requirements.txt
```

</details>


## Usage



```python
>>> scrapy crawl spidername -o output.csv
```


For more information read [documentation](https://github.com/seraph776/python-crash-course-amazon-review-scraper).

## How to Contribute


Contributions are Welcome! For instructions on how to contribute please read our [Contributing Guidelines](https://github.com/seraph776/python-crash-course-amazon-review-scraper/blob/main/CONTRIBUTING.md). 


## Discussions

Have any Questions? Visit [Discussions](https://github.com/seraph776/python-crash-course-amazon-review-scraper/discussions) which is a space for our community to have conversations, ask questions and post answers without opening issues. Please read our [Code of Conduct](https://github.com/seraph776/python-crash-course-amazon-review-scraper/blob/main/CODE-OF-CONDUCT.md) which defines the  standards for engaging with the community!


## Feedback / Questions?

If you have any feedback or questions please contact me at [seraph776@gmail.com](mailto:seraph776@gmail.com)



## Donate


<details>
<summary>🪙 Support my work </summary>


All donations help fund the continued development of new content.


| Coin                                                                                                                        | Address                                                     |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <img src="https://user-images.githubusercontent.com/72005563/206338569-a607c171-5dfe-47c4-abed-a7e3beeab5bf.png" width=150> | 3GhUQkT7jJcfu6xuqrAh8E9PR5hwQhTXsC                          |
| <img src="https://user-images.githubusercontent.com/72005563/206338723-44e6f026-01fd-41dd-ab31-0c184c78a896.png" width=150> | 0x6fA9A81b7e6373Ca5C55A265dFeAa0d438c91D81                  |
| <img src="https://user-images.githubusercontent.com/72005563/206338886-1a07e215-0664-472a-a2a9-2a6d4e38b694.png" width=150> | 0x9a5C640a853B8E759111A28C4D43224a090E53d9                  |
| <img src="https://user-images.githubusercontent.com/72005563/206338998-9819976d-622a-462c-8d88-897a8d5880f4.png" width=150> | [Buy me a Coffee](https://www.buymeacoffee.com/codecrypt76) |       


</details>

## License 

All code in this repository is available under the [MIT License](https://github.com/seraph776/python-crash-course-amazon-review-scraper/blob/main/LICENSE) © [seraph★vega](https://github.com/seraph776)



<div align="right">

[[↑] Back to top](#top)

</div>  


