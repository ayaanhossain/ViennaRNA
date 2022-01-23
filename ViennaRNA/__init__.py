try:
    import RNA
except Exception as E:
    raise ImportError(' ViennaRNA / RNAlib not installed')

ViennaRNA = RNA
viennarna = RNA
RNAlib    = RNA
rnalib    = RNA
RNA       = RNA
rna       = RNA

__license__ = '''
    MIT License

    Copyright (c) 2022 Ayaan Hossain

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''

__doc__     = '''
    The ViennaRNA Package consists of a C code library and several stand-alone programs for the prediction and comparison of RNA secondary structures. It is developed and maintained by the Theoretical Biochemistry Group at the University of Vienna.

    In case you are using ViennaRNA software for your publications you may want to cite:

    Lorenz, Ronny and Bernhart, Stephan H. and Höner zu Siederdissen, Christian and Tafer,
    Hakim and Flamm, Christoph and Stadler, Peter F. and Hofacker, Ivo L.
    ViennaRNA Package 2.0
    Algorithms for Molecular Biology, 6:1 26, 2011, doi:10.1186/1748-7188-6-26

    Additional docs at: https://www.tbi.univie.ac.at/RNA/documentation.html

    The PyPI installer is maintained by Ayaan Hossain, so that Python developers can
    specify ViennaRNA as a requirement for their applications, without needing their
    users to download and install it separately. Because this is the 21st century, and
    dependency installation should not deter application adoption.
'''

__version__ = '2.5.0'

__author__ = 'Ayaan Hossain'


def main():
    return RNA

if __name__ == '__main__':
    main()