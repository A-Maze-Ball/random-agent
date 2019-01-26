"""Sets up conda environment for running random agent"""

import os, sys
import subprocess

def main():
    print('Setting up RandomAgent conda environment.')
    if not is_conda_available():
        print('\"conda\" is not available in this context. Are you sure you have minconda or anaconda installed and are running this from a conda environment?')

    add_conda_forge()
    install_deps()

    print('Done setting up environment.')

def is_conda_available():
    try:
        subprocess.check_call(
            ['conda', '--help'],
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

def install_deps():
    subprocess.check_call(['conda', 'install', '--yes',
        'python=3.6',
        'pylint',
        'git',
        'cmake']
    )
    subprocess.check_call(['pip', 'install',
        'gym',
        'gym[atari]',
        'gym-retro']
    )

def add_conda_forge():
    subprocess.check_call(['conda', 'config', '--add', 'channels', 'conda-forge'])

if __name__ == '__main__': main()