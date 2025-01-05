echo "Cloning Repo...."
git clone https://github.com/alexgurliya/data-v2 /data-v2
cd /data-v2
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 modules/main.py
