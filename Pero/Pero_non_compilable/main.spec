# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('UI/font/*','UI/font'), ('UI/MainMenu/elements/*.png', 'UI/MainMenu/elements'), ('UI/RulesWindow/elements/*.png', 'UI/RulesWindow/elements'),
    ('UI/DifficultyWindow/elements/*.png', 'UI/DifficultyWindow/elements'), ('UI/LevelSwitcher/elements/*.png', 'UI/LevelSwitcher/elements')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
    a.binaries,
    a.zipfiles,
    a.datas,
    a.scripts,
    [],
    name='Обведи не отрывая пера',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
