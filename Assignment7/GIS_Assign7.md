#### Remote Sensing and GIS

#### Assignment 7

#### Kaushal Singh [CH22BTECH11018]

## Configuration and Setup

Before starting the exercises, I prepared QGIS so that all the required tools were easy to access. I enabled the main toolbars from the **View** menu, including **Attributes**, **Data Source Manager**, **Digitizing**, **Label**, **Map Navigation**, **Project**, **Selection**, and **Snapping**. This made the interface ready for map creation, editing, and analysis.

I also installed the **QuickMapServices** and **QuickOSM** plugins through the Plugin Manager. These plugins are useful because they add extra basemaps and make it easier to bring online geographic data into the project.

![Assignment 7 setup overview](image 0.png)

## 1. Creating Maps

This part of the assignment was about learning the basic map-making workflow in QGIS. The work included loading layers, styling them properly, adding labels, and finally arranging everything in a print layout. For this exercise, earthquake data was used to build a map that is both informative and visually clear.

### 1.1 Importing Vector Data

I began by loading the required datasets into QGIS. The **ne_10m_land** layer was added first to show the land areas of the world. After that, I imported **gem_active_faults_harmonized** so that the active fault lines could be displayed. The earthquake dataset was then loaded from a TSV file by using the **Delimited Text** option, selecting **Tab** as the delimiter, assigning **Longitude** as the X field, **Latitude** as the Y field, and setting the geometry CRS to **EPSG:4326**.

After loading the data, I checked the attribute table to understand the available fields. I used the selection tools to first isolate earthquakes from the year **2020**, and then refined the selection further by keeping only features with magnitude greater than **7**. After reviewing the table, I sorted the earthquake records using the **Total Deaths** field in descending order and selected the ten events with the highest death counts. These selected records were exported as a new layer called **large_earthquakes** in GeoPackage format. Once the data preparation was complete, I saved the QGIS project.

![Attribute table and selection workflow](image 1.png)

### Challenge 1.1.1: Locating Null Island

**Do you know about Null Island? The ne_10m_land contains a polygon for this feature. Locate this polygon on the map.**

To find **Null Island**, I opened the attribute table of the **ne_10m_land** layer and searched for the feature with that name. After selecting the matching record, I used the **Zoom to Selected Features** option to move directly to its location on the map.

Null Island is positioned at **0° latitude and 0° longitude**, where the Equator meets the Prime Meridian. It is not a real island, but a well-known placeholder location that often appears in GIS datasets when coordinates are missing or incorrectly assigned.

![Imported earthquake and fault layers](image 2.png)

### 1.2 Symbology

In this section, I improved the appearance of each layer so the map would communicate information more effectively. The **ne_10m_land** layer was given a light grey fill with a white outline to create a soft background. The **gem_active_faults_harmonized** layer was styled with a brown line and a very small stroke width of **0.1** so the fault lines would be visible without dominating the map.

The **significant_earthquakes_2000_2020** layer was shown with small red circles outlined in white, with a marker size of **0.7 millimeters** and a stroke width of **0.1**. For the **large_earthquakes** layer, I used proportional symbols so that bigger circles represented earthquakes with larger death tolls. I set **Total Deaths** as the source field and used a value range from **5000 to 500000**, which QGIS converted to a size range of **3 to 10**.

I also reduced transparency where needed and refined the outlines so the layers remained readable. The large earthquake circles were given a white outline, and I created a data-defined size legend using manual classes for **5000**, **50000**, and **500000**. This made it easier to understand what the circle sizes represented.

![Symbology applied to earthquake layers](image 3.png)

### Challenge 1.2.1

**QGIS has many rich cartography features. One of my favorites is called _Live Layer Effects_. This allows you to add effects such as _Outer Glow_, _Drop Shadow_, etc., to each symbol. This takes your symbology to the next level and helps highlight certain features. Select the large_earthquakes layer and open the _Layer Styling Panel_. Expand the _Layer Rendering_ section and enable _Draw effects_. Click the _Customize effects_ button and add a drop shadow effect to the layer.**

To complete this task, I opened the **Layer Styling Panel** for the **large_earthquakes** layer and turned on **Draw effects** under **Layer Rendering**. Then I used **Customize effects** to add a **Drop Shadow** effect.

After enabling the effect, I adjusted settings such as shadow offset, blur, and opacity so the symbols stood out more clearly. This gave the earthquake circles more depth and helped separate them from the background map.

![Live layer effects with drop shadow](image 4.png)

### 1.3 Labelling

Next, I added labels to the **large_earthquakes** layer to show extra information directly on the map. I first changed the project CRS to **Equal Earth (EPSG:8857)** because it provides a better appearance for a global map. Then I enabled **Single Labels** and created an expression that combined the location name and total deaths into one label.

The label text was wrapped by using **;** as the wrap character and **20 characters** as the wrap limit. I changed the text size to **8**, set the text color to **white**, and added a **black background** with a small buffer to improve readability. I also enabled **callouts** so that each label remained visually connected to its earthquake point.

Finally, I manually moved some labels using the **Label Toolbar** so that they would not overlap. When QGIS asked for an auxiliary storage key, I used the default **fid** field. This made the overall map much cleaner and easier to read.

![Labelled earthquake map](image 5.png)

### Challenge 1.3.1

**The numbers displayed in the labels can be hard to read since they are not formatted. We can make them readable by adding a thousand-separator. So a number such as _227899_ is displayed as _227,899_ and a number like _5749_ as _5,749_. Update the expression for the labels, so the numbers are formatted. To achieve this, you can use the format_number() function in the QGIS expression editor.**

I updated the label expression by using the **format_number()** function in the QGIS expression editor. In practice, this meant changing the label text so that the **Total Deaths** value was passed through **format_number()** before display.

As a result, death counts became much easier to read. For example, values like **227899** appeared as **227,899**, which made the labels clearer and more professional.

### 1.4 Print Layout

After finishing the map design in the main QGIS window, I created a print layout to prepare the map for presentation. I opened a new layout, selected **A4** as the page size, and set the orientation to **landscape**. Then I inserted the map, stretched it across most of the page width, and left space at the top and bottom for supporting elements.

I adjusted the map scale to about **120000000** so the global view fit well inside the layout. I also added supporting items such as a title, legend, and logos to improve the final presentation. The legend was edited to remove unnecessary entries and rename items in a more understandable way. I also added text for the title and data source so the map had enough context.

Finally, the layout was exported as an image so it could be included in reports or presentations.

### Challenge 1.4.1

**Export your layout as a PDF.**

To complete this challenge, I opened the prepared print layout from the Layout Manager and selected **Export as PDF**. During export, I turned off the **Simplify geometries** option so that the map details would remain accurate and clean in the output.

The layout was then saved successfully as a PDF file, making it suitable for submission and printing.

![Final print layout export](image 6.png)

![Exported map layout in QGIS](image 7.png)

## 2. Visualizing Spatial Data

This section focused on processing and displaying spatial data in a meaningful way. I used New York City neighborhood boundaries together with population data to create a population density map. The work mainly involved joining a table to a spatial layer and then applying graduated symbology to make a choropleth map.

### 2.1 Table Join

I first loaded the **nynta2010** shapefile, which represents the neighborhood tabulation areas of New York City. Then I added the CSV file containing population information as a separate table.

Since the table included multiple years, I filtered it to keep only the records for **2010**. After that, I performed a table join using the common **NTA Code** field so that the population values became attached to the boundary layer.

Once the join was complete, I used the field calculator to create a new field for population density by combining the population and area values. The result was saved as a new layer, which was then ready for mapping.

![NYC neighborhood boundary layer](image 8.png)

### Challenge 2.1.1

**Round the population density values to the nearest integer and store them in another column named `Density_Round`.**

I used the **Field Calculator** to add a new column named **Density_Round**. In that expression, I applied the **round()** function so that the density values would be converted from decimal values to the nearest whole number.

This made the density field easier to read and more convenient to use in later analysis and map styling.

![Joined population table and density fields](image 9.png)

### 2.2 Creating a Choropleth Map

To visualize the density values, I styled the **nynta_population_density** layer using the **Graduated** renderer. I selected the **Density** field as the classification value and applied the **Yellow-Orange-Brown** color ramp so that areas with different population densities could be distinguished clearly.

I divided the data into multiple classes and adjusted the class breaks so the map would be easier to interpret. I also edited the legend labels to make them more meaningful for the reader.

The final choropleth map clearly showed how population density varies across neighborhoods in New York City.

![Choropleth map of population density](image 10.png)

### Challenge 2.2.1

**Create a new layer containing all the neighborhood tabulation areas having a population density > 100000.**

To solve this challenge, I used the **Extract by Attribute** tool and selected features where the density value was greater than **100000**. This created a new layer containing only the neighborhoods with very high population density.

The resulting layer made it easier to identify and study the most densely populated parts of the city.

![High-density neighborhoods extracted](image 11.png)
