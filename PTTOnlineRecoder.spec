# -*- mode: python -*-

block_cipher = None
import shutil


a = Analysis(['PTT.py'],
             pathex=['E:\\MyProjects\\PTTOnlineTracker'],
             binaries=[],
             datas=[('config.yaml', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PTTOnlineRecoder',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False , icon='app.ico')


shutil.copyfile('config.yaml', '{0}/config.yaml'.format(DISTPATH))