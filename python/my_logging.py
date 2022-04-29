# logging for better diagnosis

# import built-in logging module
import logging

# extra formatting of the logs
extraData = {
    'user': 'jonsnow@got.com'
}


def transact():
    # bla bla bla
    logging.error("Error occurred with the transaction!", extra=extraData)


def main():
    # logging config, only for this file.
    fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line:%(lineno)d Message: %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(level=logging.DEBUG,
                        filename='my_logger.log', filemode='w', format=fmtstr, datefmt=datestr)

    # logging
    logging.debug('Diagnostic information useful for debugging',
                  extra=extraData)
    logging.info(
        'General information about program execution results', extra=extraData)
    logging.warning(
        'Something unexpected, or a problem approaching', extra=extraData)
    transact()
    logging.critical(
        'Program may not be able to continue, serious error', extra=extraData)


if __name__ == '__main__':
    main()
