# RobotFramework for TMCM

## Environment setting
* Python >= 3.6
* Run
```
pip install --upgrade -r requirements
```
* Add `RobotFramework\webdriver` into environment variable `PATH`.

## How to run cases
* Run specific test case
```
robot -d <result folder> -t <test case title> <test file>
```

* Run all test case
```
robot -d <result folder> <test file>
```

* Run all test case having specific tag
```
robot -d <result folder> -i <tag> <test file>
```
