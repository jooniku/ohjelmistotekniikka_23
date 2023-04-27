# MMAlogbook

With the app, users can keep a record of their martial arts training sessions and get data from them. The app can be used by multiple registered users.

## Documentation
- [User manual](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/user_manual.md)
- [Requirement specification](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/requirement_specification.md)
- [Architecture description](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/architecture.md)
- [Changelog](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/changelog.md)
- [Working time record](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/working_time_record.md)

## Releases
- [Week 5 Release](https://github.com/jooniku/ohjelmistotekniikka_23/releases/tag/week5)

## Installation

1. Install dependencies:
```bash
poetry install
```
2. Set up database:
```bash
poetry run invoke build
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

