import io
import logging
from os import path


def read_from_file(file_name: str, output_stream: io.StringIO, error_stream: io.StringIO) -> bool:
    """
    Reads file content into output_stream.
    Writes errors into error_stream.
    :return: True on success
    """
    success = False
    if not path.exists(file_name):
        error_stream.write('No such file %s' % file_name)
    elif not path.isfile(file_name):
        error_stream.write('%s is not a file' % file_name)
    else:
        file = open(file_name)
        if file.mode == 'r':
            success = True
            output_stream.write(file.read())
        else:
            error_stream.write('Cannot read from file %s' % file_name)
        file.close()
    return success


def read_from_file_log_errors(file_name: str, output_stream: io.StringIO, tag: str) -> bool:
    """Reads file content into output_stream and logs errors."""
    error_stream = io.StringIO()
    success = read_from_file(file_name, output_stream, error_stream)
    error = error_stream.getvalue()
    if len(error) > 0:
        logging.error(("[%s]" % tag) + error)
    return success
