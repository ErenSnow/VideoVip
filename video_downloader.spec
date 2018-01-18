# -*- mode: python -*-
a = Analysis(['video_downloader.py'],
             pathex=['E:\\ErenGit\\video_downloader'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='video_downloader.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
