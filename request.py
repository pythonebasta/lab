import requests
def main():
    response = requests.get("http://www.google.it/")
    print ("status code: ", response.status_code)

if __name__ == "__main__":
    main()
