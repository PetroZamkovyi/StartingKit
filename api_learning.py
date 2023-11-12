#! /usr/bin/env python3

import os
import requests


# Folder with txt files:
feedback_directory = '/data/feedback/'

# URL with company website (according to the lab):
company_website_url = 'http://34.16.144.70/feedback/'

def read_feedback(file_path):
    """
    Read the content of a feedback file and return a dictionary.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return {
            'title': lines[0].strip(),
            'name': lines[1].strip(),
            'date': lines[2].strip(),
            'feedback': lines[3].strip()
        }

def upload_feedback(feedback_data):
    """
    Upload feedback data to the company's website using POST request.
    """
    response = requests.post(company_website_url, json=feedback_data)

    # Check if the request was successful (status code 201)
    if response.status_code == 201:
        print(f"Feedback uploaded successfully: {response.text}")
    else:
        print(f"Error uploading feedback. Status Code: {response.status_code}, Response: {response.text}")

        # Print the error message if available
        try:
            error_message = response.json().get('detail', '')
            print(f"Error Message: {error_message}")
        except ValueError:
            print("Error Message: Unable to parse JSON response.")


def main():
    # List all .txt files under /data/feedback directory
    feedback_files = [file for file in os.listdir(feedback_directory) if file.endswith('.txt')]
    print("Print a list of feedback files: ", feedback_files)

    for feedback_file in feedback_files:
        file_path = os.path.join(feedback_directory, feedback_file)

        # Read feedback from the file
        feedback_data = read_feedback(file_path)
        print(feedback_data)

        # Upload feedback to the company's website
        upload_feedback(feedback_data)


if __name__ == "__main__":
    main()
