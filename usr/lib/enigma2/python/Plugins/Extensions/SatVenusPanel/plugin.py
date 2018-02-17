from Plugins.Plugin import PluginDescriptor
from Tools.Directories import fileExists
from Tools.LoadPixmap import LoadPixmap
from Screens.Screen import Screen
from Screens.Standby import *
from Screens.Standby import TryQuitMainloop
from Tools.Directories import *
from Screens.MessageBox import MessageBox
from Components.Sources.List import List
from Components.MenuList import MenuList
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap, NumberActionMap
from Components.Label import Label
from Components.Button import Button
from Components.Sources.StaticText import StaticText
from Components.ScrollLabel import ScrollLabel
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest
from enigma import eListbox, eTimer, eListboxPythonMultiContent, gFont, RT_HALIGN_LEFT, RT_HALIGN_RIGHT, RT_HALIGN_CENTER, getDesktop, loadPNG, loadPic
from enigma import *
from enigma import eConsoleAppContainer
from radio import SatVenusScr
from image_viewer import Feeds, ScreenBox
from dmimage_viewer import dmFeeds
from backup_downloader import buFeeds
from settings import Settings_Menu
from milesettings import MileSettings_Menu
from os import listdir
import os
import sys
import re
from xml.dom import Node, minidom
from twisted.web.client import getPage
import urllib
import base64
data_xml = 'aHR0cDovLzE3OC42My4xNTYuNzUvU29mdENhbXMv'
xml_path = base64.b64decode(data_xml)
adata_xml = 'aHR0cDovLzE3OC42My4xNTYuNzUv'
axml_path = base64.b64decode(adata_xml)
DESKHEIGHT = getDesktop(0).size().height()
currversion = '7.0.0'
plugin_path = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/fonts'
skin_path = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/Skin/'
from enigma import addFont
try:
    addFont('%s/Capture_it_2.ttf' % plugin_path, 'Cap2', 100, 1)
    addFont('%s/Raleway-Black.ttf' % plugin_path, 'Rale', 100, 1)
    addFont('%s/28-Days-Later.ttf' % plugin_path, 'Days', 100, 1)
    addFont('%s/Sansation-Bold.ttf' % plugin_path, 'Sansation-Bold', 100, 1)	
except Exception as ex:
    print ex

p_path = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel'

def getversions2():
    currversion = 'oe2.0'
    enigmaos = 'oe2.0'
    currpackage = 'full'
    currbuild = '08022018'
    if os.path.exists(p_path + '/version'):
        try:
            fp = open(p_path + '/version', 'r').readlines()
            for line in fp:
                if 'version' in line:
                    currversion = line.split(':')[1].strip()
                if 'kernel' in line:
                    enigmaos = line.split(':')[1].strip()
                if 'package' in line:
                    currpackage = line.split(':')[1].strip()
                if 'build' in line:
                    currbuild = line.split(':')[1].strip()

        except:
            pass

    return (currversion,
     enigmaos,
     currpackage,
     currbuild)
	
Amenu_list = [_('|  EX-YU Lista za milenka61'),
 _('|  SatVenus Addons'),
 _('|  SatVenus BackUp Images'),
 _('|  Play SatVenus Radio'),
 _('|  Other Addons Download'),
 _('|  Image Downloader'), 
 _('|  News and Updates'),
 _('|  Panel Update'),
 _('|  About The Panel')]
ANEWmenu_list = [_('|  EX-YU Lista za milenka61'),
 _('|  SatVenus BackUp Images'),
 _('|  Play SatVenus Radio'),
 _('|  Other Addons Download'), 
 _('|  Image Downloader'), 
 _('|  News and Updates'),
 _('|  Panel Update'),
 _('|  About The Panel')] 
Bmenu_list = [_('| ==> Plugins'),
 _('| ==> Panels'),
 _('| ==> E2 Settings'),
 _('| ==> Softcams'),
 _('| ==> Picons'),
 _('| ==> Skins'),
 _('| ==> Dependencies'),
 _('| ==> Addons for oe1.6'),
 _('| ==> Addons for sh4')] 
Cmenu_list = [_('|  ARM Based Softcams'),
 _('|  NCams'),
 _('|  OSCams'),
 _('|  OSCam Emus'),
 _('|  Modern OSCam Emus'),
 _('|  GCams'),
 _('|  Other Softcams')]
Dmenu_list = [_('| ==> Plugins'),
 _('| ==> Panels'),
 _('| ==> E2 Settings'),
 _('| ==> Softcams'),
 _('| ==> Skins')]
##############
class AmenuList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        if DESKHEIGHT <= 1000:
            self.l.setItemHeight(50)
            self.l.setFont(0, gFont('Days', 48))
        else:
            self.l.setItemHeight(73)
            self.l.setFont(0, gFont('Days', 71))

def AmenuListEntry(name, idx):
    res = [name]
    if idx == 0:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 1:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 2:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 3:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 4:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 5:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 6:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 7:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 8:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'	
    if fileExists(png):
        res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 0), size=(0, 0), png=loadPNG(png)))
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res

##############
class ANEWmenuList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        if DESKHEIGHT <= 1000:
            self.l.setItemHeight(50)
            self.l.setFont(0, gFont('Days', 48))
        else:
            self.l.setItemHeight(73)
            self.l.setFont(0, gFont('Days', 71))

def ANEWmenuListEntry(name, idx):
    res = [name]
    if idx == 0:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 1:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 2:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 3:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 4:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 5:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 6:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 7:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'	
    if fileExists(png):
        res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 0), size=(0, 0), png=loadPNG(png)))
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res	
	
class BmenuList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        if DESKHEIGHT < 1000:
            self.l.setItemHeight(50)
            self.l.setFont(0, gFont('Days', 48))
        else:
            self.l.setItemHeight(76)
            self.l.setFont(0, gFont('Days', 74))

def BmenuListEntry(name, idx):
    res = [name]
    if idx == 0:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 1:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 2:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 3:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 4:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 5:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 6:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 7:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 8:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 9:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'		
    if fileExists(png):
        res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 0), size=(0, 0), png=loadPNG(png)))
        res.append(MultiContentEntryText(pos=(0, 0), size=(1000, 320), font=0, text=name))
    return res

class CmenuList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        if DESKHEIGHT <= 1000:
            self.l.setItemHeight(58)
            self.l.setFont(0, gFont('Sansation-Bold', 55))
        else:
            self.l.setItemHeight(86)
            self.l.setFont(0, gFont('Sansation-Bold', 84))

def CmenuListEntry(name, idx):
    res = [name]
    if idx == 0:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 1:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 2:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 3:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 4:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 5:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 6:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if fileExists(png):
        res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 0), size=(0, 0), png=loadPNG(png)))
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res

class DmenuList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, False, eListboxPythonMultiContent)
        if DESKHEIGHT <= 1000:
            self.l.setItemHeight(58)
            self.l.setFont(0, gFont('Sansation-Bold', 55))
        else:
            self.l.setItemHeight(86)
            self.l.setFont(0, gFont('Sansation-Bold', 84))

def DmenuListEntry(name, idx):
    res = [name]
    if idx == 0:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 1:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 2:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if idx == 3:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 4:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 5:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    elif idx == 6:
        png = '/usr/lib/enigma2/python/Plugins/Extensions/SatVenusPanel/pics/'
    if fileExists(png):
        res.append(MultiContentEntryPixmapAlphaTest(pos=(0, 0), size=(0, 0), png=loadPNG(png)))
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res
##############
class MenuA(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'menuAHD.xml'
        else:
            skin = skin_path + 'menuAFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self['text'] = AmenuList([])
        self.working = False
        self.selection = 'all'
        self['actions'] = NumberActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.updateMenuList)

    def updateMenuList(self):
        self.menu_list = []
        for x in self.menu_list:
            del self.menu_list[0]

        list = []
        idx = 0
        for x in Amenu_list:
            list.append(AmenuListEntry(x, idx))
            self.menu_list.append(x)
            idx += 1

        self['text'].setList(list)

    def okClicked(self):
        self.keyNumberGlobal(self['text'].getSelectedIndex())

    def keyNumberGlobal(self, idx):
        sel = self.menu_list[idx]
        if sel == _('|  Other Addons Download'):
			self.session.open(MenuB)
        elif sel == _('|  EX-YU Lista za milenka61'):
            self.session.open(MileSettings_Menu)
        elif sel == _('|  SatVenus Addons'):
		    self.session.open(SatVenus)
        elif sel == _('|  SatVenus BackUp Images'):	
			self.session.open(buFeeds)
        elif sel == _('|  About The Panel'):
            self.session.open(Infoo)
        elif sel == _('|  Play SatVenus Radio'):
            self.session.open(SatVenusScr)
        elif sel == _('|  News and Updates'):
            self.session.open(NewsCheck)
        elif sel == _('|  Panel Update'):	
			self.session.open(Update)
        elif sel == _('|  Image Downloader'):
            self.session.open(Feeds)			
##############
class MenuNEWA(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'menuAHD.xml'
        else:
            skin = skin_path + 'menuAFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self['text'] = ANEWmenuList([])
        self.working = False
        self.selection = 'all'
        self['actions'] = NumberActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.updateMenuList)

    def updateMenuList(self):
        self.menu_list = []
        for x in self.menu_list:
            del self.menu_list[0]

        list = []
        idx = 0
        for x in ANEWmenu_list:
            list.append(ANEWmenuListEntry(x, idx))
            self.menu_list.append(x)
            idx += 1

        self['text'].setList(list)

    def okClicked(self):
        self.keyNumberGlobal(self['text'].getSelectedIndex())

    def keyNumberGlobal(self, idx):
        sel = self.menu_list[idx]
        if sel == _('|  EX-YU Lista za milenka61'):
            self.session.open(MileSettings_Menu)
        elif sel == _('|  SatVenus BackUp Images'):
            self.session.open(buFeeds)
        elif sel == _('|  About The Panel'):
            self.session.open(Infoo)
        elif sel == _('|  Play SatVenus Radio'):
            self.session.open(SatVenusScr)
        elif sel == _('|  News and Updates'):
            self.session.open(NewsCheckDEB)
        elif sel == _('|  Panel Update'):
            self.session.open(UpdateDEB)
        elif sel == _('|  Image Downloader'):
            self.session.open(dmFeeds)
        elif sel == _('|  Other Addons Download'):
			self.session.open(MenuD)				   
				   
class MenuB(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'menuBHD.xml'
        else:
            skin = skin_path + 'menuBFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self['text'] = BmenuList([])
        self.working = False
        self.selection = 'all'
        self['actions'] = NumberActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.updateMenuList)

    def updateMenuList(self):
        self.menu_list = []
        for x in self.menu_list:
            del self.menu_list[0]

        list = []
        idx = 0
        for x in Bmenu_list:
            list.append(BmenuListEntry(x, idx))
            self.menu_list.append(x)
            idx += 1

        self['text'].setList(list)

    def okClicked(self):
        self.keyNumberGlobal(self['text'].getSelectedIndex())

    def keyNumberGlobal(self, idx):
        sel = self.menu_list[idx]
        if sel == _('| ==> Plugins'):
            self.session.open(Pluginss)
        elif sel == _('| ==> Panels'):
            self.session.open(Panels)
        elif sel == _('| ==> E2 Settings'):
            self.session.open(Settings_Menu)
        elif sel == _('| ==> Softcams'):
            self.session.open(MenuC)
        elif sel == _('| ==> Picons'):
            self.session.open(Picons)
        elif sel == _('| ==> Skins'):
            self.session.open(Skins)
        elif sel == _('| ==> Dependencies'):
            self.session.open(Dependencies)
        elif sel == _('| ==> Addons for sh4'):
            self.session.open(sh4)
        elif sel == _('| ==> Addons for oe1.6'):
            self.session.open(Oeenasest)	

class MenuC(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'menuCHD.xml'
        else:
            skin = skin_path + 'menuCFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self['text'] = CmenuList([])
        self.working = False
        self.selection = 'all'
        self['actions'] = NumberActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.updateMenuList)

    def updateMenuList(self):
        self.menu_list = []
        for x in self.menu_list:
            del self.menu_list[0]

        list = []
        idx = 0
        for x in Cmenu_list:
            list.append(CmenuListEntry(x, idx))
            self.menu_list.append(x)
            idx += 1

        self['text'].setList(list)

    def okClicked(self):
        self.keyNumberGlobal(self['text'].getSelectedIndex())

    def keyNumberGlobal(self, idx):
        sel = self.menu_list[idx]
        if sel == _('|  ARM Based Softcams'):
            self.session.open(arm)
        elif sel == _('|  NCams'):
            self.session.open(ncam)
        elif sel == _('|  OSCams'):
            self.session.open(oscam)
        elif sel == _('|  OSCam Emus'):
            self.session.open(emus)
        elif sel == _('|  Modern OSCam Emus'):
            self.session.open(modern)
        elif sel == _('|  GCams'):
            self.session.open(gcam)
        elif sel == _('|  Other Softcams'):
            self.session.open(other_soft)

class MenuD(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'menuBHD.xml'
        else:
            skin = skin_path + 'menuBFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self['text'] = DmenuList([])
        self.working = False
        self.selection = 'all'
        self['actions'] = NumberActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -1)
        self.onLayoutFinish.append(self.updateMenuList)

    def updateMenuList(self):
        self.menu_list = []
        for x in self.menu_list:
            del self.menu_list[0]

        list = []
        idx = 0
        for x in Dmenu_list:
            list.append(DmenuListEntry(x, idx))
            self.menu_list.append(x)
            idx += 1

        self['text'].setList(list)

    def okClicked(self):
        self.keyNumberGlobal(self['text'].getSelectedIndex())

    def keyNumberGlobal(self, idx):
        sel = self.menu_list[idx]
        if sel == _('| ==> Plugins'):
            self.session.open(PluginssDeb)
        elif sel == _('| ==> Panels'):
            self.session.open(PanelsDeb)
        elif sel == _('| ==> E2 Settings'):
            self.session.open(Settings_Menu)
        elif sel == _('| ==> Softcams'):
            self.session.open(SoftcamsDeb)
        elif sel == _('| ==> Skins'):
            self.session.open(SkinsDeb)
##############
class PluginssDeb(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'PluginssDEB.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In PluginssDEB data =', data
        self.xml = data
        try:
            print 'In PluginssDEB self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In PluginssDEB match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(InstallDeb, self.xml, name)
            except:
                return

        else:
            self.close

class PanelsDeb(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'PanelsDEB.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In PanelsDEB data =', data
        self.xml = data
        try:
            print 'In PanelsDEB self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In PanelsDEB match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(InstallDeb, self.xml, name)
            except:
                return

        else:
            self.close

class SkinsDeb(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'SkinsDEB.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In SkinsDEB data =', data
        self.xml = data
        try:
            print 'In SkinsDEB self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In SkinsDEB match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(InstallDeb, self.xml, name)
            except:
                return

        else:
            self.close

class SoftcamsDeb(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'SoftcamsDEB.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In SoftcamsDEB data =', data
        self.xml = data
        try:
            print 'In SoftcamsDEB self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In SoftcamsDEB match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(InstallDeb, self.xml, name)
            except:
                return

        else:
            self.close
##############	
class InstallDeb(Screen):

    def __init__(self, session, data, name, selection = None):
        self.session = session
        print "In InstallDeb data =", data
        print "In InstallDeb name =", name
        if DESKHEIGHT < 1000:		
            skin = skin_path + 'allHD.xml'
        else:	
            skin = skin_path + 'allFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.selection = selection        
        list = []
        list.sort()				
        n1 = data.find(name, 0)
        n2 = data.find("</plugins>", n1)
        data1 = data[n1:n2]
        print "In InstallDeb data1 =", data1
        self.names = []
        self.urls = []
        regex = '<plugin name="(.*?)".*?url>"(.*?)"'		
        match = re.compile(regex,re.DOTALL).findall(data1)
        print "In InstallDeb match =", match
        for name, url in match:
                self.names.append(name)
                self.urls.append(url)				
        print "In InstallDeb self.names =", self.names
        self['text'] = OtherList([])
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.selclicked,
         'cancel': self.close}, -2)
        self.onLayoutFinish.append(self.start)
        
    def start(self):	
        showlist(self.names, self['text'])

    def selclickedX(self):
        try:
            selection_country = self['text'].getCurrent()
        except:
            return

        for plugins in self.xmlparse.getElementsByTagName('plugins'):
            if str(plugins.getAttribute('cont').encode('utf8')) == self.selection:
                for plugin in plugins.getElementsByTagName('plugin'):
                    if plugin.getAttribute('name').encode('utf8') == selection_country:
                        urlserver = str(plugin.getElementsByTagName('url')[0].childNodes[0].data)
                        pluginname = plugin.getAttribute('name').encode('utf8')
                        self.prombt(urlserver, pluginname)		

    def selclicked(self):
        idx = self['text'].getSelectionIndex()
        dom = self.names[idx]
        com = self.urls[idx]
        self.prombt(com, dom)

    def prombt(self, com, dom):
        self.com = com
        self.dom = dom
        self.timer = eTimer()
        self.timer.start(100, True)
        try:
            self.timer.callback.append(self.deletetmp)
        except:
            self.timer_conn = self.timer.timeout.connect(self.deletetmp)		
#        cmd = 'wget -q -O /tmp/tmp.deb %s ; dpkg --install --force-depends --force-overwrite /tmp/tmp.deb; apt-get -f -y install' % str(com)
        cmd = 'wget -q -O /tmp/tmp.deb %s ; dpkg --install --force-overwrite /tmp/tmp.deb' % str(com)
        self.session.open(ConsoleDeb, _('Downloading-installing: %s') % dom, [cmd])	

    def deletetmp(self):
        os.system('rm -f /tmp/down.deb')
		
class ConsoleDeb(Screen):

    def __init__(self, session, title = "Console", cmdlist = None, finishedCallback = None, closeOnSuccess = False):
        self.session = session
        if DESKHEIGHT < 1000:		
            skin = skin_path + 'konzHD.xml'
        else:	
            skin = skin_path + 'konzFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self["text"] = ScrollLabel("")
        self["actions"] = ActionMap(["WizardActions", "DirectionActions"], 
        {
			"ok": self.cancel,
			"back": self.cancel,
			"up": self["text"].pageUp,
			"down": self["text"].pageDown
        }, -1)
		
        self.cmdlist = cmdlist
        self.newtitle = title
		
        self.onShown.append(self.updateTitle)
		
        self.container = eConsoleAppContainer()
        self.run = 0
        self.appClosed_conn = self.container.appClosed.connect(self.runFinished)
        self.dataAvail_conn = self.container.dataAvail.connect(self.dataAvail)
        self.onLayoutFinish.append(self.startRun) # dont start before gui is finished

    def updateTitle(self):
		self.setTitle(self.newtitle)

    def startRun(self):
		self["text"].setText(_("Execution Progress:") + "\n\n")
		print "Console: executing in run", self.run, " the command:", self.cmdlist[self.run]
		if self.container.execute(self.cmdlist[self.run]): #start of container application failed...
			self.runFinished(-1) # so we must call runFinished manual

    def runFinished(self, retval):
		self.run += 1
		if self.run != len(self.cmdlist):
			if self.container.execute(self.cmdlist[self.run]): #start of container application failed...
				self.runFinished(-1) # so we must call runFinished manual
		else:
			str = self["text"].getText()
			str += _("Execution finished!!");
			self["text"].setText(str)
			self["text"].lastPage()
			if self.finishedCallback is not None:
				self.finishedCallback()
			if not retval and self.closeOnSuccess:
				self.cancel()	

    def cancel(self):
		if self.run == len(self.cmdlist):
			self.close()
			self.appClosed_conn = None
			self.dataAvail_conn = None

    def dataAvail(self, str):
		self["text"].setText(self["text"].getText() + str)

class NewsCheckDEB(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'infoHD.xml'
        else:
            skin = skin_path + 'infoFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
         'ok': self.close,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown,
         'cancel': self.close,
         'left': self['text'].pageUp}, -1)
        try:
            fp = urllib.urlopen(axml_path + 'novostiDEB.txt')
            count = 0
            self.labeltext = ''
            while True:
                s = fp.readline()
                count = count + 1
                self.labeltext = self.labeltext + str(s)
                if s:
                    continue
                else:
                    break
                    continue

            fp.close()
            self['text'].setText(self.labeltext)
        except:
            self['text'].setText('Unable to download...')
		
class UpdateDEB(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'upHD.xml'
        else:
            skin = skin_path + 'upFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['key_red'] = Button(_('Exit'))
        self['key_yellow'] = Button(_('Update'))			
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.close,
         'cancel': self.close,
         'red': self.close,
         'yellow': self.runupdate}, -1)
        try:
            fp = urllib.urlopen(axml_path + 'SvPverzijaAUTO/verzijaAUTOdeb.txt')
            count = 0
            self.labeltext = ''
            s1 = fp.readline()
            s2 = fp.readline()
            s3 = fp.readline()
            s1 = s1.strip()
            s2 = s2.strip()
            s3 = s3.strip()
            self.link = s2
            self.version = s1
            self.info = s3
            fp.close()
            cstr = s1 + ' ' + s2
            if s1 == currversion:
                self['text'].setText('SatVenus Panel version: ' + currversion + '\n\nNo updates available!')
                self.update = False
            else:
                updatestr = '\nSatVenus Panel version: ' + currversion + '\n\nNew update ' + s1 + ' is available!  \n\nUpdates:' + self.info + '\n\n\n\nPress yellow button to start updating'
                self.update = True
                self['text'].setText(updatestr)
        except:
            self.update = False
            self['text'].setText('Unable to check for updates\n\nNo internet connection or server down\n\nPlease check later')

    def runupdate(self):
        if self.update == False:
            return
        com = self.link
        dom = 'Updating plugin to ' + self.version		
        cmd = 'wget -q -O /tmp/tmp.deb %s ; dpkg --install --force-overwrite /tmp/tmp.deb' % str(com)
        self.session.open(ConsoleDeb, _('Downloading-installing: %s') % dom, [cmd])		
##############		
class arm(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'Arm_Based.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class ncam(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'NCams.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class oscam(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'OSCams.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class emus(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'OSCam_Emus.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class modern(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'Modern_OSCam.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class gcam(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'GCams.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class other_soft(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = xml_path + 'Other_Soft.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close
##############			
class FirstList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, True, eListboxPythonMultiContent)
        if DESKHEIGHT < 1000:
            self.l.setItemHeight(36)
            textfont = int(30)
        else:
            self.l.setItemHeight(55)
            textfont = int(47)
        self.l.setFont(0, gFont('Rale', textfont))

def FirstListEntry(name):
    res = [name]
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res

def showlist(data, list):
    icount = 0
    plist = []
    for line in data:
        name = data[icount]
        plist.append(FirstListEntry(name))
        icount = icount + 1
        list.setList(plist)

class OtherList(MenuList):

    def __init__(self, list):
        MenuList.__init__(self, list, True, eListboxPythonMultiContent)
        if DESKHEIGHT < 1000:
            self.l.setItemHeight(37)
            textfont = int(24)
        else:
            self.l.setItemHeight(50)
            textfont = int(34)
        self.l.setFont(0, gFont('Rale', textfont))

def OtherListEntry(name):
    res = [name]
    res.append(MultiContentEntryText(pos=(5, 0), size=(1000, 320), font=0, text=name))
    return res

def lastlist(data, list):
    icount = 0
    plist = []
    for line in data:
        name = data[icount]
        plist.append(OtherListEntry(name))
        icount = icount + 1
        list.setList(plist)

##############
class Pluginss(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'Pluginss.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Dependencies(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'dependencies.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Pluginss data =', data
        self.xml = data
        try:
            print 'In Pluginss self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Pluginss match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Panels(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'Panels.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Panels data =', data
        self.xml = data
        try:
            print 'In Panels self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Panels match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Others(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'OtherE2Settings.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Others data =', data
        self.xml = data
        try:
            print 'In Others self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Others match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Oeenasest(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'Oeenasest.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Oeenasest data =', data
        self.xml = data
        try:
            print 'In Oeenasest self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Oeenasest match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Picons(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'Picons.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Picons data =', data
        self.xml = data
        try:
            print 'In Picons self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Picons match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(InstallPicons, self.xml, name)
            except:
                return

        else:
            self.close

class Skins(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'Skins.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In Skins data =', data
        self.xml = data
        try:
            print 'In Skins self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In Skins match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class sh4(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def downloadxmlpage(self):
        url = axml_path + 'sh4.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def _gotPageLoad(self, data):
        print 'In sh4 data =', data
        self.xml = data
        try:
            print 'In sh4 self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In sh4 match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close
##############			
class Installall(Screen):

    def __init__(self, session, data, name):
        self.session = session
        print 'In Installall data =', data
        print 'In Installall name =', name
        if DESKHEIGHT < 1000:
            skin = skin_path + 'allHD.xml'
        else:
            skin = skin_path + 'allFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        list = []
        list.sort()
        n1 = data.find(name, 0)
        n2 = data.find('</plugins>', n1)
        data1 = data[n1:n2]
        print 'In Installall data1 =', data1
        self.names = []
        self.urls = []	
        regex = '<plugin name="(.*?)".*?url>"(.*?)"'
        match = re.compile(regex, re.DOTALL).findall(data1)
        print 'In Installall match =', match
        for name, url in match:
            self.names.append(name)
            self.urls.append(url)

        print 'In Installall self.names =', self.names
        self['text'] = OtherList([])
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.selclicked,
         'cancel': self.close}, -2)
        self.onLayoutFinish.append(self.start)

    def start(self):
        showlist(self.names, self['text'])

    def selclickedX(self):
        try:
            selection_country = self['text'].getCurrent()
        except:
            return

        for plugins in self.xmlparse.getElementsByTagName('plugins'):
            if str(plugins.getAttribute('cont').encode('utf8')) == self.selection:
                for plugin in plugins.getElementsByTagName('plugin'):
                    if plugin.getAttribute('name').encode('utf8') == selection_country:
                        urlserver = str(plugin.getElementsByTagName('url')[0].childNodes[0].data)
                        pluginname = plugin.getAttribute('name').encode('utf8')
                        self.prombt(urlserver, pluginname)

    def selclicked(self):
        idx = self['text'].getSelectionIndex()
        dom = self.names[idx]
        com = self.urls[idx]
        self.prombt(com, dom)

    def prombt(self, com, dom):
        self.com = com
        self.dom = dom	
        self.session.open(Konzola, _('downloading-installing: %s') % dom, ['opkg install -force-overwrite -force-depends %s' % com])

class InstallPicons(Screen):

    def __init__(self, session, data, name):
        self.session = session
        print 'In InstallPicons data =', data
        print 'In InstallPicons name =', name
        if DESKHEIGHT < 1000:
            skin = skin_path + 'piconHD.xml'
        else:
            skin = skin_path + 'piconFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        list = []
        list.sort()
        n1 = data.find(name, 0)
        n2 = data.find('</plugins>', n1)
        data1 = data[n1:n2]
        print 'In InstallPicons data1 =', data1
        self.names = []
        self.urls = []
        regex = '<plugin name="(.*?)".*?url>"(.*?)"'
        match = re.compile(regex, re.DOTALL).findall(data1)
        print 'In InstallPicons match =', match
        for name, url in match:
            self.names.append(name)
            self.urls.append(url)

        print 'In InstallPicons self.names =', self.names
        self['text'] = OtherList([])
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.selclicked,
         'cancel': self.close}, -2)
        self.onLayoutFinish.append(self.start)

    def start(self):
        lastlist(self.names, self['text'])

    def selclickedX(self):
        try:
            selection_country = self['text'].getCurrent()
        except:
            return

        for plugins in self.xmlparse.getElementsByTagName('plugins'):
            if str(plugins.getAttribute('cont').encode('utf8')) == self.selection:
                for plugin in plugins.getElementsByTagName('plugin'):
                    if plugin.getAttribute('name').encode('utf8') == selection_country:
                        urlserver = str(plugin.getElementsByTagName('url')[0].childNodes[0].data)
                        pluginname = plugin.getAttribute('name').encode('utf8')
                        self.prombt(urlserver, pluginname)

    def selclicked(self):
        idx = self['text'].getSelectionIndex()
        dom = self.names[idx]
        com = self.urls[idx]
        self.prombt(com, dom)

    def prombt(self, com, dom):
        self.com = com
        self.dom = dom
        self.session.open(Konzola, _('downloading-installing: %s') % dom, ['opkg install -force-overwrite -force-depends %s' % com])
##############
class Konzola(Screen):

    def __init__(self, session, title = 'Konzola', cmdlist = None, finishedCallback = None, closeOnSuccess = False):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'konzHD.xml'
        else:
            skin = skin_path + 'konzFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.finishedCallback = finishedCallback
        self.closeOnSuccess = closeOnSuccess
        self['text'] = ScrollLabel('')
        self['actions'] = ActionMap(['WizardActions', 'DirectionActions'], {'ok': self.cancel,
         'back': self.cancel,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown}, -1)
        self.cmdlist = cmdlist
        self.newtitle = title		
        self.onShown.append(self.updateTitle)
        self.container = eConsoleAppContainer()
        self.run = 0
        self.container.appClosed.append(self.runFinished)
        self.container.dataAvail.append(self.dataAvail)
        self.onLayoutFinish.append(self.startRun)

    def updateTitle(self):
        self.setTitle(self.newtitle)

    def startRun(self):
        self['text'].setText(_('Execution Progress:') + '\n\n')
        print 'Console: executing in run', self.run, ' the command:', self.cmdlist[self.run]
        if self.container.execute(self.cmdlist[self.run]):
            self.runFinished(-1)

    def runFinished(self, retval):
        self.run += 1
        if self.run != len(self.cmdlist):
            if self.container.execute(self.cmdlist[self.run]):
                self.runFinished(-1)
        else:
            str = self['text'].getText()
            str += _('Execution finished!!')
            self['text'].setText(str)
            self['text'].lastPage()
            if self.finishedCallback is not None:
                self.finishedCallback()
            if not retval and self.closeOnSuccess:
                self.cancel()
        return

    def cancel(self):
        if self.run == len(self.cmdlist):
            self.close()
            self.container.appClosed.remove(self.runFinished)
            self.container.dataAvail.remove(self.dataAvail)

    def dataAvail(self, str):
        self['text'].setText(self['text'].getText() + str)
##############
class SatVenus(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'pluginsHD.xml'
        else:
            skin = skin_path + 'pluginsFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        self.list = []
        self['text'] = FirstList([])
        self.addon = 'emu'
        self.icount = 0
        self['info'] = Label(_('Getting the list, please wait ...'))
        self.downloading = False
        self.onLayoutFinish.append(self.downloadxmlpage)
        self['actions'] = ActionMap(['SetupActions', 'ColorActions'], {'ok': self.okClicked,
         'cancel': self.close}, -2)

    def checkupdate(self):
        self.session.open(Update)

    def downloadxmlpage(self):
        url = axml_path + 'panelupdater2.xml'
        getPage(url).addCallback(self._gotPageLoad).addErrback(self.errorLoad)

    def errorLoad(self, error):
        print str(error)
        self['info'].setText('Try again later ...')
        self.downloading = False

    def shownews(self):
        self.session.open(NewsCheck)

    def _gotPageLoad(self, data):
        print 'In SatVenus data =', data
        self.xml = data
        try:
            print 'In SatVenus self.xml =', self.xml
            regex = '<plugins cont="(.*?)"'
            match = re.compile(regex, re.DOTALL).findall(self.xml)
            print 'In SatVenus match =', match
            for name in match:
                self.list.append(name)
                self['info'].setText('Please select ...')

            showlist(self.list, self['text'])
            self.downloading = True
        except:
            self.downloading = False

    def okClicked(self):
        if self.downloading == True:
            try:
                selection = str(self['text'].getCurrent())
                idx = self['text'].getSelectionIndex()
                name = self.list[idx]
                self.session.open(Installall, self.xml, name)
            except:
                return

        else:
            self.close

class Update(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'upHD.xml'
        else:
            skin = skin_path + 'upFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['key_red'] = Button(_('Exit'))
        self['key_yellow'] = Button(_('Update'))
        self['text'] = Label()
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions', 'ColorActions'], {'ok': self.close,
         'cancel': self.close,
         'red': self.close,
         'yellow': self.runupdate}, -1)
        try:
            fp = urllib.urlopen(axml_path + 'SvPverzijaAUTO/verzijaAUTO.txt')
            count = 0
            self.labeltext = ''
            s1 = fp.readline()
            s2 = fp.readline()
            s3 = fp.readline()
            s1 = s1.strip()
            s2 = s2.strip()
            s3 = s3.strip()
            self.link = s2
            self.version = s1
            self.info = s3
            fp.close()
            cstr = s1 + ' ' + s2
            if s1 == currversion:
                self['text'].setText('SatVenus Panel version: ' + currversion + '\n\nNo updates available!')
                self.update = False
            else:
                updatestr = '\nSatVenus Panel version: ' + currversion + '\n\nNew update ' + s1 + ' is available!  \n\nUpdates:' + self.info + '\n\n\n\nPress yellow button to start updating'
                self.update = True
                self['text'].setText(updatestr)
        except:
            self.update = False
            self['text'].setText('Unable to check for updates\n\nNo internet connection or server down\n\nPlease check later')

    def runupdate(self):
        if self.update == False:
            return
        com = self.link
        dom = 'Updating plugin to ' + self.version
        self.session.open(Konzola, _('downloading-installing: %s') % dom, ['opkg install -force-overwrite %s' % com])

class NewsCheck(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'infoHD.xml'
        else:
            skin = skin_path + 'infoFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['text'] = ScrollLabel(info)
        self['actions'] = ActionMap(['SetupActions', 'DirectionActions'], {'right': self['text'].pageDown,
         'ok': self.close,
         'up': self['text'].pageUp,
         'down': self['text'].pageDown,
         'cancel': self.close,
         'left': self['text'].pageUp}, -1)
        try:
            fp = urllib.urlopen(axml_path + 'novosti.txt')
            count = 0
            self.labeltext = ''
            while True:
                s = fp.readline()
                count = count + 1
                self.labeltext = self.labeltext + str(s)
                if s:
                    continue
                else:
                    break
                    continue

            fp.close()
            self['text'].setText(self.labeltext)
        except:
            self['text'].setText('Unable to download...')

class Infoo(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'aboutHD.xml'
        else:
            skin = skin_path + 'aboutFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)
        info = ''
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.close,
         'cancel': self.close}, -1)

class BootlogoScr(Screen):

    def __init__(self, session):
        self.session = session
        if DESKHEIGHT < 1000:
            skin = skin_path + 'bootHD.xml'
        else:
            skin = skin_path + 'bootFHD.xml'
        f = open(skin, 'r')
        self.skin = f.read()
        f.close()
        Screen.__init__(self, session)		
        self['actions'] = ActionMap(['SetupActions'], {'ok': self.okClicked,
         'cancel': self.okClicked}, -1)
        self.timer2 = eTimer()
        self.timer2.start(5, True)

    def okClicked(self):
        currversion, enigmaos, currpackage, currbuild = getversions2()	
        if enigmaos == 'oe2.0':	
		     self.session.openWithCallback(self.close, MenuA)
        else:
            self.session.openWithCallback(self.close, MenuNEWA)		

    def exit(self):
        currversion, enigmaos, currpackage, currbuild = getversions2()
        if enigmaos == 'oe2.0':	
		     self.session.openWithCallback(self.close, MenuA)
        else:
            self.session.openWithCallback(self.close, MenuNEWA)
##############
def main(session, **kwargs):
    session.open(BootlogoScr)

def menu(menuid, **kwargs):
    if menuid == 'mainmenu':
        return [(_('SatVenus Panel'),
          main,
          'SatVenus Panel',
          44)]
    return []

def Plugins(**kwargs):
    list = []
    list.append(PluginDescriptor(icon='pics/addons.png', name='SatVenus Panel', description='Addons for your Image!', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main))
    list.append(PluginDescriptor(icon='pics/addons.png', name='SatVenus Panel', description='Addons for your Image!', where=PluginDescriptor.WHERE_MENU, fnc=menu))
    return list