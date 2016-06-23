from __future__ import print_function, division


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('sisl', parent_package, top_path)
    config.add_subpackage('geom')
    config.add_subpackage('io')
    config.add_subpackage('tb')
    config.make_config_py()  # installs __config__.py
    config.add_data_dir('tests')
    return config

if __name__ == '__main__':
    print('This is the wrong setup.py file to run')
