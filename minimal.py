import kopf
import logging


@kopf.on.create('wim-vdw.io', 'v1alpha1', 'mycustomdatabases')
def create_fn(spec, name, **kwargs):
    logging.info(f'********* Creating a new database instance [{name}] **********')
    logging.info(f'Size in Gb     : {spec.get('databaseSizeGb')}')
    logging.info(f'High Available : {spec.get('highAvailability')}')
    logging.info(f'Region         : {spec.get('region')}')
    logging.info(f'********** End of creation logic **********')


@kopf.on.update('wim-vdw.io', 'v1alpha1', 'mycustomdatabases')
def update_fn(name, old, new, patch, **kwargs):
    logging.info(f'********* Updating a database instance [{name}] **********')
    logging.info(f'Size in Gb (old)     : {old['spec'].get('databaseSizeGb')}')
    logging.info(f'Size in Gb (new)     : {new['spec'].get('databaseSizeGb')}')
    logging.info(f'High Available (old) : {old['spec'].get('highAvailability')}')
    logging.info(f'High Available (new) : {new['spec'].get('highAvailability')}')
    logging.info(f'Region (old)         : {old['spec'].get('region')}')
    logging.info(f'Region (new)         : {new['spec'].get('region')}')
    if new['spec'].get('databaseSizeGb') < old['spec'].get('databaseSizeGb'):
        patch.spec['databaseSizeGb'] = old['spec'].get('databaseSizeGb')
        raise kopf.PermanentError("Downsizing the database is not allowed.")
    logging.info(f'********** End of updating logic **********')


@kopf.on.delete('wim-vdw.io', 'v1alpha1', 'mycustomdatabases')
def delete_fn(name, **kwargs):
    logging.info(f'********** Deleting a database instance [{name}] **********')
    logging.info(f'********** End of deletion logic **********')
