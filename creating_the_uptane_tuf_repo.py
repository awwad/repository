# Creating a test repository for the Uptane project.

# From shell, create directories for targets, keys, etc., and create targets
# files, in the repository directory.
# mkdir -p tufrepo/keys
# mkdir -p tufrepo/targets
# cd tufrepo/targets
# mkdir -p images/brakes/config
# mkdir -p images/cellfw
# mkdir -p images/flobinator/acme
# echo "pborih2098gawidopg" > images/brakes/E859A50_9613.zip
# echo "0902gj" > images/brakes/config/someconfig.cfg
# echo "10t9813u103934035351513515" > images/flobinator/acme/1111111.zip
# echo "09103t9" > images/flobinator/acme/b20.zip
# echo "00909909104156309135609ifva" > images/cellfw/infotainment_adjacent_fw.zip
# cd ../..


# This amounts to this list:
# ['.../repository/tufrepo/targets/images/brakes/E859A50_9613.zip',
#  '.../repository/tufrepo/targets/images/brakes/config/someconfig.cfg',
#  '.../repository/tufrepo/targets/images/cellfw/infotainment_adjacent_fw.zip',
#  '.../repository/tufrepo/targets/images/flobinator/acme/1111111.zip',
#  '.../repository/tufrepo/targets/images/flobinator/acme/b20.zip']

# Then do the TUF work:

from tuf.repository_tool import *

KEYS_DIR = '/Users/s/w/repository/tufrepo/keys/'
IMAGES_DIR = '/Users/s/w/repository/tufrepo/targets/images/'


repo = create_new_repository("tufrepo")

# Create key pairs for all roles.
generate_and_write_rsa_keypair(KEYS_DIR + 'root', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'time', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'snap', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'targets', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'images', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'director', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'brakes', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'acme', password="pw")
generate_and_write_rsa_keypair(KEYS_DIR + 'cell', password="pw")


# Import public and private keys from the generated files.
public_root_key = import_rsa_publickey_from_file(KEYS_DIR + 'root.pub')
public_time_key = import_rsa_publickey_from_file(KEYS_DIR + 'time.pub')
public_snap_key = import_rsa_publickey_from_file(KEYS_DIR + 'snap.pub')
public_targets_key = import_rsa_publickey_from_file(KEYS_DIR + 'targets.pub')
public_images_key = import_rsa_publickey_from_file(KEYS_DIR + 'images.pub')
public_director_key = import_rsa_publickey_from_file(KEYS_DIR + 'director.pub')
public_brakes_key = import_rsa_publickey_from_file(KEYS_DIR + 'brakes.pub')
public_acme_key = import_rsa_publickey_from_file(KEYS_DIR + 'acme.pub')
public_cell_key = import_rsa_publickey_from_file(KEYS_DIR + 'cell.pub')
private_root_key = import_rsa_privatekey_from_file(KEYS_DIR + 'root', password='pw')
private_time_key = import_rsa_privatekey_from_file(KEYS_DIR + 'time', password='pw')
private_snap_key = import_rsa_privatekey_from_file(KEYS_DIR + 'snap', password='pw')
private_targets_key = import_rsa_privatekey_from_file(KEYS_DIR + 'targets', password='pw')
private_images_key = import_rsa_privatekey_from_file(KEYS_DIR + 'images', password='pw')
private_director_key = import_rsa_privatekey_from_file(KEYS_DIR + 'director', password='pw')
private_brakes_key = import_rsa_privatekey_from_file(KEYS_DIR + 'brakes', password='pw')
private_acme_key = import_rsa_privatekey_from_file(KEYS_DIR + 'acme', password='pw')
private_cell_key = import_rsa_privatekey_from_file(KEYS_DIR + 'cell', password='pw')

# Add public keys to repo.
repo.root.add_verification_key(public_root_key)
repo.timestamp.add_verification_key(public_time_key)
repo.snapshot.add_verification_key(public_snap_key)
repo.targets.add_verification_key(public_targets_key)

# Add private keys to repo.
repo.root.load_signing_key(private_root_key)
repo.timestamp.load_signing_key(private_time_key)
repo.snapshot.load_signing_key(private_snap_key)
repo.targets.load_signing_key(private_targets_key)


# Perform some delegations.
repo.targets.delegate('images', [public_images_key],
    [], restricted_paths=[])
repo.targets.delegate('director', [public_director_key],
    [], restricted_paths=[])
repo.targets('images').delegate('brakes', [public_brakes_key],
    [], restricted_paths=[IMAGES_DIR + 'brakes/'])
repo.targets('images').delegate('acme', [public_acme_key],
    [], restricted_paths=[IMAGES_DIR + 'flobinator/acme/'])
repo.targets('images').delegate('cell', [public_cell_key],
    [], restricted_paths=[IMAGES_DIR + 'cellfw/'])

# Perform the multi-role delegation giving Director + Images control of images.
restricted_paths = [IMAGES_DIR]
required_roles = ['targets/images', 'targets/director']
repo.targets.multi_role_delegate(restricted_paths, required_roles)

# The delegation itself already added the new roles' public keys. We still have
# to add their private keys.
repo.targets('images').load_signing_key(private_images_key)
repo.targets('director').load_signing_key(private_director_key)
repo.targets('images')('brakes').load_signing_key(private_brakes_key)
repo.targets('images')('acme').load_signing_key(private_acme_key)
repo.targets('images')('cell').load_signing_key(private_cell_key)

# Now we add targets.
repo.targets('images')('brakes').add_targets([
    IMAGES_DIR + 'brakes/E859A50_9613.zip',
    IMAGES_DIR + 'brakes/config/someconfig.cfg'])
repo.targets('images')('cell').add_targets([
    IMAGES_DIR + 'cellfw/infotainment_adjacent_fw.zip'])
repo.targets('images')('acme').add_targets([
    IMAGES_DIR + 'flobinator/acme/1111111.zip',
    IMAGES_DIR + 'flobinator/acme/b20.zip'])

# Add two of those targets to the director role as well.
repo.targets('director').add_targets([
    IMAGES_DIR + 'brakes/E859A50_9613.zip',
    IMAGES_DIR + 'flobinator/acme/1111111.zip'])

# Write/save the repository.
repo.write()
