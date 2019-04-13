# xkcd Downloader

Ever been bored and wanted offline access to [xkcd](https://xkcd.com/)? You might've seen many other xkcd downloads out there, but this one is by far the best because of the following reasons.
- This software downloads each comic from xkcd skipping those already downloaded without the need for a database, complex command line arguments, etc. 
- It facilitates easier reading by storing comics in `year/month` subdirectories. 
- It runs really fast because it downloads comics in parallel.
- It's well documented for usage on Android, Windows, etc. 
- It features a CLI application.

NOTE: A few comic numbers might be skipped because they either don't exist or don't contain a visual.

# Installation

## Prerequisites

- [Python 3](https://www.python.org/downloads/)

## Building

1. Clone the repository:
    - HTTPS: `git clone https://github.com/neelkamath/xkcd-downloader.git`
    - SSH: `git clone git@github.com:neelkamath/xkcd-downloader.git`
1. Change the directory: `cd xkcd-downloader`
1. Install dependencies:
    - Windows: `pip install -r requirements.txt`
    - Other: `pip3 install -r requirements.txt`

# Usage

1. Change the directory: `cd xkcd-downloader/src`
1. Run:
    - Windows: `python downloader.py`
    - Other: `python3 downloader.py`

If you're using [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en), you can have the comics show up in Google Photos on your device by running `termux-setup-storage` and specifying the path to be `./../../storage/pictures/xkcd`.

You can optionally have the script run each time your computer boots using the following steps:
- Windows:
    1. Go to the directory `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `<YOUR_USERNAME>` is your username.
    1. Create a shortcut pointing to the location of the script.
    1. Make sure python scripts open with `Python` (so that when you open the file from Windows Explorer it runs the script and doesn't open the editor). You can do this by right-clicking the script, clicking `Opens with:` in the `General` tab and choosing `Python`.
- Other:
    1. Make the script executable: `chmod +x downloader.py`
    1. Schedule it:
        1. `crontab -e`
        1. At the end of the file, add: `@reboot <PATH>`, where `<PATH>` is the path to the script

# Credits

- [Neel Kamath](https://github.com/neelkamath): initial work
- [goldlagoon](https://github.com/goldragoon): download parallelization, command line application

# License

This project is under the [MIT License](LICENSE).
