#!/usr/bin/python3
"""Module that fetches and processes posts from JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print status code and all post titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them into a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()

        posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(posts)
