from setuptools import find_packages, setup
import os                     # ★追加：OSの機能を使う
from glob import glob         # ★追加：ファイルをまとめて探す機能

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')), # ★重要：これを書かないとLaunchファイルが認識されません！
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryougasan21',
    maintainer_email='s24c1136ww@s.chibakoudai.jp',
    description='Degree to Radian converter package',
    license='GPL-3.0-only',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
            ],
    },
)
