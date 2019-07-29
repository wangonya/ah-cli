# ah-cli
[![Build Status](https://travis-ci.com/wangonya/ah-cli.svg?branch=develop)](https://travis-ci.com/wangonya/ah-cli)
[![Coverage Status](https://coveralls.io/repos/github/wangonya/ah-cli/badge.svg?branch=develop)](https://coveralls.io/github/wangonya/ah-cli?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/9007430b73f08f4ef978/maintainability)](https://codeclimate.com/github/wangonya/ah-cli/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/95c411aeeb8e4f39899dd8b085e99ec4)](https://www.codacy.com/app/wangonya/ah-cli?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wangonya/ah-cli&amp;utm_campaign=Badge_Grade)

A simple command line application that consumes the Authors Haven API.

## Installation
* Clone the project and enter its directory:
```
git clone https://github.com/wangonya/ah-cli.git && cd ah-cli
```
* Run `. .env` to install the app.

## Commands
*  `ah --help` - display help page
*  `ah view new_wangonya` - view the article with the slug "new_wangonya"
*  `ah list` - list all articles
*  `ah list --limit 2` - list the first two articles
*  `ah list --export json` - list all articles and export to JSON file
*  `ah list --export csv` - list all articles and export to CSV file
*  `ah list --export sqlite` - list all articles and export to sqlite database
*  `ah search tag=trevor` - search for an article with the tag "trevor"
*  `ah search author=wangonya` - search for an article with the author "wangonya"
*  `ah search title=new` - search for an article with the title "new"

**The commands can also be combined. E.g, `ah list --limit 2 --export json` lists the first 2 articles and exports the data to a JSON file**
