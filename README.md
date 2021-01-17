# Functional Overview
The dataViz program allows to analyze music data by generating different graphs.

To preview the program's results without running it, a pre-generated page has been prepared at this URL : http://dash.monnot.org/ 

### Dashboard information :
#### Home
Homepage of the generated website, the `Home` dashboard contains
basic statistics which are visible by clicking the collapsable "Basic statistics"
button; and a pie chart representing the number of songs per genre.

#### Music list
The `Music list` dashboard displays the server's music database and
shows their respective metadata.

#### Year
The `Year` dashboard contains a graph representing the number of songs
released each year in the form of a vertical bar graph.

#### Popular genres
The `Popular genres` dashboard contains an animated vertical bar graph.
The basic graph displays the number of songs per genre and updates itself
when the user changes the year for which the study is done, by playing with
the animation bar.

#### Average genre duration
The `Average genre duration` dashboard allows the user to visualize the average
duration of the songs for each genre. For aesthetic purposes, only a
few genres have been isolated (Metal, R&B, Alternative, Rock, Pop and Hip-Hop).
Other genres have been grouped in the "Other" section. This has been done to prevent
a large database to generate too many genres, which would make the graph unreadable.


# Technical Overview
#### Installation
- Install Python dependencies
````
$ python pip install -r requirements.txt
````
#### Usage :
The dataViz program can run using two modes of music sourcing :
- MP3 files : Add the music you want to analyze in the `assets` folder
located in the `dataViz` parent folder.
```
$ python dataViz
```
- JSON file : Analyze music data contained in a JSON file. Either test use
our pre-generated file : `dataViz/resources/data.json` \
or add your own file. \
Make sure to add the -j option.
```
python dataViz -j dataViz/resources/data.json
```

For further help, the -h option is available for use :

```
$ python dataViz -h

usage: dataViz [-h] [-j JSON File]

Visualize song data.

optional arguments:
  -h, --help    show this help message and exit
  -j JSON File  source metadata from JSON file
```
