# crypto_card
I must've been loopy or something when I coded this, despite it's name, this program does not implement an encryption algorithm but rather uses a very simple method of stenography to hide messages within images.

## How to Use

After cloning this repository to your machine you can create your first image by executing ccwrite with `python ccwrite.py image.png Text I want to hide`. This command will create an image within your current working directory. To read the contents of the image execute ccread with `python ccread.py image.png`. This command will print the hidden text within the image to your standard output stream.
