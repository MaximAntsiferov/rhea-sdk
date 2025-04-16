logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(levelname)-8s %(name)s:%(lineno)s - %(message)s",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["stdout"],
            "propagate": False,
        },
    },
}
