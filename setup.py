from setuptools import setup
import os
from subprocess import call

#call(["pip3", "install", "git+https://github.com/dpallot/simple-websocket-server.git"])
#call(["pip3", "install", "git+https://github.com/giampaolo/psutil.git"])

user = os.listdir("/home")
pth = '/home/' + user[0]

#call(["wget", "-P", pth, "https://raw.githubusercontent.com/MrYsLab/s2-pi/master/s2_pi/s2_pi.js"])

setup(
    name='s2-piptbr',
    version='1.21',
    packages=['s2_pi'],

    entry_points={
            'console_scripts': ['s2piptbr = s2_pi.s2_pi:run_server',
                                'sbx_to_sb2 = s2_pi.sbx_to_sb2:sbx_to_sb2'],
        },
    url='https://github.com/HackEduca/s2-pi',
    license='GNU General Public License v3 (GPLv3)',
    author='Alan Yorinks - changed by Edson Sidnei Sobreira',
    author_email='MisterYsLab@gmail.com - changed by hackeduca@hackeduca.com.br',
    description='Creating Scratch 2 Extensions For The Raspberry Pi',
    include_package_data=True,
    keywords=['Raspberry Pi', 'Scratch 2', 'Extensions'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4',
            'Topic :: Education',
            'Topic :: Software Development',
        ],
)