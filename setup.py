from setuptools import setup

setup(name='opec',
    version='1.0',
    description='The Benchmarking Tool of the EU Operational Ecology project, OpEc',
    author='Thomas Storm',
    author_email='thomas.storm@brockmann-consult.de',
    url='http://marine-opec.eu/',
    packages=['opec', 'test'],
    data_files=[
        'default.properties',
        ('resources', ['resources/test.nc',
                               'resources/test_without_records.nc',
                               'resources/test_only_reference.nc',
                               'resources/test_with_two_ref_vars.nc',
                               'resources/test_without_depth.nc',
                               'resources/test_including_fill_values.nc',
                               'resources/ogs_test_smaller.nc.nc',
                               'resources/test.properties',
                               'resources/analysis-summary.xsl',
                               'resources/matchup_report_template.xml',
                               'resources/styleset.css',
                               'resources/default.properties'
                ])],
    requires=['numpy (>= 1.6.2)',
              'scipy (>= 0.11.0)',
              'netCDF4 (>= 1.0.1)',
              'nose (>= 1.2.1)',
              'mako (>= 0.7.3)',
              'matplotlib (>= 1.2.0)'],
)
