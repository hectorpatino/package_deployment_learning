from setuptools import setup


# with open("README.md", "r") as fh:
#     long_description


setup(name="rote_chairs",  # Nombreen pipy
      version="0.0.2",  # Versión de desarrollo
      description="Paquete de prueba",  # Descripción del funcionamiento
      author="Hector Patiño",  # Nombre del autor
      author_email='hectorpatino24@gmail.com',  # Email del autor
      license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
      url="http://ejemplo.com",  # Página oficial (si la hay)
      packages=['chairs'],
      install_requires=['pandas'],
      test_suite='tests',
      keywords='separted spaces keywords',
      # long_description=long_description,
      # long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      )
