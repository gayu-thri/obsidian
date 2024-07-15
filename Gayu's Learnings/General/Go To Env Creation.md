d
setup.sh
```bash
mkdir installed_programs
cd installed_programs

# Minconda installation & setup 
wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -u
export PATH=$HOME/miniconda3/bin:$PATH
. $HOME/miniconda3/etc/profile.d/conda.sh
conda config --set report_errors false

# Poetry installation & setup
curl -sSL https://install.python-poetry.org >get-poetry.py
python get-poetry.py --version 1.1.15 -y
export PATH="$HOME/.local/bin:$PATH"
export PATH="$HOME/.poetry/bin:$PATH"
poetry config virtualenvs.create false
```