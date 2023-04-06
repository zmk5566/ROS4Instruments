from setuptools import setup

package_name = 'serial2topic'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='k-pc',
    maintainer_email='k-pc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'talker = serial2topic.publish:main'
        'topic2osc = serial2topic.topic2osc:main'
        ],
    },
)
