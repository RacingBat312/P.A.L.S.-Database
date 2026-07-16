# Source - https://stackoverflow.com/a/49394750
# Posted by James Harvey, modified by community. See post 'Timeline' for change history
# Retrieved 2026-07-16, License - CC BY-SA 3.0

import sys
import time
from time import sleep
for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)
