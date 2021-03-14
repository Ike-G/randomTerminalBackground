# Random Terminal Background 

This is a basic program to change the background of the windows terminal at random. Within the script there is a list of paths to images which the program considers, then with simple regex the settings.json file used by windows terminal is written to. To determine the image I use the `uniform` function as provided by the `random` module which feeds into a discrete probability distribution that I calculate to weight the current background as being 0.9 times as likely as the other backgrounds to be selected. 

To have this work in any meaningful way on Windows use the task scheduler pointing to this program, and then you can set it up to change according to whichever event you want. I personally set the program to run every 15 minutes, but with a little more work you can get it to run every time you initialise the terminal. Sorry for lack of packaging, it shouldn't be too difficult to edit though hopefully.

If you want to set it up to initialise on terminal process creation, I couldn't find a way to do so without Windows 10 Pro because of the need to enable process auditing, so that's something to be mindful of. Otherwise, you can either set it up just as your python interpreter pointing to the main.py file wherever you clone this repo into with `git clone https://github.com/Ike-G/randomTerminalBackground`, or you can create a .bat file to run with the following format: 

```
"{Your interpreter path}" "{Repo location}/main.py"
pause 
```

The downside of this is that you need a bit of VB scripting to prevent the .bat file creating a command window every time the command runs, but if you need to debug it might be useful.

## Setup 

Use the `.paths` file to specify the location of the `settings.json` folder on your machine. Leave a one line space, then add the paths of images that you want to use.

Optionally you can include the opacity of your image after the path. If this is not included then the current opacity will be kept for all images, however if it is included then images will update with their corresponding opacities.

```
{Windows terminal filepath}/LocalState/settings.json

{Image path}/example.jpg {Opacity}
{Second image path}/example2.png 0.3
...
```

Example `.path` file above.
