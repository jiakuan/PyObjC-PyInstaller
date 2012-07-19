# -*- mode: python -*-
a = Analysis(['/Users/rdsears/PycharmProjects/OSX_Monty/Gather_info.py'],
             pathex=['/Users/rdsears/Coding/PyObjC-PyInstaller/pyinstaller'],
             hiddenimports=[],
             hookspath=None)
a.datas += [
                ('bridge/AddressBook.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/AddressBook/PyObjC.bridgesupport','DATA'),
                ('bridge/AppKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/AppKit/PyObjC.bridgesupport','DATA'),
                ('bridge/AppleScriptKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/AppleScriptKit/PyObjC.bridgesupport','DATA'),
                ('bridge/Automator.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Automator/PyObjC.bridgesupport','DATA'),
                ('bridge/CalendarStore.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/CalendarStore/PyObjC.bridgesupport','DATA'),
                ('bridge/CFNetwork.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/CFNetwork/PyObjC.bridgesupport','DATA'),
                ('bridge/Collaboration.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Collaboration/PyObjC.bridgesupport','DATA'),
                ('bridge/CoreData.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/CoreData/PyObjC.bridgesupport','DATA'),
                ('bridge/CoreFoundation.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/CoreFoundation/PyObjC.bridgesupport','DATA'),
                ('bridge/CoreText.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/CoreText/PyObjC.bridgesupport','DATA'),
                ('bridge/DictionaryServices.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/DictionaryServices/PyObjC.bridgesupport','DATA'),
                ('bridge/ExceptionHandling.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/ExceptionHandling/PyObjC.bridgesupport','DATA'),
                ('bridge/Foundation.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Foundation/PyObjC.bridgesupport','DATA'),
                ('bridge/FSEvents.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/FSEvents/PyObjC.bridgesupport','DATA'),
                ('bridge/InputMethodKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/InputMethodKit/PyObjC.bridgesupport','DATA'),
                ('bridge/InstallerPlugins.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/InstallerPlugins/PyObjC.bridgesupport','DATA'),
                ('bridge/InstantMessage.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/InstantMessage/PyObjC.bridgesupport','DATA'),
                ('bridge/InterfaceBuilderKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/InterfaceBuilderKit/PyObjC.bridgesupport','DATA'),
                ('bridge/JavaScriptCore.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/JavaScriptCore/PyObjC.bridgesupport','DATA'),
                ('bridge/LatentSemanticMapping.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/LatentSemanticMapping/PyObjC.bridgesupport','DATA'),
                ('bridge/LaunchServices.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/LaunchServices/PyObjC.bridgesupport','DATA'),
                ('bridge/Message.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Message/PyObjC.bridgesupport','DATA'),
                ('bridge/PreferencePanes.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/PreferencePanes/PyObjC.bridgesupport','DATA'),
                ('bridge/PubSub.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/PubSub/PyObjC.bridgesupport','DATA'),
                ('bridge/QTKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/QTKit/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.CoreGraphics.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/CoreGraphics/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.CoreVideo.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/CoreVideo/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.ImageIO.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/ImageIO/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.ImageKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/ImageKit/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.PDFKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/PDFKit/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.QuartzComposer.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/QuartzComposer/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.QuartzCore.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/QuartzCore/PyObjC.bridgesupport','DATA'),
                ('bridge/Quartz.QuartzFilters.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/Quartz/QuartzFilters/PyObjC.bridgesupport','DATA'),
                ('bridge/ScreenSaver.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/ScreenSaver/PyObjC.bridgesupport','DATA'),
                ('bridge/ScriptingBridge.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/ScriptingBridge/PyObjC.bridgesupport','DATA'),
                ('bridge/SearchKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/SearchKit/PyObjC.bridgesupport','DATA'),
                ('bridge/SyncServices.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/SyncServices/PyObjC.bridgesupport','DATA'),
                ('bridge/SystemConfiguration.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/SystemConfiguration/PyObjC.bridgesupport','DATA'),
                ('bridge/WebKit.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/WebKit/PyObjC.bridgesupport','DATA'),
                ('bridge/XgridFoundation.PyObjC.bridgesupport','/System/Library/Frameworks/Python.framework/Versions/Current/Extras/lib/python/PyObjC/XgridFoundation/PyObjC.bridgesupport','DATA'),
           ]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'Gather_info'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
