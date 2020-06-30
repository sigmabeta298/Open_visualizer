# Open_visualizer

__About__:

Open visualizer is a simple open source data visualization tool using Python and Plotly Dash.

__Author__: 

Syamanthaka B

### Description

On running the application, a browser opens up, with an option to upload user file.
A drag and drop or browse to select option is provided. 
Once the user uploads the file, currently only csv files, it populates the columns on the left panel, for selection.
In this initial v1.0 version, no checks are being done on the columns themselves. 

The user then choses what is to be plotted on x and y axes, from the freshly populated drop downs.
The graph is then displayed on the center panel, with the default graph type being bar.

The graph type can be changed using the radio button the right, with currently 3 options available.

### How to

Set up your virtual environment and git clone the repository. 
Install required libraries using 
`pip install -r requirements.txt`

Run `python index.py`

### Upcoming planned versions
*v1.0*
- [x] Upload file
- [x] Graph options
- [x] X, Y selector
- [x] Graph display

*v1.5*
- [X] Color options
- [x] Data type of columns
- [ ] Axis labels
- [ ] Graph titles

*v2.0
- [ ] Multiple lines
- [ ] Multiple y axes

*v3.0*
- [ ] Smart suggestion for graph
- [ ] More graph types

