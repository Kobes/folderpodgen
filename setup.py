setup(
    name='folderpodgen',
    version='0.1',
    py_modules=['folderpodgen'],
    install_requires=[
         'Click',
         'Podgen',
         'Mutagen',
    ],
    entry_points='''
        [console_scripts]
        folderpodgen=folderpodgen:generate
    ''',
)
