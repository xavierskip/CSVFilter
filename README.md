warning：just read GBK encode CSV file if the with other unASCII chart.

基于 Python3  
图形界面需要 Gooey  
可执行文件打包需要 PyInstaller

### PyInstaller 打包命令

`pyinstaller build.spec`

### 在Windows下用PyInstaller打包

在中文windows系统上需要在修改Gooey库文件来转换字符编码[issue:Non-ASCII output can't show in display panel on windows system with chinese language](https://github.com/chriskiehl/Gooey/issues/230)

例如：`gooey\gui\windows\runtime_display_panel`第51行加上`txt = txt.decode(gbk)`

如果通过修改stdout来完成字符编码的转换则无法在窗口模式下打包。

如果你打包的程序需要在Windows XP下运行，则需要PyInstaller version <= 3.2.1，因为PyInstaller 3.3不支持Windows XP。

当你使用3.2.1版本进行打包时需要注意的是，如果你之前用3.3版本执行过打包，需要清空之前生成的build文件夹内容，否则无法完成打包。

删除之前安装的PyInstaller
`pipuninstall PyInstaller` 

安装3.2.1版本
`pip install PyInstaller==3.2.1`

### Issues

* __Windows xp下打包version file出错__
    
(winXP-32位,python3.4,PyInstaller v3.2.1,UPX 3.94)

解决办法：

因为PyInstaller v3.2.1添加version file的相关代码的py3兼容性的问题，所以我们需要手动修改相关代码。

找到3.3版本的PyInstaller，替换3.2.1版本的`PyInstaller/utils/win32/versioninfo.py`文件。

然后修改第15行

    from ...compat import is_py3, win32api
    
修改为

    import win32api
    from ...compat import is_py3
    
然后又发现了3.2.1版本下的`pyi-grab_version`兼容性问题。

修改`PyInstaller\utils\cliutils\grab_version`文件

    15:- PyInstaller.log
    15:+ from PyInstaller import log
    19:- PyInstaller.log.init()
    19:+ log.init()
    39:- fp.write(unicode(vs))
    39:+ fp.write(u"%s" % (vs,))   

* __Windows 7下打包使用UPX出错__

(win7-32位,python3.6-32位,PyInstaller v3.3,UPX 3.94)

    PyInstaller\loader\pyimod03_importers.py", line 714, in load_module
        module = loader.load_module(fullname)
    ImportError: DLL load failed: 内存位置访问无效。

* __Windows 10下打包和Windows 7有一样的问题__