# Usage

## Basic Usage
When using pyimg you first need to specify what image file you want to manipulate

*Example:*
```bash
$ python -m pyimg example.png
```

There are two options you can add to this:
```-s/--stats``` and ```-o/--output```

### Stats

Prints stats about the image such as size and colourspace

### Output

Takes in a file name and will output the edited image to that file instead of writing to the same image as before

## Adding actions/commands

After you have selected your image and any of the options above, you need to choose which submodule you wish to use. There are three included but more can be added via Plugins. Once you specify your submodule, you then specify which action to use from it such as ```Rotate``` for ```Transform```

*Example Usage*
```bash
$ python -m pyimg example.png SUBMODULE ACTION
```

**Built-In:**

- [Transform](transform.md)