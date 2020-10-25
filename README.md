# Dockpylenium

This is a simple Python program using Selenium to get a link, take a screenshot, and send an email to you.

It uses Docker to eliminate the need to use a Python virtualenv and deal with  Chrome/Chromedriver issues.

The purpose is for you to expand this boilerplate code however you'd like!



## How to use

1. Clone this repo somewhere on your computer

   ```
   $ git clone git@github.com:jianajavier/dockpylenium.git
   ```

2. Change directories into the repo

   ```
   $ cd dockpylenium
   ```

3. Change the `TO_EMAIL` constant in `./helpers/web_helper_methods.py`

   ```python
   TO_EMAIL = 'youremail@mail.com'
   ```

   You can optionally change `FROM_EMAIL` and `APP_PASSWORD` with your own if you have an account for this. I just left mine in to be easier for  you. Please don't use maliciously :)

   ```python
   FROM_EMAIL = 'jianascripts@gmail.com'
   APP_PASSWORD = 'woczgwgmwjsmnuhe'
   ```

4. Make sure you have Docker installed and running. Build the Docker container.

   ```
   $ docker build -t dockpylenium .
   ```

5. Run the container. Replace `/your/absolute/path/`

   ```
   $ docker run -v /your/absolute/path/dockpylenium:/dockpylenium dockpylenium
   ```

   * The `-v /your/absolute/path/dockpylenium:/dockpylenium ` part is to map the docker volume to a path locally so the screenshot will save to your computer

6. See an email in your inbox with a screenshot of my website.

7. Do whatever awesome things you want with it! Change links in `links.txt`



### How to add breakpoints for debugging

1. Insert breakpoint wherever you'd like the program to stop

   ```python
   pdb.set_trace()
   ```

2. Run the container with the options `-it`. [Reference](https://docs.docker.com/engine/reference/commandline/run/) to docker options.

   ```
   $ docker run -it -v /your/absolute/path/dockpylenium:/dockpylenium dockpylenium
   ```
