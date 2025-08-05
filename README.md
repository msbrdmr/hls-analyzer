# HLS Analyzer

This script analyzes HLS streams and provides useful information about them. It can parse master playlists and variant playlists, download segments, and analyze the transport stream (TS) contents.

## Features

- Parses master and variant HLS playlists.
- Analyzes TS segments to extract information about tracks and media formats.
- Reports timing information, including declared vs. real duration.
- Analyzes video frames, including keyframe information and alignment between variants.
- Provides a real-time analysis report with checks for media sequence consistency and frame alignment.

## Requirements

The script requires the following Python packages:

- `iso8601`
- `m3u8`

## Installation

 Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To analyze an HLS stream, run the `hls-analyzer.py` script with the URL of the HLS playlist:

```bash
python hls-analyzer.py <HLS_URL> [OPTIONS]
```

### Arguments

-   `url`: The URL of the HLS stream to be analyzed.

### Options

-   `-s <NUM_SEGMENTS>`: The number of segments to be analyzed per playlist (default: 1).
-   `-l <NUM_FRAMES>`: The maximum number of frames per track whose information will be reported (default: 30).
