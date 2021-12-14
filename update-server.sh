cd $HOME/mc.twelventi.com
git pull
pip install -r bot/requirements.txt
sudo service site restart
sudo service bot restart
sudo service apache2 restart
