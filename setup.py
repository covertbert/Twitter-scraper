from setuptools import setup

setup(name='Tweet Scraper',
      version='0.1',
      description='Writes tweets containing given data to csv file',
      url='https://github.com/covertbert/ISS-next-pass',
      author='Bertie Blackman',
      author_email='blackmanrgh@gmail.com',
      license='MIT',
      install_requires=[
          'python-env',
          'tweepy'
      ],
      zip_safe=False)
