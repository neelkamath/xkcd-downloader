# xkcd Downloader

Have you ever been bored and wanted offline access to [xkcd](https://xkcd.com/)? Thre are many other xkcd downloads out there, but this one is by far the best because it downloads super fast using download parallelization, doesn't require complex setups with tools such as databases, facilitates easier reading by using `year/month` subdirectories, is well documented for multiple platforms such as Android, and is easily configurable.

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

    Supplying `-v` or `--verbose` will print the number of comics to be printed.

    Supplying `-d <DIRECTORY>` or `--directory <DIRECTORY>` will download comics to `<DIRECTORY>` instead of the current directory.
1. You can optionally have the script run each time your computer boots.
    - Windows:
        1. Go to the directory `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `<YOUR_USERNAME>` is your username.
        1. Create a shortcut pointing to the location of the script.
        1. Make sure python scripts open with `Python` (so that when you open the file from Windows Explorer it runs the script and doesn't open the editor). You can do this by right-clicking the script, clicking `Opens with:` in the `General` tab and choosing `Python`.
    - Other:
        1. Make the script executable: `chmod +x downloader.py`
        1. Schedule it:
            1. `crontab -e`
            1. At the end of the file, add: `@reboot <PATH>`, where `<PATH>` is the path to the script
1. If you're using [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en), you can have the comics show up in Google Photos on your device by running `termux-setup-storage` and specifying the path to be `./../../storage/pictures/xkcd`.

# Credits

- [Neel Kamath](https://github.com/neelkamath): initial work
- [goldlagoon](https://github.com/goldragoon): download parallelization, command line application

# License

This project is under the [MIT License](LICENSE).
