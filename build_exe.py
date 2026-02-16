import PyInstaller.__main__

if __name__ == '__main__':
    args = [
        'src/regutility/app.py',
        '--name=ScriptForge',
        '--onefile',
        '--noconsole',
        '--clean',
        '--paths=src',
        '--add-data=src/regutility/assets;regutility/assets',
        '--icon=src/regutility/assets/anvil.ico',
    ]

    print('Building ScriptForge...')
    PyInstaller.__main__.run(args)
    print('Build complete. detailed logs above.')