# Server

## Setup

1. Create python VENV (optional)///
2. Install requirements

```shell
pip install -r api_server/requirements.txt
pip install -r common/requirements.txt
pip install -r mcu_driver/requirements.txt
```

3. Install Redis

## Things to do

1. Add the Redis code
2. Turn Redis test code into unit tests (research unittest/pytest)
3. Look into FastAPI documentation
   1. basic server
   2. transform into cbv
   3. create separate route file
   4. try a websocket example
   5. run a separate thread along side FastAPI
   6. how to server static files)
4. Later we'll do the MCU
5. Wait for list of parameter from frontend/embedded teams

- I'll talk to Zach about getting you more specifics (try to get back to your later today or tomorrow)
- In the meantime
  - Cleaning up the code (consistency, comments, naming, etc...)
  - Think of some solutions for how to store our parameters (experiment with enums, dicts, etc...)
  - Look into Serial Peripheral Interface (SPI) and maybe research a few libraries in Python that work with spi
  - Look into how to create a docker container (Dockerfiles & docker-compose)