<div align=left><img width=100% src="https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/asset/mainpage.png"/></div>
# NER and Linking of Ancient and Historic Places

A Named-entity Recognition tool that can recognize historical places names in a text.


## Table of Contents

1. [About the Project](#about-the-project)
1. [Project Status](#project-status)
1. [Getting Started](#getting-started)
	1. [Dependencies](#dependencies)
	1. [Installation](#installation)
	1. [Usage](#usage)
1. [Release Process](#release-process)
1. [How to Get Help](#how-to-get-help)
1. [Further Reading](#further-reading)
1. [Contributing](#contributing)
1. [License](#license)
1. [Authors](#authors)

# About the Project

This project is a web application that can recognize historical places names
 in a text. User can click on the recognized results and find out completed details 
 of each historical place recognized.   
    
 All dataset are from Pleiades,  At present, it has extensive coverage for the Greek and Roman world, and is expanding into Ancient Near Eastern, Byzantine, Celtic, Early Islamic, and Early Medieval geography.    
    
 This project includes:

* A completed model built by using Spacy
* A  web application


**[Back to top](#table-of-contents)**

# Project Status

The specific domain model of historical places names is completed.  

Web pages mostly done, need to add more details.  

Evaluations not completed yet, need more tests.


**[Back to top](#table-of-contents)**

# Getting Started

Environment: 
```bash
python 3.7
```

## Dependencies

This project mainly used Spacy and Flask for external libraries.  
    
More others details see [requirements.txt](https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/requirements.txt).

## Getting the Source

This project is [hosted on GitHub](https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places.git). You can clone this project directly using this command:

```
git clone https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places.git
```

## Installation

Instructions for how to install the project.

```
# load the web directory.
cd web/

# run app.py
python app.py

# The web application should be deploy on localhost now.
# Click on the localhost address to use the web application.
```

## Usage

When enter the localhost web application, it should be looked like this.    
<div align=center><img width=70% src="https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/asset/mainpage.png"/></div>  
        
After entering your historical text, click on submit button, results come out.  
<div align=center><img width=70% src="https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/asset/result.png"/></div>

Click on place names recognized, it would jump to place information details page.
<div align=center><img width=70% src="https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/asset/place_information.png"/></div>


**[Back to top](#table-of-contents)**

# Release Process

Version 1.0.0.

# How to Get Help

Please post on issues section if you need any helps.

# Contributing

We encourage public contributions! Please review [CODE_OF_CONDUCT.md](https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/CODE_OF_CONDUCT.md) for details on our code of conduct and development process.

**[Back to top](#table-of-contents)**

# Further Reading and References

[Pleiades](https://pleiades.stoa.org/)  
[Flask](https://flask.palletsprojects.com/en/1.1.x/)    
[Spacy](https://spacy.io/)  

**[Back to top](#table-of-contents)**

# License

Copyright (c) 2020 Dr. Andreas Vlachidis, Zhishu Lin.

This project is licensed under the MIT license - see [LICENSE.md](https://github.com/lamharrison/NER-and-Linking-of-Ancient-and-Historic-Places/blob/master/LICENSE) file for details.    


**[Back to top](#table-of-contents)**

# Authors

* **[Dr. Andreas Vlachidis](https://www.ucl.ac.uk/information-studies/dr-andreas-vlachidis-0)**
* **[Zhishu Lin](https://github.com/lamharrison)**


**[Back to top](#table-of-contents)**