from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cygno',                                            # package name
    author="Giovanni Mazzitelli",
    author_email="giovanni.mazzitelli@lnf.infn.it",
    version='1.0.19',                                         # version
    description='Cygno Experiment Python Packge',            # short description
    url='https://github.com/CYGNUS-RD/cygno',                # package URL
    packages=find_packages(),
    package_data={'cygno': ['./pmt_correction_tables/table_cell_LNGS.npy',
                            './pmt_correction_tables/table_nsample_LNGS.npy',
                            './pmt_correction_tables/table_cell_LNF.npy',
                            './pmt_correction_tables/table_nsample_LNF.npy',
                            './pmt_correction_tables/table_cell_MAN.npy',
                            './pmt_correction_tables/table_nsample_MAN.npy']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache2 License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/cygno_repo', 'bin/cygno_runs', 'bin/cygno_mid2root', 'bin/cygno_his2root', 'bin/cygno_htc'],
    python_requires='>=3.5',
    install_requires=[
    'requests',
    'pandas',
    'requests',
    'matplotlib',
    'boto3',
    'botocore',
    'boto3sts',
    'tqdm'
    ],
    # dependency_links=[
    #     'git+https://github.com/DODAS-TS/boto3sts.git#egg=boto3sts'  # Link with version at the end
    # ]
)
