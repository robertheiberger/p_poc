from setuptools import setup, find_packages

setup(
    name='model',
    version='0.0.1rc0',

    # Package data
    packages=find_packages(),
    include_package_data=True,

    # Insert dependencies list here
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'flask',
        'gunicorn',
        'gevent',
        'tensorflow',
        'keras',
        'gensim',
        'tqdm',
        'nltk',
        'emoji',
        'sagemaker' 
    ],

    entry_points={
        "model.training": [
           "train=model.train:entry_point"
        ],
        "model.hosting": [
           "serve=model.server:start_server"
        ]
    }
)
