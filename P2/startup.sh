# # Download python3.10
# sudo apt-get install python3.10

# # Download virtualenv package
# pip install virtualenv

# # Get into the phase 2 folder
# cd restify  

# # Create a new environment
# virtualenv -p  "/usr/bin/python3.10" venv

# # activate the virtual environment  
# source venv/bin/activate  
  
# # install needed packages  
# pip install -r packages.txt

# cd restify  
  
# # run migrations  
# python3 manage.py makemigrations  
# python3 manage.py migrate  


# mac version
# Download python3.10
brew install python3.10

# Download virtualenv package
pip3 install virtualenv

# Get into the phase 2 folder
cd restify

# Create a new environment
virtualenv -p "/usr/local/bin/python3.10" venv

# activate the virtual environment
source venv/bin/activate

# install needed packages
pip install -r packages.txt

cd restify

# run migrations
python3 manage.py makemigrations
python3 manage.py migrate
