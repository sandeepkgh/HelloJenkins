#!/usr/bin/env python3
"""
Simple Hello World Python Script for Jenkins Pipeline Learning
"""

def hello_world():
    """Print a hello world message"""
    print("Hello from Jenkins Pipeline!")
    print("Python Jenkins Integration - Hello World Example")


def greet(name):
    """Greet a person by name"""
    print(f"Hello, {name}! Welcome to Jenkins CI/CD Pipeline.")


if __name__ == "__main__":
    print("=" * 50)
    hello_world()
    print("=" * 50)
    greet("Jenkins User")
    print("\nScript execution completed successfully!")
