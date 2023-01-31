from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(
    name='ghinks-test-pub',
    version='0.1.0',
    description='test publication from tutorial to learn how to publish',
    package_dir={'': 'src'},
    author='ghinks',
    author_email='ghinks@yahoo.com',
    long_description=open('README.md').read() ,
    long_description_content_type="text/markdown",
    url='https://github.com/ghinks/Your-First-Python-Package-on-PyPI.git',
    include_package_data=True
)
