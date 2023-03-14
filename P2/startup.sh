echo "Starting up"
sudo apt-get update
echo "Installing python3.10"
sudo apt-get install python3.10
echo "Installing pip3"
sudo apt-get install python3-pip
echo "Installing virtualenv"
sudo apt install python3-virtualenv
echo "Creating virtual environment"
virtualenv -p python3 venv
echo "Virtual environment created"
echo "Activating virtual environment"
source venv/bin/activate
echo "Virtual environment activated"
echo "Installing packages"
cd restify
pip install -r /packages.txt
echo "Packages installed"
echo "Running migrations"
cd restify
python3 manage.py makemigrations
python3 manage.py migrate
echo "Migrations done"
echo "All compelted"

#--------------- MAC -----------------

# # mac version
# # Download python3.10
# brew install python3.10

# # Download virtualenv package
# pip3 install virtualenv

# # Get into the phase 2 folder
# cd restify

# # Create a new environment
# virtualenv -p "/usr/local/bin/python3.10" venv

# # activate the virtual environment
# source venv/bin/activate

# # install needed packages
# pip install -r packages.txt

# cd restify

# # run migrations
# python3 manage.py makemigrations
# python3 manage.py migrate
