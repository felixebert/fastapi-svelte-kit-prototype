## Setup

Ensure that you have set up Python 3.9.

### Dependencies

This app uses [pipenv](https://pipenv.pypa.io/en/latest/). If you are not already using it, install it by running:

```bash
pip install --user pipenv
```

When pipenv is ready, use the following command to install all dependencies:
```bash
pipenv install
```

### Configuration

1) Create `.env` as a copy from `.env.example`. Please adjust the secret key, you can generate one by running `openssl rand -hex 32`
2) Create `src/db/database.json` as a copy from `src/db/database.example.json`. It contains all usable users and products. For each user, you can specify a `password` field containing plain text or a `hashed_password` field with the already hashed password.

## Development

Start a local development server by running:

```bash
pipenv run uvicorn src.main:app --reload
```
