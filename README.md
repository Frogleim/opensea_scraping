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



Open ``config.py`` and add latest chrome driver ``path`` then just run ``run_all.py``




## __Note__
- For changing updates frequency just open ``run_all.py``, find code `` shcedule.every(24).hours.., and set up your time
- Dont keep open output files! Always close them, for now get errors from script


## Runing on server

- For runing sript on server change ``self.driver`` to ``self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                       desired_capabilities={
                                           "browserName": "chrome",
                                           "enableVNC": False,
                                           "enableVideo": False
                                       }, options=self.options)`` in ``all_time.py`` , ``daily.py`` , ``seven_days.py`` and in ``thirty_days.py``
- Install selenoid 
