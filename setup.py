from setuptools import setup

setup(name='fcsanalysis',
      version='0.1a',
      description='FCS analysis.',
      packages=['fcsanalysis'],
      install_requires=['numpy==1.15.3',
                        'pandas==0.23.4',
                        'matplotlib==3.0.0',
                        'lmfit==0.9.11',
                        'openpyxl==2.5.9'],
      zip_safe=False)
