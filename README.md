# Images To PDF
A utility which searches a directory for target images that are combined together into a PDF.

## Installation
- Clone Repo
- Install Python3
- Install python dependencies
```commandline
pip install -r requirements.txt 
```

## CLI

```commandline
dist/main imagesDirectory targetDirectory outputPDF
```

```commandline
dist/main images final finalImages
```

- `imagesDirectory` default `None`
  - Directory which will be recursed through to find target images
- `targetDirectory` default `None`
  - Sub directory of imagesDirectory which contains images to put into PDF
- `outputPDF` default `Grouped_Images.pdf`
  - Name of PDF to output. Don't include `.pdf` extension 


## Build
- Install `pyinstaller`
```commandline
pip install pyinstaller
```

- Build executable from root of project
```commandline
pyinstaller main.spec
```

### First build
If building for the first time with `imagesToPDF.spec` run
```commandline
pyinstaller -F --name imagesToPDF main.py
```