# MMAlogbook

With the app, users can keep a record of their martial arts training sessions and get data from them. The app can be used by multiple registered users.

## Documentation
- [User manual](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/user_manual.md)
- [Requirement specification](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/requirement_specification.md)
- [Architecture description](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/architecture.md)
- [Testing](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/testing.md)
- [Changelog](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/changelog.md)
- [Working time record](https://github.com/jooniku/ohjelmistotekniikka_23/blob/master/training_log_app/documentation/working_time_record.md)

## Releases
- [Final release](https://github.com/jooniku/ohjelmistotekniikka_23/releases/tag/week7)
- [Week 6 Release](https://github.com/jooniku/ohjelmistotekniikka_23/releases/tag/week6)
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
3. Run the application:
```bash
poetry run invoke start
```

## CLI commands

### Running the application

To run the application:
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

#### Test code quality using pylint:
```bash
poetry run invoke lint
```

