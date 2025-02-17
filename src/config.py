import os

class CONFIG:

    # Paths
    ROOT = os.path.abspath(os.path.join(os.getcwd(), '..'))
    RAW_DATA_PATH = os.path.join(ROOT, 'data', 'climate.csv')
    PRO_DATA_PATH_v1 = os.path.join(ROOT, 'data', 'processed.parquet')