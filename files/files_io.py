import io
import logging


def read_from_file(file_name: str, output_stream: io.StringIO, error_stream: io.StringIO) -> bool:
    """
    Reads file content into output_stream.
    Writes errors into error_stream.
    :return: True on success
    """
    try:
        with open(file_name) as file:
            output_stream.write(file.read())
            return True
    except IOError as e:
        error_stream.write(e.strerror)
        return False


def read_from_file_log_errors(file_name: str, output_stream: io.StringIO, tag: str) -> bool:
    """Reads file content into output_stream and logs errors."""
    error_stream = io.StringIO()
    success = read_from_file(file_name, output_stream, error_stream)
    error = error_stream.getvalue()
    if len(error) > 0:
        logging.error("[%s] %s", tag, error)
    return success
