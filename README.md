# opensea_scraping
Scraping Daily top 500 data from opensea to json

## Requirments

```Python 3.8 or upper```
- `` pip install selenium``
- `` pip install webdriver_manager``
- ``pip install bs4``
- ``pip install pandas openpyxl``
- `` pip install schedule``
- Or ``pip install -r requirments.txt``

## Runing



Open ``config.py`` and add latest chrome driver path then just run ``run_all.py``

## __Note__
 For changing updates frequency just open ``run_all.py``, find code `` shcedule.every(24).hours.., and set up your time

