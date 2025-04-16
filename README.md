# EPUB to AZW3 Converter

A script that uses [Calibre's `ebook-convert`](https://manual.calibre-ebook.com/generated/en/ebook-convert.html) to convert `.epub` files into `.azw3` format.

##  Docker Usage
### Build the Docker Image
```
docker build -t epub-to-azw3 .
```
### Run with Docker
```
docker run --rm -v $(pwd):/data epub-to-azw3 \
  python3 script.py /data/mybook.epub
```
