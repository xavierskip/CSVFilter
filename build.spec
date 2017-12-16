import gooey
cwd = os.getcwd()
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(cwd, 'resource'), prefix = 'gooey/images')

a = Analysis(['gui_csvfilter.py'],
             pathex=['c:\\Python3\\Scripts'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages, # Add them in to collected files
          gooey_images, # Same here.
          name='csvFilter',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(cwd, 'resource', 'program_icon.ico'),
          version='version.txt')