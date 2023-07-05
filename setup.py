from setuptools import setup, find_packages

setup(
    name='EnvAI',
    version='1.0',
    description='Performs Object Detection using Image Segmentation',
    author='Ashwini Ramanuj',
    author_email='ashwiniramanuj1802@email.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy',
        
        'opencv-python',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
