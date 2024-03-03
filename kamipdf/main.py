import os
import click
import fitz


@click.group()
def cli():
    """
    An PDF manipulation tool. Kami stands for paper in Japanese.
    """
    pass


@click.command("extract")
@click.argument(
    "pdf", type=click.Path(exists=True)
)
@click.argument(
    "outputdir",
    type=click.Path(),
    default="extracted_images"
)
def extract_images(pdf: str, outputdir: str):
    """Extract images from a PDF file."""

    print(f"Extracting images from {pdf}...")

    # Create output directory if it doesn't exist
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # Open the PDF document
    try:
        doc = fitz.open(pdf)
    except IOError as e:
        click.echo(f"Error opening PDF file: {e}")
        return

    # Initialize image count
    img_count = 0

    # Iterate over every page
    for page in doc:
        # Iterate over every image in the page
        for img in page.get_images():
            # Get the XREF of the image
            xref = img[0]

            # Extract the image bytes
            base = fitz.Pixmap(doc, xref)
            if base.n < 5:  # this is GRAY or RGB
                pix = base
            else:  # CMYK: convert to RGB first
                pix = fitz.Pixmap(fitz.csRGB, base)

            # Get the image extension
            ext = ".png"

            # Save the image to the local disk
            img_path = os.path.join(outputdir, f"image_{img_count}{ext}")
            pix.save(img_path)

            # Increment image count
            img_count += 1

    # Close the PDF document
    doc.close()

    click.echo(f"Extracted {img_count} images from {pdf}.")


# Add the extract_images command to the cli group
cli.add_command(extract_images)

if __name__ == "__main__":
    cli()
