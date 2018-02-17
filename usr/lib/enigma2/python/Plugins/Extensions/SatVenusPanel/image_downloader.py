import sys
import urllib, urllib2, re, os
from urllib import urlencode
from urllib2 import urlopen, URLError, Request, build_opener, HTTPCookieProcessor

#NOT WORKING ... NonSoloSat, Nachtfalke, Open-Plus, OpenSPA
#7 team on VenusCS + OpenSPA

module_path = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/'
temppath = '/tmp/'

list2=[]

def readnet(url):
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
        return data
    except:
        return None

    return None

def gethostname(url):
    from urlparse import parse_qs, urlparse
    query = urlparse(url)
    return query.hostname

def main_cats():

            cats=['VuPlus','DreamBox oe2.0','Xtrend','GigaBlue', 'Formuler']
            cats=[]
            cats.append(('VuPlus',''))
            cats.append(('DreamBox oe2.0',''))
            cats.append(('Xtrend',''))
            cats.append(('GigaBlue',''))
            cats.append(('Formuler',''))
            for cat in cats:
                print 'cat',cat
                addDir(cat[0], cat[0], 100, cat[1], '', 1)

def getteams(name,url,page):
       if name=='DreamBox oe2.0':
          mode=102
          teams=[('Demonisat', 'http://www.demonisat.info/demonisat-e2Img-OE2.0/', ''),
                 ('Dreamboxupdate', 'http://www.dreamboxupdate.com/opendreambox/2.0.0/images/', ''),
                 ('Dream-Elite', 'http://images.dream-elite.net/DE4/index.php?dir=', ''),			 
                 ('Merlin3', 'http://feed.merlin3.info/', ''),
                 ('NewNigma2', 'http://feed.newnigma2.to/daily/', ''),
                 ('NonSoloSat', 'http://www.nonsolosat.net/upload/index.php?dir=Dreambox%20/', ''),#NOT WORKING			 
                 ('OoZooN', 'https://www.oozoon-download.de/opendreambox/images/', ''),
                 ('OpenATV', 'http://images.mynonpublic.com/openatv/6.2/index.php?open=', ''),
                 ('OpenESI', 'http://www.openesi.eu/images/Dreambox/', ''),
                 ('OpenPLi', 'https://openpli.org/download/dreambox/', ''),
                 ('Power-Sat', 'http://www.power-sat.org/power-plus/Powersat_2.0/', ''),
                 ('SatDreamGR', 'http://sgcpm.com/satdreamgr-images/dreambox/', ''),
                 ('TSimage', 'http://tunisia-dreambox.info/tsimage-feed/unstable/3.0/images/', '')]

       elif name=='VuPlus':
           mode=103
           teams=[('Black Hole', 'http://178.63.156.75/VuPlusImages/BlackHole/vu', ''),#On VenusCS
                  ('Code.VuPlus', 'http://code.vuplus.com/index.html?action=image&image=30&model=vu', ''),		   
                  ('Custom Build', 'http://178.63.156.75/VuPlusImages/Custom/vu', ''),#On VenusCS
                  ('HDmedia', 'http://www.hdmedia-universe.com/board/pages.php?pageid=1&box=vu', ''),
                  ('Odisealinux', 'https://www.odisealinux.com/Test/', ''),
                  ('OpenATV', 'http://images.mynonpublic.com/openatv/6.2/index.php?open=vu', ''),
                  ('Open Black Hole', 'http://178.63.156.75/VuPlusImages/OpenBlackHole/vu', ''),#On VenusCS
                  ('OpenDROID', 'http://images.opendroid.org/6.4/VU+/vu', ''),
                  ('OpenESI', 'http://www.openesi.eu/images/VU+/vu', ''),
                  ('OpenHDF', 'http://v62.hdfreaks.cc/vu', ''),
                  ('OpenPLi', 'https://openpli.org/download/vuplus/', ''),
                  ('OpenPlus', 'http://images.open-plus.es/?dir=./', ''),#NOT WORKING
#                  ('OpenSPA', 'https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes/Vuplus/vu', ''),#NOT WORKING
                  ('OpenSPA', 'http://178.63.156.75/VuPlusImages/OpenSPA/VuPlus/', ''),#On VenusCS
                  ('OpenViX', 'http://www.openvix.co.uk/index.php/downloads/vu-plus-images/', ''),
                  ('PKTeam', 'http://e2.pkteam.pl/IMAGE%20VU%2B/HYPERION%205.8/', ''),
                  ('PurE2', 'http://pur-e2.club/OU/images/index.php?dir=6.2/', ''),
                  ('ruDREAM', 'http://178.63.156.75/VuPlusImages/ruDREAM/vu', ''),#On VenusCS
                  ('SatDreamGR', 'http://sgcpm.com/satdreamgr-images-experimental/vu/vu', ''),
                  ('SFTeam', 'http://178.63.156.75/VuPlusImages/SFteam/vu', ''),#On VenusCS
                  ('VTi', 'http://178.63.156.75/VuPlusImages/VTi/vu', '')]#On VenusCS

       elif name=='Xtrend':
           mode=114
           teams=[('HDmedia', 'http://www.hdmedia-universe.com/board/pages.php?pageid=1&box=', ''),
                  ('OpenATV', 'http://images.mynonpublic.com/openatv/6.2/index.php?open=', ''),
                  ('OpenESI', 'http://www.openesi.eu/images/index.php?dir=Xtrend/', ''),
                  ('OpenHDF', 'http://v62.hdfreaks.cc/', ''),
                  ('OpenPLi', 'https://openpli.org/download/xtrend/', ''),				  
                  ('OpenViX', 'http://www.openvix.co.uk/index.php/downloads/xtrend-images/', ''),
                  ('SatDreamGR', 'http://sgcpm.com/satdreamgr-images/et/', '')]

       elif name=='GigaBlue':
           mode=116
           teams=[('HDmedia', 'http://www.hdmedia-universe.com/board/pages.php?pageid=1&box=', ''),
#                  ('Nachtfalke', 'http://dev.nachtfalke.biz/nfr/feeds/6.1/images/', ''),#NOT WORKING		   
                  ('Odisealinux', 'https://www.odisealinux.com/Test/', ''),
                  ('OpenATV', 'http://images.mynonpublic.com/openatv/6.2/index.php?open=', ''),
                  ('OpenDROID', 'http://images.opendroid.org/6.4/GigaBlue/', ''),
                  ('OpenESI', 'http://www.openesi.eu/images/index.php?dir=GigaBlue/', ''),
                  ('OpenHDF', 'http://v62.hdfreaks.cc/', ''),
#                  ('OpenSPA', 'https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes%2FGigaBlue/', ''),#NOT WORKING
                  ('OpenViX', 'http://www.openvix.co.uk/index.php/downloads/gigablue-images/',''),
                  ('PurE2', 'http://pur-e2.club/OU/images/index.php?dir=6.2/', ''),
                  ('TeamBlue', 'http://images.teamblue.tech/6.1-release/index.php?open=','')]

       elif name=='Formuler':
           mode=118
           teams=[('HDmedia', 'http://www.hdmedia-universe.com/board/pages.php?pageid=1&box=', ''),
#                  ('Nachtfalke', 'http://dev.nachtfalke.biz/nfr/feeds/6.1/images/', ''),#NOT WORKING		   
                  ('OpenATV', 'http://images.mynonpublic.com/openatv/6.2/index.php?open=', ''),
                  ('OpenDROID', 'http://images.opendroid.org/6.4/Formuler/', ''),
                  ('OpenHDF', 'http://v62.hdfreaks.cc/', ''),
                  ('OpenPLi', 'https://openpli.org/download/formuler/',''),
#                  ('OpenSPA', 'https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes%2FFormuler/', ''),#NOT WORKING
                  ('OpenViX', 'http://www.openvix.co.uk/index.php/downloads/forumler-images/',''),
                  ('PKTeam', 'http://e2.pkteam.pl/IMAGE%20FORMULER/', '')]

       for team in teams:
         addDir(team[0], team[1], mode, team[2], '', 1)
######################
######################
def formulermodels(name,url,page):
          models =['formuler1',
                   'formuler3',
                   'formuler4',
                   'formuler4turbo']
          for model in models:
                print 'model',model
                href=url+model
                addDir(model, href,119, '','', 1)
######################
def extract_formulerimages(model,url,page):
    if 'openpli' in url: 
       if model=='formuler1':
        model='F1'
       if model=='formuler3':
        model='F3'
       if model=='formuler4':
        model='F4' 
       if model=='formuler4turbo':
        model='F4+Turbo'  			
       url='https://openpli.org/download/formuler/'+model
    if 'hdmedia' in url: 
       if model=='formuler1':
        model='FormulerF1'
       if model=='formuler3':
        model='FormulerF3'	
       url='http://www.hdmedia-universe.com/board/pages.php?pageid=1&box='+model
    if 'openatv' in url: 
       url='http://images.mynonpublic.com/openatv/6.2/index.php?open='+model
    if 'opendroid' in url: 	
        url='http://images.opendroid.org/6.4/Formuler/'+model	   
    if 'hdfreaks' in url: 
        url='http://v62.hdfreaks.cc/'+model		   
    if 'openvix' in url: 
       if model=='formuler1':
        model='formuler-1'
       if model=='formuler3':
        model='' 
       if model=='formuler4':
        model='' 
       if model=='formuler4turbo':
        model='formuler-f4-turbo' 		
       url='http://www.openvix.co.uk/index.php/downloads/forumler-images/'+model 
    if 'pkteam' in url: 		
       if model=='formuler1':
        model='HYPERION%205.8'
       if model=='formuler3':
        model='HYPERION%205.8'
       if model=='formuler4':
        model='HYPERION%205.8' 
       if model=='formuler4turbo':
        model='HYPERION%205.8' 		
       print 'model',model		
       url='http://e2.pkteam.pl/IMAGE%20FORMULER/'+model
    if 'openspa' in url:#NOT WORKING
        url='https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes%2FFormuler/'+model
    if 'nachtfalke' in url: #NOT WORKING
        url='http://dev.nachtfalke.biz/nfr/feeds/6.1/images/'+model
	   
    print "image_url",url		   
    data=readnet(url)    
    if data is None:
       print 'download error'
       return (False, 'Download error')
    url=url.lower()
    listdata=[]

    if 'nachtfalke' in url: #NOT WORKING
       regx='''<tr><td><a href="(.*?)" title="(.*?)">(.*?)</a></td>.*?</tr>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           href='http://dev.nachtfalke.biz/nfr/feeds/6.1/images/'+model+'/'+href			  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'openspa' in url: #NOT WORKING	
       regx='''<a href="(.*?)" title="(.*?)" class="files">'''	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='https://openspa.webhop.info/Descarga%20de%20Im%C3%A1genes%2FFormuler/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'pkteam' in url: 	
       regx='''<a href="(.*?)">(.*?)..&gt;</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://e2.pkteam.pl/IMAGE%20FORMULER/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))	
		   		
    if 'openvix' in url: 
       regx='''<.*?href="(.*?)" download="(.*?)".*?>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))	
	
    if 'hdfreaks' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://v62.hdfreaks.cc/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))	
	
    if 'opendroid' in url: 	
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
              continue
           href='http://images.opendroid.org/6.4/Formuler/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		
	
    if 'hdmedia' in url: 
       regx='''<td class="list_files_table_file_link"><font color="#ff0000"><b>Flash Image: </b></font><a href="(.*?)">(.*?)</a></td>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))

    if 'openatv' in url: 
       regx='''<a href='(.*?)'>(.*?)</a><br/>'''       
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://images.mynonpublic.com/openatv/6.2/'+href
           listdata.append((name.strip(),href,imdate,imsize)) 
		   
    if 'openpli' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))			   

    print 'listdata',listdata
    for item in listdata:
        addDir(item[0],item[1],10,'','',1,True)
    return True,listdata	
###################### 
######################       
def dreamboxmodels(name,url,page):
            models = ['dm500hd',
             'dm500hdv2',			
             'dm800se',
             'dm800sev2',
             'dm7020hd',			 
             'dm7020hdv2',
             'dm8000']
            for model in models:
                print 'model',model				 
                href=url+model  
                addDir(model, href,104, '','', 1)
######################				          		   
def extract_dreamboximages(model,url,page):
    if 'openpli' in url: 		
       if model=='dm500hd':
        model='DM500+HD'	
       if model=='dm800se':
        model='DM800+SE'	
       if model=='dm7020hd':
        model='DM7020+HD'		
       if model=='dm8000':
        model='DM8000'			
       url='https://openpli.org/download/dreambox/'+model	   
    if 'openatv' in url: 
       url='http://images.mynonpublic.com/openatv/6.2/index.php?open='+model 
    if 'openesi' in url: 
        url='http://www.openesi.eu/images/Dreambox/'+model	
    if 'demonisat' in url: 
       if model=='dm500hd':
        model='DM%20500%20HD'	
       if model=='dm800se':
        model='DM%20800se%20HD'	
       if model=='dm7020hd':
        model='DM%207020%20HD'		
       if model=='dm7020hdv2':
        model='DM%207020%20HDv2'
       if model=='dm800sev2':
        model='DM%20800sev2%20HD'
       if model=='dm500hdv2':
        model='DM%20500HDv2'
       if model=='dm8000':
        model='DM%208000%20HD'		
       print 'model',model
       url='http://www.demonisat.info/demonisat-e2Img-OE2.0/'+model		
    if 'oozoon' in url: 
        url='https://www.oozoon-download.de/opendreambox/images/'+model
    if 'dreamboxupdate' in url: 
        url='http://www.dreamboxupdate.com/opendreambox/2.0.0/images/'+model		
    if 'tsimage' in url: 
        url='http://tunisia-dreambox.info/tsimage-feed/unstable/3.0/images/'+model
    if 'merlin3' in url: 
       if model=='dm500hd':
        model='images'	
       if model=='dm500hdv2':
        model='images'	
       if model=='dm800se':
        model='images'
       if model=='dm800sev2':
        model='images'
       if model=='dm7020hd':
        model='images'
       if model=='dm7020hdv2':
        model='images'
       if model=='dm8000':
        model='images'		
       print 'model',model	
       url='http://feed.merlin3.info/'+model
    if 'power-sat' in url: 
       if model=='dm500hd':
        model='Immagini_OE_2.0_powersat'	
       if model=='dm500hdv2':
        model='Immagini_OE_2.0_powersat'	
       if model=='dm800se':
        model='Immagini_OE_2.0_powersat'
       if model=='dm800sev2':
        model='Immagini_OE_2.0_powersat'
       if model=='dm7020hd':
        model='Immagini_OE_2.0_powersat'
       if model=='dm7020hdv2':
        model='Immagini_OE_2.0_powersat'
       if model=='dm8000':
        model='Immagini_OE_2.0_powersat'		
       print 'model',model 	
       url='http://www.power-sat.org/power-plus/Powersat_2.0/'+model
    if 'newnigma2' in url: 
       if model=='dm500hd':
        model='images'	
       if model=='dm500hdv2':
        model='images'	
       if model=='dm800se':
        model='images'
       if model=='dm800sev2':
        model='images'
       if model=='dm7020hd':
        model='images'
       if model=='dm7020hdv2':
        model='images'
       if model=='dm8000':
        model='images'		
       print 'model',model 	
       url='http://feed.newnigma2.to/daily/'+model
    if 'dream-elite' in url: 
       if model=='dm500hd':
        model='DM500HD'
       if model=='dm800se':
        model='DM800SE'
       if model=='dm7020hd':
        model='DM7020HD'	
       if model=='dm7020hdv2':
        model='DM7020HDv2'
       if model=='dm800sev2':
        model='DM800SEv2'
       if model=='dm500hdv2':
        model='DM500HDv2'
       if model=='dm8000':
        model='DM8000'
       print 'model',model
       url='http://images.dream-elite.net/DE4/index.php?dir='+model	   
    if 'nonsolosat' in url: #NOT WORKING
       if model=='dm500hd':
        model='Nonsolosat%208.7'	
       if model=='dm500hdv2':
        model='Nonsolosat%208.7'	
       if model=='dm800se':
        model='Nonsolosat%208.7'
       if model=='dm800sev2':
        model='Nonsolosat%208.7'
       if model=='dm7020hd':
        model='Nonsolosat%208.7'
       if model=='dm7020hdv2':
        model='Nonsolosat%208.7'
       if model=='dm8000':
        model='Nonsolosat%208.7'		
       print 'model',model
       url='http://www.nonsolosat.net/upload/index.php?dir=Dreambox%20/'+model
	   
    print 'image_url',url

    data=readnet(url)
    if data is None:
       return (False, 'Download error')
    url=url.lower()
    listdata=[]

    if 'nonsolosat' in url: #NOT WORKING
       regx='''<a class="autoindex_a" href="(.*?)">'''
       images=re.findall(regx,data, re.M|re.I)
       for href in images:
           imdate=''
           imsize=''
           try:href=href.split("file=")[1]
           except:continue
           name=href	   
           href='http://www.nonsolosat.net/upload/Dreambox%20/'+model+"/"+href#download failed
           listdata.append((name.strip(),href,imdate,imsize))
	
    if 'dream-elite' in url:
       regx='''<a class="autoindex_a" href="(.*?)">'''
       images=re.findall(regx,data, re.M|re.I)
       for href in images:
           imdate=''
           imsize=''
           try:href=href.split("file=")[1]
           except:continue
           name=href
           href='http://images.dream-elite.net/DE4/'+model+"/"+href
           listdata.append((name.strip(),href,imdate,imsize))	
	
    if 'merlin3' in url: 
       regx='''<td><a href="(.*?)">(.*?)</a></td>'''	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.nfi' in href:
              continue           
           href='http://feed.merlin3.info/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))
		   
    if 'newnigma2' in url: 
       regx='''<td><a href="(.*?)">(.*?)</a></td>''' 	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.nfi' in href:
              continue           
           href='http://feed.newnigma2.to/daily/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))		   
	
    if 'power-sat' in url: 
       regx='''<td><a href="(.*?)">(.*?)..&gt;</a></td>'''	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue           
           href='http://www.power-sat.org/power-plus/Powersat_2.0/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))
		   
    if 'tsimage' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.nfi' in href:
              continue           
           href='http://tunisia-dreambox.info/tsimage-feed/unstable/3.0/images/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))

    if 'dreamboxupdate' in url: 
       regx='''<a class="nfi" href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.nfi' in href:
              continue           
           href='http://www.dreamboxupdate.com/opendreambox/2.0.0/images/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))
		   
    if 'oozoon' in url:  
       regx='''<td><a href="(.*?)">(.*?)</a></td>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.nfi' in href:
              continue           
           href='https://www.oozoon-download.de/opendreambox/images/'+model+'/'+href
           listdata.append((name,href,imdate,imsize))			   
		   
    if 'demonisat' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://www.demonisat.info/demonisat-e2Img-OE2.0/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))	
			   
    if 'openesi' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://www.openesi.eu/images/Dreambox/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		   

    if 'satdreamgr' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if 'parent' in name.lower():
              continue
           
           href='http://sgcpm.com/satdreamgr-images/dreambox/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'openatv' in url: 
       regx='''<a href='(.*?)'>(.*?)</a><br/>'''       
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://images.mynonpublic.com/openatv/6.2/'+href
           listdata.append((name.strip(),href,imdate,imsize)) 
		   
    if 'openpli' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))		   
                 
    print 'listdata',listdata
    for item in listdata:
        addDir(item[0],item[1],10,'','',1,True)
    return True,listdata 
######################	
######################	   
def vuplusmodels(name,url,page):
            models = ['zero',
             'uno',
             'solo',
             'solo2',
             'ultimo',
             'duo',
             'duo2',
             'solose',
             'solo4k',
             'zero4k',
             'uno4k',
             'uno4kse',
             'ultimo4k']            
            for model in models:
              print 'model',model
              href=url+model  
              addDir(model, href,105, '','', 1)  
######################	
def extract_vuplusimages(model,url,page):
    if 'openatv' in url: 
       url='http://images.mynonpublic.com/openatv/6.2/index.php?open=vu'+model 
    if 'openvix' in url:
       if model=='duo2':
        model='duo-2'
       if model=='solose':
        model='solo-se'
       if model=='solo2':
        model='solo-2'
       if model=='uno4kse':
        model='uno4k-se'
       if model=='zero4k':
        model='zero-4'
       url='http://www.openvix.co.uk/index.php/downloads/vu-plus-images/vu-'+model  
    if 'satdreamgr' in url: 
        url='http://sgcpm.com/satdreamgr-images-experimental/vu/vu'+model
    if 'openesi' in url: 
        url='http://www.openesi.eu/images/VU+/vu'+model
    if 'opendroid' in url: 
        url='http://images.opendroid.org/6.4/VU+/vu'+model
    if 'openblackhole' in url: 
        url='http://178.63.156.75/VuPlusImages/OpenBlackHole/vu'+model
    if 'vti' in url:
        url='http://178.63.156.75/VuPlusImages/VTi/vu'+model
    if 'sfteam' in url:
        url='http://178.63.156.75/VuPlusImages/SFTeam/vu'+model
    if 'blackhole' in url:
        url='http://178.63.156.75/VuPlusImages/BlackHole/vu'+model
    if 'rudream' in url:
        url='http://178.63.156.75/VuPlusImages/ruDREAM/vu'+model
    if 'custom' in url:
        url='http://178.63.156.75/VuPlusImages/Custom/vu'+model
    if 'hdfreaks' in url:
        url='http://v62.hdfreaks.cc/vu'+model
    if 'openpli' in url:
       if model=='uno':
        model='Uno'
       if model=='solo':
        model='Solo'
       if model=='solo2':
        model='Solo2'
       if model=='zero':
        model='Zero'
       if model=='ultimo':
        model='Ultimo'
       if model=='solose':
        model='Solo+SE'
       if model=='uno4k':
        model='Uno+4K'
       if model=='ultimo4k':
        model='Ultimo+4K'
       if model=='uno4kse':
        model='Uno+4K+SE'
       if model=='zero4k':
        model='Zero+4K'
       if model=='solo4k':
        model='Solo+4K'
       if model=='duo':
        model='Duo'
       if model=='duo2':
        model='Duo2'
       print 'model',model		
       url='https://openpli.org/download/vuplus/'+model
    if 'pkteam' in url:
       if model=='uno':
        model='HYPERION%205.8'
       if model=='solo':
        model='HYPERION%205.8'
       if model=='solo2':
        model='HYPERION%205.8'
       if model=='zero':
        model='HYPERION%205.8'
       if model=='ultimo':
        model='HYPERION%205.8'
       if model=='solose':
        model='HYPERION%205.8'
       if model=='uno4k':
        model='HYPERION%205.8'
       if model=='ultimo4k':
        model='HYPERION%205.8'
       if model=='uno4kse':
        model='HYPERION%205.8'
       if model=='zero4k':
        model='HYPERION%205.8'
       if model=='solo4k':
        model='HYPERION%205.8'
       if model=='duo':
        model='HYPERION%205.8'
       if model=='duo2':
        model='HYPERION%205.8'
       print 'model',model
       url='http://e2.pkteam.pl/IMAGE%20VU%2B/'+model
    if 'code.vuplus' in url:
       print 'model',model	
       if model=='duo':
        model='bm750'	
        url='http://code.vuplus.com/index.html?action=image&image=30&model='+model
       else:
        url='http://code.vuplus.com/index.html?action=image&image=30&model=vu'+model	   
    if 'hdmedia' in url:    
       url='http://www.hdmedia-universe.com/board/pages.php?pageid=1&box=vu'+model
    if 'odisealinux' in url: 
       if model=='uno':
        model='VuPlus.html'
       if model=='solo':
        model='VuPlus.html'
       if model=='solo2':
        model='VuPlus.html'
       if model=='zero':
        model='VuPlus.html'
       if model=='ultimo':
        model='VuPlus.html'
       if model=='solose':
        model='VuPlus.html'
       if model=='uno4k':
        model='VuPlus.html'
       if model=='ultimo4k':
        model='VuPlus.html'
       if model=='uno4kse':
        model='VuPlus.html'
       if model=='zero4k':
        model='VuPlus.html'
       if model=='solo4k':
        model='VuPlus.html'
       if model=='duo':
        model='VuPlus.html'
       if model=='duo2':
        model='VuPlus.html'
       print 'model',model
       url='https://www.odisealinux.com/Test/'+model
    if 'pur-e2' in url:
       if model=='uno':
        model='vuplus'
       if model=='solo':
        model='vuplus'
       if model=='solo2':
        model='vuplus'
       if model=='zero':
        model='vuplus'
       if model=='ultimo':
        model='vuplus'
       if model=='solose':
        model='vuplus'
       if model=='uno4k':
        model='vuplus'
       if model=='ultimo4k':
        model='vuplus'
       if model=='uno4kse':
        model='vuplus'
       if model=='zero4k':
        model='vuplus'
       if model=='solo4k':
        model='vuplus'
       if model=='duo':
        model='vuplus'
       if model=='duo2':
        model='vuplus'
       print 'model',model
       url='http://pur-e2.club/OU/images/index.php?dir=6.2/'+model
    if 'open-plus' in url: #NOT WORKING
        url='http://images.open-plus.es/?dir=.%2Fvu'+model
#    if 'openspa' in url:#NOT WORKING
#        url='https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes/Vuplus/vu'+model
    if 'openspa' in url:#On VenusCS
        url='http://178.63.156.75/VuPlusImages/OpenSPA/VuPlus/'+model		

    print "image_url",url

    data=readnet(url)

    if data is None:
       print 'download error'
       return (False, 'Download error')
    url=url.lower()
    listdata=[]

    if 'openspa' in url:#On VenusCS
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/OpenSPA/VuPlus/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))	
	
#    if 'openspa' in url: #NOT WORKING	
#       regx='''<li class="files"><a class="files" href="(.*?)" title="(.*?)"><span class="icon file-zip">.*?/li>'''
#       regx='''<a href="(.*?)" title="(.*?)" class="files"</a>'''
#       regx='''<a class="files" href="(.*?)".*?</a>'''
#       regx='''<a href="(.*?)">(.*?)</a>'''
#       regx='''<a href="(.*?)" title="(.*?)" class="files"><span class="name">(.*?)</span></a>'''
#       regx='''<a href=(.*?)><span class=(.*?)>(.*?)</span></a>'''	 	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='https://openspa.webhop.info/Descarga%20de%20Im%C3%A1genes/Vuplus/vu'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'open-plus' in url: #NOT WORKING
#       regx='''<li class="files"><a href="(.*?)" title="(.*?)" class="files">'''	
#       regx='''<a class="item _blank zip" href="(.*?)" target="_parent">(.*?)</a>'''
#       regx='''<a class="item _blank zip" href="(.*?)" target="_parent">(.*?)</a>'''
#       regx='''<a href="(.*?)" target="_parent" class="item _blank zip">(.*?)</a>'''	
       regx='''<a href="(.*?)" target="_parent" class="item _blank zip">(.*?)</a>'''   
       images=re.findall(regx,data, re.M|re.I)
       for href in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://images.open-plus.es/?dir=vu'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))			   

    if 'pur-e2' in url:
       regx='''<a class="autoindex_a" href="(.*?)">'''
       images=re.findall(regx,data, re.M|re.I)
       for href in images:
           imdate=''
           imsize=''
           try:href=href.split("file=")[1]
           except:continue
           name=href
           href='http://pur-e2.club/OU/images/6.2/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))		   
		   
    if 'sfteam' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/SFTeam/vu'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'odisealinux' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))

    if 'hdmedia' in url: 
       regx='''<td class="list_files_table_file_link"><font color="#ff0000"><b>Flash Image: </b></font><a href="(.*?)">(.*?)</a></td>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))

    if 'code.vuplus' in url: 
       regx='''<tr><td><a href="(.*?)" rel="external">(.*?)</a></td></tr>'''
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://code.vuplus.com'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'pkteam' in url: 
       regx='''<a href="(.*?)">(.*?)..&gt;</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://e2.pkteam.pl/IMAGE%20VU%2B/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'openpli' in url:
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))

    if 'hdfreaks' in url:
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://v62.hdfreaks.cc/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'custom' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/Custom/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))

    if 'rudream' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/ruDREAM/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		   
		   		   
    if 'opendroid' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
              continue
           href='http://images.opendroid.org/6.4/VU+/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		    
    		   		   
    if 'satdreamgr' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if 'parent' in name.lower():
              continue
           
           href='http://sgcpm.com/satdreamgr-images-experimental/vu/vu'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))   
    
    if 'openesi' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://www.openesi.eu/images/VU+/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'openblackhole' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/OpenBlackHole/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		   	   

    if 'vti' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/VTi/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))

    if 'blackhole' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://178.63.156.75/VuPlusImages/BlackHole/vu'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'openatv' in url: 
       regx='''<a href='(.*?)'>(.*?)</a><br/>'''       
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://images.mynonpublic.com/openatv/6.2/'+href
           listdata.append((name.strip(),href,imdate,imsize)) 
		   	   
    if 'openvix' in url: 
       regx='''<.*?href="(.*?)" download="(.*?)".*?>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))
           
    print 'listdata',listdata
    for item in listdata:
        addDir(item[0],item[1],10,'','',1,True)
    return True,listdata 
######################
###################### 
def xtrendmodels(name,url,page):
          models =['ET4x00',
                   'ET5x00',
                   'ET6x00',
                   'ET7x00',
                   'ET8x00',
                   'ET8500',				   
                   'ET9x00',
                   'ET10000']            
          for model in models:
                print 'model',model
                href=url+model  
                addDir(model, href,115, '','', 1)  
######################
def extract_xtrendimages(model,url,page):
    if 'openatv' in url: 
       url='http://images.mynonpublic.com/openatv/6.2/index.php?open='+model.lower()
    if 'openvix' in url:        
       url='http://www.openvix.co.uk/index.php/downloads/xtrend-images/xtrend-'+model.lower()+'-images/'
    if 'satdreamgr' in url: 
       url='http://sgcpm.com/satdreamgr-images/et/'+model.lower()
    if 'openesi' in url: 
       url='http://www.openesi.eu/images/Xtrend/'+model.lower()
    if 'openpli' in url:              
       url='https://openpli.org/download/xtrend/'+model
    if 'hdfreaks' in url: 
        url='http://v62.hdfreaks.cc/'+model.lower()
    if 'hdmedia' in url:        
       url='http://www.hdmedia-universe.com/board/pages.php?pageid=1&box='+model.lower()		   

    print "image_url",url		   
    data=readnet(url)    
    if data is None:
       print 'download error'
       return (False, 'Download error')
    url=url.lower()
    listdata=[]	  

    if 'hdmedia' in url: 
       regx='''<td class="list_files_table_file_link"><font color="#ff0000"><b>Flash Image: </b></font><a href="(.*?)">(.*?)</a></td>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))

    if 'hdfreaks' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://v62.hdfreaks.cc/'+model.lower()+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'openatv' in url: 
       regx='''<a href='(.*?)'>(.*?)</a><br/>'''       
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://images.mynonpublic.com/openatv/6.2/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'openvix' in url: 
       regx='''<.*?href="(.*?)" download="(.*?)".*?>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'satdreamgr' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if 'parent' in name.lower():
              continue
           
           href='http://sgcpm.com/satdreamgr-images/et/'+model.lower()+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))   

    if 'openesi' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://www.openesi.eu/images/Xtrend/'+model.lower()+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		   
		   
    if 'openpli' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))			   

    print 'listdata',listdata
    for item in listdata:
        addDir(item[0],item[1],10,'','',1,True)
    return True,listdata 	   
######################
######################  
def gigabluemodels(name,url,page):
          models = ['gb800solo',
             'gb800se',
             'gb800seplus',
             'gb800ue',
             'gb800ueplus',
             'gbultraue',
             'gbquad',
             'gbquadplus',
             'gbx1',
             'gbx2',
             'gbx3',
             'gbipbox',
             'gbue4k',
             'gbquad4k']            
          for model in models:
                print 'model',model
                href=url+model  
                addDir(model, href,117, '','', 1)  
######################
def extract_gigablueimages(model,url,page):
    if 'openatv' in url: 
       url='http://images.mynonpublic.com/openatv/6.2/index.php?open='+model
    if 'openesi' in url: 
       url='http://www.openesi.eu/images/GigaBlue/'+model	   
    if 'opendroid' in url: 
        url='http://images.opendroid.org/6.4/GigaBlue/'+model
    if 'hdfreaks' in url: 
        url='http://v62.hdfreaks.cc/'+model	
    if 'teamblue' in url: 
        url='http://images.teamblue.tech/6.1-release/index.php?open='+model
    if 'hdmedia' in url:    
       url='http://www.hdmedia-universe.com/board/pages.php?pageid=1&box='+model		
    if 'odisealinux' in url: 
       if model=='gb800solo':
        model='Gigablue.html'	
       if model=='gb800se':
        model='Gigablue.html'	
       if model=='gb800seplus':
        model='Gigablue.html'	
       if model=='gb800ue':
        model='Gigablue.html'	
       if model=='gb800ueplus':
        model='Gigablue.html'		
       if model=='gbultraue':
        model='Gigablue.html'	
       if model=='gbquad':
        model='Gigablue.html'	
       if model=='gbquadplus':
        model='Gigablue.html'	
       if model=='gbx1':
        model='Gigablue.html'	
       if model=='gbx2':
        model='Gigablue.html'	
       if model=='gbx3':
        model='Gigablue.html'	
       if model=='gbipbox':
        model='Gigablue.html'
       if model=='gbue4k':
        model='Gigablue.html'
       if model=='gbquad4k':
        model='Gigablue.html'		
       print 'model',model 	
       url='https://www.odisealinux.com/Test/'+model
    if 'openvix' in url: 
       if model=='gb800solo':
        model='hd800-solo-images'	
       if model=='gb800se':
        model='hd800-se-images'	
       if model=='gb800seplus':
        model='hd800-se-plus-images'	
       if model=='gb800ue':
        model='hd800-ue-images'
       if model=='gb800ueplus':
        model='hd800-ue-plus-images'		
       if model=='gbultraue':
        model='hd-ultra-ue-images'	
       if model=='gbquad':
        model='quad'	
       if model=='gbquadplus':
        model='hd-quad-plus'	
       if model=='gbx1':
        model='hd-x1-images/'	
       if model=='gbx2':
        model='hd-x2-images'	
       if model=='gbx3':
        model='hd-x3'	
       if model=='gbipbox':
        model='GiGaBlue-IPBOX'
       if model=='gbue4k':
        model='uhd-ue-4k'
       if model=='gbquad4k':
        model='uhd-quad-4k'		
       print 'model',model   
       url='http://www.openvix.co.uk/index.php/downloads/gigablue-images/gigablue-'+model
    if 'pur-e2' in url:
       if model=='gb800solo':
        model='gigablue'	
       if model=='gb800se':
        model='gigablue'	
       if model=='gb800seplus':
        model='gigablue'	
       if model=='gb800ue':
        model='gigablue'	
       if model=='gb800ueplus':
        model='gigablue'		
       if model=='gbultraue':
        model='gigablue'	
       if model=='gbquad':
        model='gigablue'	
       if model=='gbquadplus':
        model='gigablue'	
       if model=='gbx1':
        model='gigablue'	
       if model=='gbx2':
        model='gigablue'	
       if model=='gbx3':
        model='gigablue'	
       if model=='gbipbox':
        model='gigablue'
       if model=='gbue4k':
        model='gigablue'
       if model=='gbquad4k':
        model='gigablue'		
       print 'model',model 	
       url='http://pur-e2.club/OU/images/index.php?dir=6.2/'+model
    if 'openspa' in url: #NOT WORKING
        url='https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes%2FGigaBlue/'+model
    if 'nachtfalke' in url: #NOT WORKING
        url='http://dev.nachtfalke.biz/nfr/feeds/6.1/images/'+model
	   
    print "image_url",url		   
    data=readnet(url)    
    if data is None:
       print 'download error'
       return (False, 'Download error')
    url=url.lower()
    listdata=[]		   
	
    if 'openspa' in url: #NOT WORKING
       regx='''<li class="files"><a href="(.*?)" title="(.*?)" class="files"><span class="icon file f-zip">.zip</span><span class="name">.*?</span><span class="details">.*?</span></a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='https://openspa.webhop.info/#Descarga%20de%20Im%C3%A1genes%2FGigaBlue/'+model			  
           listdata.append((name.strip(),href,imdate,imsize))	

    if 'nachtfalke' in url: #NOT WORKING
       regx='''<tr><td><a href="(.*?)" title="(.*?)">(.*?)</a></td>.*?</tr>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           href='http://dev.nachtfalke.biz/nfr/feeds/6.1/images/'+model+'/'+href			  
           listdata.append((name.strip(),href,imdate,imsize))	

    if 'pur-e2' in url:
       regx='''<a class="autoindex_a" href="(.*?)">'''
       images=re.findall(regx,data, re.M|re.I)
       for href in images:
           imdate=''
           imsize=''
           try:href=href.split("file=")[1]
           except:continue
           name=href
           href='http://pur-e2.club/OU/images/6.2/'+model+'/'+href
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'openatv' in url: 
       regx='''<a href='(.*?)'>(.*?)</a><br/>'''       
       images=re.findall(regx,data, re.M|re.I)
       print 'images',images
       for href,name in images:
           imdate=''
           imsize=''
           href='http://images.mynonpublic.com/openatv/6.2/'+href
           listdata.append((name.strip(),href,imdate,imsize))

    if 'openesi' in url: 
       regx='''<li><a href="(.*?)">(.*?)</a></li>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://www.openesi.eu/images/GigaBlue/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'teamblue' in url: 
       regx='''<a href='(.*?)' class="button"><span class="mif-download mif-lg fg-darkCyan"></span>(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
              continue
           href='http://images.teamblue.tech/6.1-release/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))
	   
    if 'openvix' in url: 
       regx='''<.*?href="(.*?)" download="(.*?)".*?>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'hdmedia' in url: 
       regx='''<td class="list_files_table_file_link"><font color="#ff0000"><b>Flash Image: </b></font><a href="(.*?)">(.*?)</a></td>'''
       images=re.findall(regx,data, re.M|re.I)
       print "images",images   
       for href,name in images:
           imdate=''
           imsize=''          
           print href           
           listdata.append((name.strip(),href,imdate,imsize))

    if 'odisealinux' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''	   
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not ".zip" in href:
              continue
           listdata.append((name.strip(),href,imdate,imsize))
		   
    if 'opendroid' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
              continue
           href='http://images.opendroid.org/6.4/GigaBlue/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))

    if 'hdfreaks' in url: 
       regx='''<a href="(.*?)">(.*?)</a>'''
       images=re.findall(regx,data, re.M|re.I)
       for href,name in images:
           imdate=''
           imsize=''
           if not '.zip' in href:
              continue
           href='http://v62.hdfreaks.cc/'+model+'/'+href	  
           listdata.append((name.strip(),href,imdate,imsize))		   
		   
    print 'listdata',listdata
    for item in listdata:
        addDir(item[0],item[1],10,'','',1,True)
    return True,listdata 	
######################
######################
def addDir(name, url, mode, iconimage, desc = '', page = '',link=False):
    global list2
    if not page == '':
        u = module_path + '?url=' + urllib.quote_plus(url) + '&mode=' + str(mode) + '&name=' + urllib.quote_plus(name) + '&desc=' + urllib.quote_plus(desc) + '&page=' + str(page)
    else:
        u = module_path + '?url=' + urllib.quote_plus(url) + '&mode=' + str(mode) + '&name=' + urllib.quote_plus(name) + '&desc=' + urllib.quote_plus(desc) + '&page='
    if link:
        u=url
        list2.append((name,
         u,
         iconimage,
         '',
         '',
         page))
    else:
        list2.append((name,
         u,
         iconimage,
         '',
         '',
         page))

def get_params(action_param):
    param = []
    paramstring = action_param
    if paramstring is None or paramstring == '':
        paramstring = ''
    else:
        paramstring = '?' + action_param.split('?')[1]
    if len(paramstring) >= 2:
        params = paramstring
        cleanedparams = params.replace('?', '')
        if params[len(params) - 1] == '/':
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if len(splitparams) == 2:
                param[splitparams[0]] = splitparams[1]

    print 'input,output', paramstring, param
    return param

def process_mode(action_param=None):
    global list2
    try:
        
        if os.path.exists(temppath+'Downloader.log'):
            os.remove(temppath+'Downloader.log')
        list2 = []
        print 'action_param',action_param
        try:params = get_params(action_param)
        except:params={}
        url = None
        name = None
        mode = None
        page = ''
        try:
            url = urllib.unquote_plus(params['url'])
        except:
            pass

        try:
            name = urllib.unquote_plus(params['name'])
        except:
            pass

        try:
            mode = int(params['mode'])
        except:
            pass

        try:
            page = str(params['pageToken'])
        except:
            page = 1

        print 'Mode: ' + str(mode)
        print 'URL: ' + str(url)
        print 'Name: ' + str(name)
        print 'page: ' + str(page)
        if type(url) == type(str()):
            url = urllib.unquote_plus(url)
        if mode == None :           
            
            main_cats()
        elif mode == 100:
            print '' + url
            getteams(name, url, page)
        elif mode == 102:
            print '' + url
            dreamboxmodels(name, url, page)			
        elif mode == 103:
            print '' + url
            vuplusmodels(name, url, page)
        elif mode == 114:
            print '' + url
            xtrendmodels(name, url, page)
        elif mode == 116:
            print '' + url
            gigabluemodels(name, url, page)	
        elif mode == 118:
            print '' + url
            formulermodels(name, url, page)				
        elif mode==104:
            extract_dreamboximages(name,url,1)
        elif mode==105:
            extract_vuplusimages(name,url,1)
        elif mode==108:
            extract_xtrendimages(name,url,1)
        elif mode==109:
            extract_tsdreamboximages(name,url,1)
        elif mode==115:
            extract_xtrendimages(name,url,1)
        elif mode==117:
            extract_gigablueimages(name,url,1)
        elif mode==119:
            extract_formulerimages(name,url,1)			
            
    except:
        addDir('Error:script error [error 1050]', '', '', '', desc='', page='')
    print 'list2',list2
    return list2
