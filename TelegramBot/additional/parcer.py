from pathlib import Path

def readtoken():
    with open("files/token.txt","r") as file:
        text = file.readline()
        return text


def read_database_creditians():
    with open("files/CreditionsOfDatabase.txt","r") as file:
        return file.readlines()