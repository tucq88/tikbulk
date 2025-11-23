"""Main CLI entry point for TikBulk."""

import click
import os
import sys
from pathlib import Path
from typing import List

try:
    import yt_dlp
except ImportError:
    click.echo("Error: yt-dlp is not installed. Run: pip install -r requirements.txt", err=True)
    sys.exit(1)


def download_video(url: str, output_dir: Path, quality: str = "best") -> bool:
    """Download a single TikTok video.

    Args:
        url: TikTok video URL
        output_dir: Directory to save the video
        quality: Video quality preference (best, worst, etc.)

    Returns:
        True if successful, False otherwise
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        'format': quality,
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        click.echo(f"Error downloading {url}: {str(e)}", err=True)
        return False


@click.command()
@click.argument('urls', nargs=-1, required=True)
@click.option(
    '--output', '-o',
    type=click.Path(),
    default='./downloads',
    help='Output directory for downloaded videos (default: ./downloads)'
)
@click.option(
    '--quality', '-q',
    default='best',
    help='Video quality: best, worst, or specific format (default: best)'
)
@click.option(
    '--file', '-f',
    type=click.File('r'),
    help='File containing URLs (one per line)'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Enable verbose output'
)
@click.version_option(version='0.1.0')
def main(urls: tuple, output: str, quality: str, file: click.File, verbose: bool):
    """TikBulk - Download TikTok videos in bulk.

    You can provide URLs as arguments or use --file to read from a file.

    Examples:

        tikbulk https://www.tiktok.com/@user/video/1234567890

        tikbulk url1 url2 url3 --output ./my_videos

        tikbulk --file urls.txt --quality best
    """
    output_path = Path(output).resolve()

    # Collect all URLs
    all_urls: List[str] = list(urls)

    # Read URLs from file if provided
    if file:
        file_urls = [line.strip() for line in file if line.strip()]
        all_urls.extend(file_urls)
        file.close()

    if not all_urls:
        click.echo("Error: No URLs provided. Use --file or provide URLs as arguments.", err=True)
        sys.exit(1)

    # Remove duplicates while preserving order
    seen = set()
    unique_urls = []
    for url in all_urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    click.echo(f"Found {len(unique_urls)} unique URL(s) to download")
    click.echo(f"Output directory: {output_path}")
    click.echo(f"Quality: {quality}\n")

    # Download each video
    successful = 0
    failed = 0

    for i, url in enumerate(unique_urls, 1):
        click.echo(f"[{i}/{len(unique_urls)}] Downloading: {url}")
        if download_video(url, output_path, quality):
            successful += 1
            click.echo(f"✓ Successfully downloaded\n")
        else:
            failed += 1
            click.echo(f"✗ Failed to download\n")

    # Summary
    click.echo("=" * 50)
    click.echo(f"Download complete!")
    click.echo(f"Successful: {successful}")
    click.echo(f"Failed: {failed}")
    click.echo(f"Total: {len(unique_urls)}")


if __name__ == '__main__':
    main()
