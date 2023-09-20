# gesture-map
Map gestures to key strokes.

Dylan make sure to test hid folder and install process
create a new pi


# Setup
sudo apt-get install git
cd ~
git clone https://github.com/dw-Apples-And-Bananas/gesture-map.git
sudo apt-get install xinit
echo python3 ~/gesture-map/src/app.py >> ~/.xinitrc 
xinit
