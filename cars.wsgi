import sys
sys.path.insert(0, '/srv/cars')
sys.stdout = sys.stderr

activate_this = '/srv/cars/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from cars import app as application
