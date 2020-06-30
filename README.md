# Tech2335-Freestyle

# Flight Pick-ups: Get to the Airport on time!

This program asks the user to input flight information and their address to determine the appropriate time a user needs to leave to meet an arriving flight.

### Program set-up:
1. Create the flights environment in conda
`conda create -n flights-env (first time only)`
`conda activate flights-env`
2. Install the required modules
`pip install -r requirements.txt`
3. Create a .env file and set the following API keys:
    - MAPQUEST_API
    - PLANE_API_KEY

## Running the program:
`python app/departure.py`

- Enter the required flight information when asked for input. You can refer to active flights at https://flightradar24.com
- Enter your address information.
- The program will let you know when you should leave to get to the airport on time!