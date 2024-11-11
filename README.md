
# My Zootopia

My Zootopia is a Python-based project that retrieves and displays information about various animals using the [API Ninjas Animals API](https://api-ninjas.com/api/animals). The project allows users to search for an animal by name and generates an HTML file displaying the animal’s details, such as its characteristics, habitat, diet, and more.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technologies](#technologies)

## Overview

The project uses the Animals API from API Ninjas to fetch data on a specified animal. Once retrieved, the data is formatted into a user-friendly HTML page using a customizable template. The HTML page includes a list of the animal’s traits and general information.

## Features
- **User Input**: Users can enter an animal name and skin type if wanted to retrieve data.
- **API Integration**: Fetches animal details from an external API.
- **HTML Output**: Displays retrieved information in an HTML template.

## Installation

### Prerequisites
- Python 3.x
- [API Ninjas API Key](https://api-ninjas.com/signup), [Used API](https://api-ninjas.com/api/animals)
- [dotenv](https://pypi.org/project/python-dotenv/) package for securely handling the API key

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kayeffemm/My-Zootopia.git
   cd My-Zootopia
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the project root directory and add your API key:
     ```plaintext
     API_KEY=your_api_key_here
     ```

## Usage

1. Run the program:
   ```bash
   python animals_web_generator.py
   ```

2. Follow the prompt to enter the animal name. For example:
   ```
   Please enter the desired animal: cat
   ```

3. The program generates an HTML file (`animals.html`) displaying information about the specified animal.

## File Structure

```plaintext
My-Zootopia/
├── animals_web_generator.py    # Main script for executing the program
├── data_fetcher.py             # script for communicating with Animals-API
├── animals_template.html       # HTML template for displaying animal info
├── animals.html                # Final HTML which displays the information
├── .env                        # Environment file storing API key
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Technologies
- **Python**: Primary programming language.
- **Requests**: For handling API requests.
- **dotenv**: For environment variable management.
- **HTML**: For the output template.
