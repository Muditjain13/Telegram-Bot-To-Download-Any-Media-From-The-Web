# Universal Media Downloader Telegram Bot

A powerful and versatile Telegram bot that allows users to download content from various social media platforms and websites. Built with Python and designed for ease of use across multiple platforms.

## Features

### Multi-Platform Support

- Download from various social media platforms
- Support for video sharing websites
- Handle both short and full URLs
- Cross-platform compatibility

### Flexible Download Options

- Download videos with audio
- Audio-only downloads (MP3/other formats)
- Video-only downloads
- High-quality downloads up to 50MB
- Automatic format selection

### Content Types Supported

- Videos and short-form content
- Audio tracks and music
- Images and photo galleries
- Stories and temporary content
- Profile pictures and avatars
- Playlists and collections

### General Features

- User-friendly interface with emoji feedback
- Automatic file type detection and appropriate sending
- Robust error handling and logging
- Memory-efficient temporary file management
- Support for multiple file formats (video, audio, images)
- Extensible architecture for adding new platforms

## Quick Start

### Prerequisites

- Python 3.7+
- FFmpeg installed on your system
- Telegram Bot Token (from @BotFather)
- Internet connection for downloading content

### Installation

1. **Clone the repository**
   
   ```bash
   git clone https://github.com/yourusername/telegram-media-downloader-bot.git
   cd telegram-media-downloader-bot
   ```
1. **Install dependencies**
   
   ```bash
   pip install -r requirements.txt
   ```
1. **Set up environment variables**
   
   ```bash
   # Set your token and ffmpeg location
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   export FFMPEG_PATH="/path/to/ffmpeg"  # Optional if ffmpeg is in PATH
   ```
1. **Run the bot**
   
   ```bash
   python bot.py
   ```

## Usage

### Basic Commands

- `/start` - Initialize the bot and get welcome message
- `/help` - Display usage instructions and supported features
- `info <platform>` - Get specific information about downloading from a platform

### Download Formats

Simply send a link to the bot with optional flags:

```
<link> <flags>
```

**Available Flags:**

- `audio` - Download audio only
- `video` - Download video only
- (no flag) - Download both audio and video (default)

### Examples

```bash
# Download video with audio (default)
https://example.com/video123

# Download audio only
https://example.com/video123 audio

# Download video only (no audio)
https://example.com/video123 video

# Get platform-specific help
info platform_name
```

## Configuration

### Environment Variables

|Variable            |Required|Description                            |Default      |
|--------------------|--------|---------------------------------------|-------------|
|`TELEGRAM_BOT_TOKEN`|✅       |Your Telegram bot token from @BotFather|None         |
|`FFMPEG_PATH`       |❌       |Path to FFmpeg executable              |Auto-detected|
|`MAX_FILE_SIZE`     |❌       |Maximum download file size in bytes    |50MB         |

### FFmpeg Installation

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**

1. Download from [FFmpeg official website](https://ffmpeg.org/download.html)
1. Extract and add to PATH
1. Set `FFMPEG_PATH` environment variable

**macOS:**

```bash
brew install ffmpeg
```

## Requirements

Create a `requirements.txt` file:

```txt
python-telegram-bot==20.7
yt-dlp>=2023.12.30
instaloader>=4.10
validators>=0.22.0
pathlib2>=2.3.7
```

## Security & Privacy

- **No Data Storage:** Files are temporarily downloaded and immediately deleted after sending
- **Environment Variables:** All sensitive data stored securely in environment variables
- **No Logging:** User URLs and personal data are not logged or stored
- **Rate Limiting:** Built-in protection against spam and abuse

## Technical Details

### Architecture

- **Backend:** Python with python-telegram-bot library
- **Download Engine:** yt-dlp for universal media extraction
- **Media Processing:** FFmpeg for format conversion
- **File Handling:** Temporary directory management with automatic cleanup

### Supported Formats

- **Video:** MP4, MKV, WEBM, AVI, and more
- **Audio:** MP3, AAC, OGG, FLAC, and more
- **Images:** JPG, PNG, WEBP, GIF

### Performance

- **File Size Limit:** 50MB per download (configurable)
- **Concurrent Downloads:** Handled per user session
- **Memory Usage:** Optimized with streaming downloads
- **Cleanup:** Automatic temporary file removal

## Contributing

We welcome contributions! Here’s how you can help:

1. Fork the repository
1. Create a feature branch
   
   ```bash
   git checkout -b feature/amazing-feature
   ```
1. Make your changes
1. Add tests if applicable
1. Commit your changes
   
   ```bash
   git commit -m 'Add amazing feature'
   ```
1. Push to the branch
   
   ```bash
   git push origin feature/amazing-feature
   ```
1. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/telegram-media-downloader-bot.git

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run with debug logging
export LOG_LEVEL=DEBUG
python bot.py
```

## Troubleshooting

### Common Issues

**Bot doesn’t respond:**

- Check if `TELEGRAM_BOT_TOKEN` is set correctly
- Verify bot is running and has internet connection
- Check bot permissions in Telegram

**Download fails:**

- Ensure FFmpeg is installed and accessible
- Check if the website is supported
- Verify URL is valid and publicly accessible

**File sending fails:**

- Check file size (must be under 50MB)
- Verify bot has permission to send files
- Ensure stable internet connection

### Logs and Debugging

Enable debug logging:

```bash
export LOG_LEVEL=DEBUG
python bot.py
```

Check logs for detailed error information and troubleshooting steps.

## License

This project is licensed under the MIT License - see the <LICENSE> file for details.

## Disclaimer

This bot is for educational purposes only. Users are responsible for respecting copyright laws and terms of service of the platforms they download content from. The developers are not responsible for any misuse of this software.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API wrapper
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Universal media downloader
- [FFmpeg](https://ffmpeg.org/) - Media processing toolkit

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/telegram-media-downloader-bot/issues) page
1. Create a new issue with detailed information
1. Join our [Telegram Support Group](https://t.me/your_support_group)

-----

**Made with ❤️ for the open source community**
