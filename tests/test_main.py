import os
from kamipdf.main import extract_images
from click.testing import CliRunner


def test_extract_images():
    """ Test extract_images function."""
    runner = CliRunner()
    pdf_file_path = "data/rag_survey_2402.19473.pdf"
    output_dir = "extracted_images"

    # Create a temporary output directory
    os.makedirs(output_dir, exist_ok=True)

    # Invoke the command with the arguments
    result = runner.invoke(extract_images, [pdf_file_path])

    # Check that the command executed successfully
    assert result.exit_code == 0

    # Assert that the images are extracted
    assert os.path.exists(os.path.join(output_dir, "image_0.png"))
    assert os.path.exists(os.path.join(output_dir, "image_1.png"))
    assert os.path.exists(os.path.join(output_dir, "image_2.png"))

    # Clean up the temporary output directory
    for file in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file)
        os.remove(file_path)
    os.rmdir(output_dir)
