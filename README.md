# ASCII_Art

Just a fun little project i decided to work on. Drawing a portrait of your friends is so very 19th century. 
This piece of code converts a small image into an ascii art given the dimensions are good enough to be fit for your screen. Please note that this program can only work with .jpg or .jpeg files.

It is recommended that you keep the image width below 180 pixels and use something like a text editor to view the art like <b>notepad</b> or such.

###Modules

You are going to need `numpy` and `matplotlib.image`.

Feel free to use the python code or dive into the notebook 

###How it works

We start with a JPEG image which is broken down into a tensor of 3 channels (R,G,B). We convert that tensor into a grayscale matrix by a weighted sum of all the channels. Next we take an ASCII map of characters ordered according to the relative brightness of each character. 

But every character cannot substitute a pixel properly as the length of an ASCII character is generally greater than its width. So the art will tend to strech out. To solve this problem instead of representing each pixel by a character we represent the average grayscale of 2 pixels by 1 ASCII character. This somewhat keeps the proportion of the image. Finally we can print the entire string or pipe it into a text file.