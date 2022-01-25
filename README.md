### ViennaRNA

The [`ViennaRNA` Package](https://www.tbi.univie.ac.at/RNA/) consists of a **C** code library and several stand-alone programs for the prediction and comparison of RNA secondary structures. It is developed and maintained by the [Theoretical Biochemistry Group](https://www.tbi.univie.ac.at/index.html) at the University of Vienna.

In case you are using `ViennaRNA` software for your publications you may want to cite:

```
Lorenz, Ronny and Bernhart, Stephan H. and Höner zu Siederdissen, Christian and Tafer, Hakim and Flamm, Christoph and Stadler, Peter F. and Hofacker, Ivo L.
ViennaRNA Package 2.0
Algorithms for Molecular Biology, 6:1 26, 2011, doi:10.1186/1748-7188-6-26
```

### `RNAlib` API Docs

The API docs can be found at https://www.tbi.univie.ac.at/RNA/ViennaRNA/doc/html/index.html

### `ViennaRNA` PyPI Installation

Life at last is simple, and the possibilities are endless.

Just open your favorite shell.

```bash
$ pip install ViennaRNA
```

Sit back, relax and let `pip` do its thing. When everything is installed, verify like so.

```bash
$ python
Python 3.9.5 (default, Jun  4 2022, 12:28:51)
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import ViennaRNA
>>> dir(ViennaRNA)
['RNA', 'RNAlib', 'ViennaRNA', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'main', 'rna', 'rnalib', 'viennarna']
```

> **Note** The objects `RNA`, `RNAlib`, `ViennaRNA`, `rna`, `rnalib`, and `viennarna` all refer to the same `RNA` SWIG module that you'd get if you installed the ViennaRNA python interface from source. The statements `from ViennaRNA import RNA` is then equivalent to `from ViennaRNA import rnalib`.

### Using `ViennaRNA` from PyPI

The PyPI installer was developed so that computational synthetic biologists could specify `ViennaRNA` as a requirement for their `python` applications (via `install_requires` in their `setup.py`), without requiring their users to download and install it separately. Because this is the 21st century, and dependency installation should not deter application adoption. Once installed, you can seamlessly `import RNA`, successfully. Another reason this installer exists is because the `conda` package for `ViennaRNA` is broken, and hasn't been fixed in a while. This installer works under `conda` as well.

Relevant DNA or RNA parameter files will need to be packaged with developed application and supplied to `RNA.read_parameter_file(parameter_file_path)` for proper usage. You may then want to specify those parameter files as part of your `package_data` in your `setup.py`, and make it available to `RNA.read_parameter_file(...)` via `pkg_resource.resource_filename(...)` function.

You can find all of the different DNA and RNA parameters accepted by the `RNA` module in [here](https://github.com/ayaanhossain/ViennaRNA/tree/main/ViennaRNA-2.4.18-Latest/misc).

**Example:** Say, your application is called `awesomeRNA` and your package is structured like the following.

```
- awesomeRNA/
    - docs/
    - examples/
    - tests/
    - awesomeRNA/
        - __init__.py
        - awesomeRNA.py
        - utils.py
        - params/
            - dna_mathews2004.par
            - rna_andronescu2007.par
    - setup.py
    - setup.cfg
    - README.md
    - LICENSE
```

A part of your `setup` function inside `setup.py` may then contain the following.

```python
setup(

    # stuff before

    packages=['awesomeRNA', 'awesomeRNA.params'],

    package_dir={
        'awesomeRNA': './awesomeRNA'},

    package_data={
        'awesomeRNA': ['params/*.par']},

    install_requires=[
        'numpy',
        'ViennaRNA']

    # stuff after
)
```

Then in your application code, you can perhaps do the following.

```python
import RNA
import pkg_resources

def awesomeRNA_main(
    seqeuence,
    temperature=37,
    param_name='dna_matthews2004'):

    # Basic Setup
    if temperature != 37:
        RNA.cvar.temperature = temperature
    RNA.cvar.dangles = 2
    settings = RNA.md()

    # Read Parameters
    parameter_file = pkg_resources.resource_filename(
        'awesomeRNA', 'params/{}.par'.format(
            param_name))
    RNA.read_parameter_file(parameter_file)

    # Calculate MFE and Secondary Structure
    fc_obj = RNA.fold_compound(
        seqeuence,
        settings)
    structure, mfe = fc_obj.mfe()

    # Return Results
    return structure, mfe

```

> **Note** These examples are for demonstrative purposes only.

### Troubleshooting

If you have trouble installing this package inside a `conda` environment due to `libgcc` issues, you might want to install `mamba` (`conda install -c conda-forge mamba`), or create your environment with `mamba` to begin with (`conda create -n myEnvName -c conda-forge mamba`). Then, simply `mamba install libgcc` and try `pip install ViennaRNA` again. Additionally, you might require to `mamba install libgcc-ng libstdcxx-ng`.

### License
`ViennaRNA` Package (c) Theoretical Biochemistry Group, University of Vienna.

`ViennaRNA` Package has its [own custom LICENSE](https://github.com/ViennaRNA/ViennaRNA/blob/master/COPYING).

`ViennaRNA` PyPI Installer (c) 2022 Ayaan Hossain.

`ViennaRNA` PyPI Installer is an **open-source software** under [MIT](https://opensource.org/licenses/MIT) License.

See [LICENSE](./LICENSE) file for more details.
