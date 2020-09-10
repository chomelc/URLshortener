# URLshortener v1.0

A script to shorten a long URL and copy the shortened link to the clipboard. 

## Prerequesites

- Install [pyshorteners](https://pypi.org/project/pyshorteners/).
  
    ```
    $ pip3 install pyshorteners
    ```

- Install [pyperclip](https://pypi.org/project/pyperclip/).

    ```
    $ pip3 install pyperclip
    ```

## How-to

First, add the following line to your `.bashrc` file:
```shell
source ~/<path to this folder>/.url_command.sh
```

Then, you will be able to use the `surl` command : `surl <URL>` will shorten the `URL` and copy the result to the clipboard.