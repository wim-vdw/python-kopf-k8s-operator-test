import kopf
import logging


@kopf.on.create('wim-vdw.io', 'v1alpha1', 'mycustomdatabases')
def create_fn(spec, name, **kwargs):
    logging.info(f'********* Creating a new database instance [{name}] **********')
    logging.info(f'Size in Gb     : {spec.get('databaseSizeGb')}')
    logging.info(f'High Available : {spec.get('highAvailability')}')
    logging.info(f'Region         : {spec.get('region')}')
    logging.info(f'********** End of creation logic **********')


@kopf.on.delete('wim-vdw.io', 'v1alpha1', 'mycustomdatabases')
def create_fn(name, **kwargs):
    logging.info(f'********** Deleting a database instance [{name}] **********')
    logging.info(f'********** End of deletion logic **********')
