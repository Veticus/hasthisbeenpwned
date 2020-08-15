# Has This Been Pwned ?

A quick and crummy python script, letting you check a password against the [haveibeenpwned.com](https://haveibeenpwned.com/) database, without letting the password or hash leave your machine.
This can be usefull for compliance, in airgapped machines or when you're stuck in "the field" witht a bunch of hashes and no connection.

## Getting Started


#### Step 1: Clone this repo
```bash
$ git clone https://github.com/Veticus/hasthisbeenpwned.git
```

#### Step 2: Use `pip` to install `pyspin`
```bash
$ pip install pyspin
```
_Note: on some OS'es you need to specify that you want to use python3, when using pip. If your system has both python2 and python3 just run `pip3 install pyspin`_

#### Step 3: Get the list
The file can be found here: [Have I Been Pwned: Pwned Passwords](https://haveibeenpwned.com/Passwords)
I urge you to use the torrent file, to get the file. Alternatively you can download it directly.
```bash
$ wget https://downloads.pwnedpasswords.com/passwords/pwned-passwords-sha1-ordered-by-hash-v6.7z
```

#### Step 4: Extract the list
Any 7zip compatible unarchivers can do this for you. You probably already know how to do that. If you dont - i recommend 7za or p7zip for this. They're easy to use.

## Usage
Now for the good part. 
Let's say you want to use `hunter18` as your next password, but want to check if it has been leaked.
```bash
$ python3 hasthisbeenpwned.py hunter18
```
The script will then show you a little spinner, and once a match is found, tell you in how many leaks the password has appeared.

Here's a little video to see it in action: 
[![asciicast](https://asciinema.org/a/RyzTTHDQFsziCrmDxRFU1Uo7E.svg)](https://asciinema.org/a/RyzTTHDQFsziCrmDxRFU1Uo7E)

As you can see, the password `hunter18` has been in 3468 leaks, submitted to [haveibeenpwned.com](https://haveibeenpwned.com/) - Making this a horrible password. Well, amongst other reasons.

## Author

* **Tim Engel** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the WTFPL license - see more here: [wtfpl.net](http://www.wtfpl.net/)

## Acknowledgments

* A colossal THANK YOU to Troy Hunt for making [haveibeenpwned.com](https://haveibeenpwned.com/) free to use.

## Badges

![Progress](https://progress-bar.dev/2/?scale=5&title=Usefulness&suffix=/5)
