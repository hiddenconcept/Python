# Import the 'platform' module and alias it as 'pl'.
import platform as pl

# List of attributes to retrieve from the 'platform' module.
os_profile = [
    'architecture',
    'linux_distribution',
    'mac_ver',
    'machine',
    'node',
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]

# Iterate through the list of attributes.
for key in os_profile:
    # Check if the attribute exists in the 'platform' module.
    if hasattr(pl, key):
        # Print the attribute name and its corresponding value.
        print(key + ": " + str(getattr(pl, key)()))