"""To delete a file, the OS module is first imported,
and then, os.remove() is run
"""

import os
from sys import argv

script, filename = argv

"""To prevent the command from runnng into error,
we may check if the file exists before trying to delete it."""
if os.path.exists(filename):
    os.remove(filename)
else:
    print("The file does not exist.")