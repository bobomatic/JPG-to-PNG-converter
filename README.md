# JPG-to-PNG-converter
Simple jpg to png converter written in Python 3 using Python Image library

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project is intended for converting image files to portable network graphics suitable for use in web pages.

## Technologies
This project is created with

Pillow 8.3.1 fork of the Python Image Library

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Features
* converts all jpg files in a folder to png
* places them in a destination folder

### To do:
* image processing options e.g. grayscale, resize, thumbnail

## Examples of Use

Usage: jpg2png [none] source_directory: [str] = ... target_directory: Optional[str] = ...

Converted files are placed in the target folder.

The following options are available:
* no options available

Code example:

`python3 jpg2png Pokedex/ my_pngs/`

If the target folder is omitted, a folder named 'converted' will be created in the current directory

## Status
Basic jpg to png functionality is complete.
Further development will be required to introduce image processing options

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery
