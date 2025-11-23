# TikBulk

A simple CLI tool for downloading TikTok videos in bulk.

## Features

- Download multiple TikTok videos at once
- Support for URLs from command line arguments or file input
- Configurable output directory and video quality
- Progress tracking and error handling

## Installation

### Using uv (Recommended)

1. Install [uv](https://github.com/astral-sh/uv) if you haven't already:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone or download this repository

3. Install dependencies and set up the environment:

   ```bash
   uv sync
   ```

4. Run the tool:

   ```bash
   uv run tikbulk https://www.tiktok.com/@username/video/1234567890
   ```

   Or activate the virtual environment:

   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   tikbulk https://www.tiktok.com/@username/video/1234567890
   ```

### Using pip (Alternative)

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install as a package for global access:

```bash
pip install -e .
```

## Usage

### Basic Usage

Download a single video:

```bash
uv run tikbulk https://www.tiktok.com/@username/video/1234567890
```

Or if you've activated the virtual environment:

```bash
tikbulk https://www.tiktok.com/@username/video/1234567890
```

### Download Multiple Videos

Provide multiple URLs as arguments:

```bash
uv run tikbulk url1 url2 url3
```

### Download from File

Create a text file with one URL per line (`urls.txt`):

```
https://www.tiktok.com/@user1/video/1234567890
https://www.tiktok.com/@user2/video/0987654321
https://www.tiktok.com/@user3/video/1122334455
```

Then run:

```bash
uv run tikbulk --file urls.txt
```

### Options

- `--output, -o`: Specify output directory (default: `./downloads`)
- `--quality, -q`: Video quality preference (default: `best`)
- `--file, -f`: Read URLs from a file (one per line)
- `--verbose, -v`: Enable verbose output
- `--version`: Show version information

### Examples

```bash
# Download to custom directory
uv run tikbulk url1 url2 --output ./my_videos

# Download with specific quality
uv run tikbulk --file urls.txt --quality best

# Combine options
uv run tikbulk url1 url2 --file more_urls.txt --output ./downloads --quality best
```

## Requirements

- Python 3.8+
- uv (recommended) or pip
- yt-dlp
- click

## License

MIT
