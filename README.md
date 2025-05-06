# Setup Instructions

Follow the steps below to set up the environment and install the required dependencies:

## Step 1: Install `uv`

Run the following command to install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Step 2: Create a Virtual Environment

Create a virtual environment using `uv` with Python 3.11:

```bash
uv venv --python 3.11
```

## Step 3: Activate the Virtual Environment

- **For Mac/Linux:**

    ```bash
    source .venv/bin/activate
    ```

- **For Windows:**

    ```bash
    .venv\Scripts\activate
    ```

## Step 4: Install Dependencies

Run the following command to install the required libraries:

```bash
uv run patchright install
```