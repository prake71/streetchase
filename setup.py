from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])
buildOptions = dict(include_files = ['data', 'data/hiscore', 'data/intro.txt', 'data/Credits', 'data/images/', 'data/sounds', 'data/fonts', 'code',])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('streetchase.py', base=base)
]

setup(name='Street Chase',
      version = '0.1',
      description = '2D car jostle game',
      options = dict(build_exe = buildOptions),
      executables = executables)
