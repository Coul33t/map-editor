# Map Editor
Heyo amigo, this is the map editor you've been dreaming of your whole life! I'm jsut kidding, this is a map editor I developped for my kinda-no-more-developped isometric tactical RPG. While I developped it for this purpose, it can be use for any project, as long as you create an import function in your program to use the generated map. As long as there is the :construction: emoji in the commits messages, map export won't be available.

![Example of the GUI](/img/map_editor_gui_example.png)

### Requirements

* PyQt5
* PIL
* Numpy

### Implemented features

* Arbitrary tileset size
* Map auto-adapt to tileset size
* Drag drawing (no need to click for each tile)
* Layers system
* Unique layer display
* Map stored as numpy array

### TODO

* Map overlay cursor drawing
* Bucket filling
* Tileset selection size (drag selection)
* Map export
