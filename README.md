# Open_visualizer

__About__:

Open visualizer is a simple open source data visualization tool using Python and Plotly Dash.

__Author__: 

Syamanthaka B

__Current version__:

v2.0

### Description

On running the application, a browser opens up, with an option to upload user file.
A drag and drop or browse to select option is provided. 
Once the user uploads the file, currently only csv files, it populates the columns on the left panel, for selection.
The column data type is also shown in the dropdowns for ease of selection.

The user then choses what is to be plotted on x and y axes, from the freshly populated drop downs.
The graph is then displayed on the center panel. The default graph is carefully selected
using a rule based recommender system

The graph type can be changed using the drop down the right, with currently 4 options available. 
But if the selected type is not possible for the columns selected, then an error message is displayed,
along with a recommendation. 

Color of the graphs can be changed using a color picker on the right. Currently this is not possible
for the pie chart though. 

A default title and labels for the axes are provided to the user based on the columns selected.
However, these can be updated with custom title and labels using text input boxes on the right panel.

Keep a watch for upcoming versions, or suggest new features :-)

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
- [x] Axis labels
- [x] Graph titles

*v2.0*
- [x] Smart suggestion for graph
- [x] More graph types

*v3.0
- [ ] Multiple lines
- [ ] Multiple y axes

