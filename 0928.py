# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:19:49 2023

@author: wlion
"""
"""
09-28 
目錄lccdgjango 下,先dir確認資料夾
1.安裝 pip install requests
  安裝 pip install beautifulsoup4 

2.執行 python tvbsnews.py
====================
開啟lcc/ news/views
"""

"""
try : 
	data = paginator.page(page)
except PageNotAnInteger:
	data = paginator.page(1)
except EmptyPage:
	data = paginator.page(paginator.num_pages)
#刪除 content 

return redner(request,'news.html',locaals())


"""

"""
開啟網頁 news.html

<!--分業 -->
<div style=" clear:both"></div>
<div style="float:left;height:60px; padding-top:100px;padding-left:45%">
{% if data,has_previous %}
<a href="?page={{data.previous_page_number}}">上一頁</a>

{% endif %}

{% if data,has_next %}
<a href="?page={{data.next_page_number}}">下一頁</a>

{% endif %}

<div>

"""

"""
重新到目錄 lccdjango/lcc/ python manage.py runserver
"""




