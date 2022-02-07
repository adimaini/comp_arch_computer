# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['GUI.py','C:\\Users\\will9\\OneDrive\\Desktop\\simulator\\utils\\binaryUtils.py','C:\\Users\\will9\\OneDrive\\Desktop\\simulator\\memory\\memory.py'],
             pathex=['C:\\Users\\will9\\OneDrive\\Desktop\\simulator'],
             binaries=[],
             datas=[('logging.ini', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
    #py_modules=['memory', 'utils']d

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='GUI')