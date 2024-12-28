from setuptools import setup

package_name = 'fresh_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Daichi Hirose',
    maintainer_email='marumaru09030903@gmail.com',
    description='A fresh ROS 2 package',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = fresh_package.talker:main',
            'listener = fresh_package.listener:main',
        ],
    },
)

