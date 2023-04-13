# MMAlogbook

With the app, users can keep a record of their martial arts training sessions and get data from them. The app can be used by multiple registered users.

## Documentation
- [Requirement specification](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/requirement_specification.md)
- [Working time record](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/working_time_record.md)
- [Changelog](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/changelog.md)
- [Architecture](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/architecture.md)

## Installation

1. Install dependencies:
```bash
poetry install
```
## CLI commands

### Running the program

To run the program:
```bash
poetry run invoke start
```

### Testing

Run tests:
```bash
poetry run invoke test
```
Generate the coverage report:
```bash
poetry run invoke coverage-report
```
_The report will be in the htmlcov directory_

Test code quality using pylint:
```bash
poetry run invoke lint
```

