# -*- mode: python -*-

block_cipher = None


a = Analysis(['thaad_radar_minimum_altitude.py'],
             pathex=['C:\\Users\\alex9\\Desktop\\python'],
             binaries=[],
             datas=[],
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
          name='thaad_radar_minimum_altitude',
          debug=False,
          strip=False,
          upx=True,
          console=True )
