import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'modulos'))

from modulos.menu import menu_user
from modulos.core import CheckFile

if(__name__ == '__main__'):
  

   menu_user()
