# KamiPDF Manipulation Tool 🗾

Kami is a simple command-line tool for manipulating PDF files. The name "Kami" stands for paper in Japanese. Currently, the tool offers a function to extract images from a PDF file.

## Installation

To install Kami, you need to have Python installed on your machine. You can then use pipx to install the Kami package along with its dependencies:

```bash
poetry install
pipx install .
```


## Usage

Kami is a command-line tool, so you can use it directly in your terminal. Here's how you can use the `extract` command to extract images from a PDF file:

```bash
kamipdf extract [PDF_PATH] [OUTPUT_DIRECTORY]
```

- `[PDF_PATH]`: The path to the PDF file from which you want to extract images. This is a required argument.
- `[OUTPUT_DIRECTORY]`: The directory where the extracted images will be saved. If not provided, the images will be saved in a directory named `extracted_images` in the current directory.

For example, if you want to extract images from a file named `sample.pdf` and save them in a directory named `images`, you can use the following command:

```bash
kamipdf extract sample.pdf images
```

## Contributing

Contributions are always welcome! If you want to contribute to Kami, please open a pull request.

## License

Kami is open-source software licensed under the GPL licencse.

## Contact

If you have any questions or suggestions, feel free to open an issue or contact the maintainer. 🗾