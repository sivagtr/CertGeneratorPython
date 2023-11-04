# Certification Generation Using CSV --> SVG/PNG

## About
Certificate SVG is required to have a place holders in which data need to be replaced. The same place holders will be mapped with a Mapper JSON file i.e. CSVHeaderSVGMapper.json. This helps to identify which columns need to be mapped with the SVG place holders.

Generated SVG is converted to PNG for output. Please note: Generation of PNG from SVG is done using a library which may take ample amount of time for conversion.

## Commands/Libraries installation required

* cairosvg

Install cairo uses OS libraries. So make sure that you need to install the libraries based on the OS.

```
brew install cairo
brew install pango
```

There might be issue if the python is not installed with brew, since it might not find 'dyld' cache.
In such case, create a soft links for OS to recognize or uninstall and install python via brew.

> /usr/local/lib> sudo ln -s /opt/homebrew/lib/libcairo-2.dll libcairo-2.dll

## Running
> python3 CertGenerator.py 
