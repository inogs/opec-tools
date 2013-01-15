import configparser
import logging
import os

# needed because configparser.ConfigParser requires at least one section header in a properties file
# See http://stackoverflow.com/a/8555776 for source
def add_section_header(properties_file, header_name):
    yield '[{}]\n'.format(header_name)
    for line in properties_file:
        yield line

class Configuration(object):

    def __init__(self, alpha=None, beta=None, ddof=None, macro_pixel_size=None, geo_delta=None, time_delta=None,
                 depth_delta=None, log_level=None, zip=None, show_negative_corrcoeff=None, show_legend=None,
                 target_dir=None, target_prefix=None, include_header=None, separator=None, properties_file_name=None,
                 write_taylor_diagram=None):
        """
        Priority:
        1) what is passed as parameter
        2) what is found in file that has been passed as parameter
        3) what is found in default file
        """
        self.__read_properties(properties_file_name)
        self.__read_default_properties()

        if target_dir is None:
            target_dir = os.getcwd() # needed because if default shall be CWD, it cannot be put in the static config file

        self.__dict = {}
        self.__set(alpha, 'alpha', float)
        self.__set(beta, 'beta', float)
        self.__set(ddof, 'ddof', int)
        self.__set(macro_pixel_size, 'macro_pixel_size', int)
        self.__set(geo_delta, 'geo_delta', float)
        self.__set(time_delta, 'time_delta', int)
        self.__set(depth_delta, 'depth_delta', float)
        self.__set(log_level, 'log_level', log_level_conv)
        self.__set(zip, 'zip', bool)
        self.__set(show_negative_corrcoeff, 'show_negative_corrcoeff', bool)
        self.__set(show_legend, 'show_legend', bool)
        self.__set(target_dir, 'target_dir', str)
        self.__set(target_prefix, 'target_prefix', str)
        self.__set(separator, 'separator', separator_conv)
        self.__set(include_header, 'include_header', bool)
        self.__set(write_taylor_diagram, 'write_taylor_diagram', bool)

    def __set(self, value, name, converter):
        if value is not None:
             actual_value = value
        elif self.__config is not None and name in self.__config['dummy_section']:
            actual_value = self.__config['dummy_section'][name]
        else:
            actual_value = self.__default_config['dummy_section'][name]
        self.__dict[name] = converter(actual_value)

    def __read_properties(self, properties_file_name):
        if properties_file_name is not None:
            self.__config = configparser.ConfigParser()
            properties_file = open(properties_file_name)
            self.__config.read_file(add_section_header(properties_file, 'dummy_section'))
            properties_file.close()
        else:
            self.__config = None

    def __read_default_properties(self):
        self.__default_config = configparser.ConfigParser()
        default_properties_file = open('default.properties')
        self.__default_config.read_file(add_section_header(default_properties_file, 'dummy_section'))
        default_properties_file.close()

    def __alpha(self):
        return self.__dict['alpha']

    def __beta(self):
        return self.__dict['beta']

    def __ddof(self):
        return self.__dict['ddof']

    def __macro_pixel_size(self):
        return self.__dict['macro_pixel_size']

    def __geo_delta(self):
        return self.__dict['geo_delta']

    def __time_delta(self):
        return self.__dict['time_delta']

    def __depth_delta(self):
        return self.__dict['depth_delta']

    def __log_level(self):
        return self.__dict['log_level']

    def __zip(self):
        return self.__dict['zip']

    def __show_negative_corrcoeff(self):
        return self.__dict['show_negative_corrcoeff']

    def __show_legend(self):
        return self.__dict['show_legend']

    def __target_dir(self):
        return self.__dict['target_dir']

    def __target_prefix(self):
        return self.__dict['target_prefix']

    def __include_header(self):
        return self.__dict['include_header']

    def __separator(self):
        return self.__dict['separator']

    def __write_taylor_diagram(self):
        return self.__dict['write_taylor_diagram']

    alpha = property(__alpha)
    beta = property(__beta)
    ddof = property(__ddof)
    macro_pixel_size = property(__macro_pixel_size)
    geo_delta = property(__geo_delta)
    time_delta = property(__time_delta)
    depth_delta = property(__depth_delta)
    log_level = property(__log_level)
    zip = property(__zip)
    show_negative_corrcoeff = property(__show_negative_corrcoeff)
    show_legend = property(__show_legend)
    target_dir = property(__target_dir)
    target_prefix = property(__target_prefix)
    include_header = property(__include_header)
    separator = property(__separator)
    write_taylor_diagram = property(__write_taylor_diagram)

def get_default_config():
    return Configuration()

def log_level_conv(value):
    log_level = value.upper()
    if log_level == 'DEBUG':
        return logging.DEBUG
    if log_level == 'INFO':
        return logging.INFO
    if log_level == 'WARNING':
        return logging.WARNING
    if log_level == 'CRITICAL' or log_level == 'FATAL':
        return logging.CRITICAL
    if log_level == 'DISABLED':
        return 100              # made-up logging value higher than max
    raise RuntimeError('Erroneous log level: %s' % value)

def bool(value):
    return str(value).lower() == 'true'

def separator_conv(value):
    # I just didn't get escaped strings unescaped, so here's the low-tech version
    if value in ('\\t', 'tab', '\t'):
        return '\t'
    if value in ('\' \''):
        return ' '
    return value