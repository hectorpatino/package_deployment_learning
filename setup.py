from setuptools import setup

setup(name="rote_chairs",  # Nombre
      version="0.0.1",  # Versión de desarrollo
      description="Paquete de prueba",  # Descripción del funcionamiento
      author="Hector Patiño",  # Nombre del autor
      author_email='hectorpatino24@gmail.com',  # Email del autor
      license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
      url="http://ejemplo.com",  # Página oficial (si la hay)
      packages=['chairs'],
      install_requires=['pandas'],
      test_suite='tests',
      classifiers=[
              "Development Status :: 3 - Alpha",
              "Topic :: Utilities",
              "License :: OSI Approved :: GNU General Public License (GPL)",
          ],
      )
