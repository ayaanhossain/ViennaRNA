from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys
import os
import shutil
import io
import site
import platform
import uuid
import atexit

VIENNA_VER = '2.5.0'
VIENNA_DIR = './ViennaRNA-{}'.format(VIENNA_VER)
SETUP_VER  = 'a4'

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

def remove_temp_path(tmp_path):
    '''
    Remove temporary installation directory.
    '''
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)

def make_temp_path():
    '''
    Build temporary installation directory.
    '''
    cwd = os.getcwd().rstrip('/')
    tmp_path = cwd + '/' + str(uuid.uuid4())
    atexit.register(
        remove_temp_path,
        tmp_path)
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    return tmp_path

def get_sitepath():
    '''
    Return site-packages path.
    '''
    return site.getsitepackages()[-1]

class ViennaRNAInstall(install):
    '''
    Custom ViennaRNA installer from latest
    source code version.
    '''

    def compile_and_install_ViennaRNA(self):
        '''
        Use the subprocess module to compile/install ViennaRNA.
        '''
        tmp_path = make_temp_path()
        src_path = VIENNA_DIR
        sitepath = get_sitepath()

        python_ver = sys.version[0]

        # Configure ViennaRNA
        cmd = ['./configure',
            '--prefix={}'.format(tmp_path),
            '--enable-simd',
            '--without-perl',
            '--without-doc-pdf',
            '--without-doc-html',
            '--without-doc',
            '--without-tutorial-pdf',
            '--without-tutorial-html',
            '--without-tutorial',
            '--without-cla-pdf',
            '--without-cla',
            '--without-kinfold',
            '--without-forester',
            '--without-rnalocmin']
        if platform.system().lower() == 'darwin':
            cmd.append('--disable-openmp')
        cmd.extend([
            'PYTHON{}_DIR={}'.format(python_ver, sitepath),
            'PYTHON{}_EXECDIR={}'.format(python_ver, sitepath)])
        cmd = ' '.join(cmd)

        # Execute Configuration
        subprocess.check_call(cmd, cwd=src_path, shell=True)

        # Execute Make
        subprocess.check_call('make', cwd=src_path, shell=True)

        # Execute Make Install
        subprocess.check_call('make install', cwd=src_path, shell=True)

        # Remove Installation Directory
        remove_temp_path(tmp_path)

    def run(self):
        self.compile_and_install_ViennaRNA()
        super(ViennaRNAInstall, self).run()

setup(
    name='ViennaRNA',

    # Link: https://www.python.org/dev/peps/pep-0440/#version-scheme
    version=VIENNA_VER+SETUP_VER,

    description='The ViennaRNA Package consists of a C code library and several stand-alone programs for the prediction and comparison of RNA secondary structures.',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ayaanhossain/ViennaRNA',

    author='Ayaan Hossain',

    author_email='auh57@psu.edu',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords=' '.join([
        'synthetic',
        'computational',
        'biology',
        'genetic',
        'DNA',
        'RNA',
        'secondary',
        'structure',
        'prediction',
        'minimum',
        'free',
        'energy',
        'centroid',
        'subopt',
        'mfe',
        'ViennaRNA',
        'dynamic',
        'programming']),

    packages=['ViennaRNA'],

    package_dir={
        'ViennaRNA': './ViennaRNA'
    },

    # python_requires=', '.join([
    #     '>=2.7',
    #     '!=3.0.*',
    #     '!=3.1.*',
    #     '!=3.2.*',
    #     '!=3.3.*',
    #     '!=3.4.*',
    #     '!=3.5.*',
    #     '>=3.6.*',
    #     '<4.0.*']),

    install_requires=[],

    cmdclass={'install': ViennaRNAInstall},

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ayaanhossain/ViennaRNA/issues',
        'Source'     : 'https://github.com/ayaanhossain/ViennaRNA/tree/master/viennarna',
    },
)
