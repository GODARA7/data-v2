# if [ -z $UPSTREAM_REPO ]
# then
  echo "Cloning main Repository"
  # git clone https://github.com/alexgurliya/Black /data-v2
# else
#   echo "Cloning Custom Repo from $UPSTREAM_REPO "
#   git clone $UPSTREAM_REPO /data-v2
# fi
# cd /data-v2
# pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 modules/main.py
