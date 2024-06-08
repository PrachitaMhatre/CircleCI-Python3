# CircleCI-Python3

Working with CircleCI for continuous integration.

# Aim: To study about the CircleCI model.

#Practical steps:
1. Working with CircleCI for continuous integration. Link for Download – https://desktop.github.com
2. Download Git for windows. Link for download - https://git-scm.com/download/win
3. Open Visual Studio Code → Go to Extensions → Search for Python Extension in VS Code and
download it.
4. Create a folder named as “CIRLE CI” in File Manager and open it in Visual Studio Code.
5. Create a file named as “main.py” inside CIRCLE CI folder. In “main.py” write the code as shown
below.
def to_upper(name):
return name.upper()
def say_hello(name):
print(f'Hello,{name}')
if __name__ == '__main__':
name = "TrainWithRida"
say_hello(name)
up = to_upper(name)
print(up)

6. Create a file named as “test.py” inside CIRCLE CI folder. In “test.py” write the code as shown below.
import unittest
from main import to_upper
class MyTestCase(unittest.TestCase):
def test_to_upper(self):
name = "Rida"
upper_name = to_upper(name)
self.assertEqual(upper_name,"RIDA")
if __name__ == "__main__":
unittest.main()

7.  Go to Terminal → New Terminal. On right-side click on dropdown arrow beside +icon, there should be an
option of Git Bash as shown below.
8. While installing Git, make sure to check “Add a Git Bash Profile to Windows Terminal” checkbox.
This will show Git Bash terminal in the Visual Studio Code.
9. After selecting Git Bash option the terminal should look like this.
10. Open Github for desktop → Click on Sign in to Github.com
11. Create “readme.md” file in Visual Studio Code and write the code as shown below.
12. Create new repository in Github by clicking “New” option. Enter Repository name as “CircleCi-Python”
→ Select Add a README file option→ Click on Create Repository button.
13. After successfully creating repository below screen will appear. Click on Code →Copy the URL of your
repository.
14. Clone this repository on Visual Studio Code by typing the following command: git clone
15.  After this change the directory by typing command: cd CircleCI-python
16.  After successfully changing the directory add these 3 files on your repository folder “CircleCi-Python”.
17.  Now type the command “git status” to check whether the files are visible or not.
18.  Add your pasted file on github by typing below command: git add . →Click Enter.
19.  Commit your file on github write command git commit -m “Something Text Message”.
20.   Now push the code on git by command: git push origin main
21.   To run the project type command: python main.py
22.   Create new folder named as “.circleci” inside CircleCi-Python Folder in Visual Studio Code → In that
create “config.yml” file.
23. Inside config.yml write below code to build main.py file.
version: 2.1
jobs:
build:
docker:
- image: cimg/python:3.11
steps:
- checkout
- run: python tests.py
workflows:
version: 2
build_and_test_deploy:
jobs:
- build

24. After writing the above code, push the code in git by running the following commands:
    
![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/6b8857e2-08c2-4ccc-8af3-211adae64018)
![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/07e33d1a-538d-4d73-b9d8-1f2a97690b00)


25. Now after pushing changes → Login to circleci website → Click on Log in with Github.
26. After authorizing, this Dashboard will appear.
27. Go to Projects → Click on Set Up Project.
28. After Setting up Project your project status will show success.
29. After Clicking on down arrow build link will appear where you can see your main.py running.
30. After Successfully building we will test tests.py file by writing below code in config.yml file:
version: 2.1
#version for yml file
jobs:
build:
docker:
- image: cimg/python:3.11
steps:
- checkout
- run: python main.py
test:
docker:
- image: cimg/python:3.11
steps:
- checkout
- run: python tests.py
workflows:
version: 2
build_and_test_deploy:
jobs:
- build
- test:
requires:
- build

31.After writing above code commit and push updated code on git by running these git commands:

![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/46d34825-114f-4471-96ab-ef710e78d88e)

32. After pushing modified code we can see in the dashboard two jobs successful build and open.
33. After this, write below code in config.yml file to run deploy code.
version: 2.1
jobs:
build:
docker:
- image: cimg/python:3.11
steps:
- checkout
- run: python main.py
test:
docker:
- image: cimg/python:3.11
steps:
- checkout
- run: python tests.py
deploy:
docker:
- image: cimg/python:3.11
steps:
- run: echo "Deploying Successful."
workflows:
version: 2
build_and_test_deploy:
jobs:
- build:
filters:
branches:
only: main
- test:
requires:
- build
filters:
branches:
only: main
- deploy:
requires:
- test
filters:
branches:
only: main

34. Push the updated code in git by executing git commands:
    
![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/5fb0b4d7-95b2-4345-9002-8055447cb85f)

35. . After successfully pushing config.yml file → Open circleci we can see three jobs done build, test and
deploy success in status.

![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/902c3ff0-80e3-46dd-855a-b66327e12958)

![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/f1746c4f-9842-450f-9596-0870db95028b)

![image](https://github.com/PrachitaMhatre/CircleCI-Python3/assets/144588590/c4a83ff6-ea75-4c61-88fe-f1bb55c7761d)
