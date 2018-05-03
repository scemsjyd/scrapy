#启动步骤
```
# 基于python3
virtualenv -p /usr/local/bin/python3 --no-site-packages venv
# 如果是python2
virtualenv --no-site-packages venv
source venv/bin/activate
# 如果是python2 使用pip
pip3 install scrapy
# 如果是python2 使用PIL
pip install PIL
pip3 install Pillow

# 启动脚本
scrapy crawl image
```
