from get_request import get_json_data
from post_request import post_json_data

def main():
    # to call the different requests defined
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = get_json_data(url)
    print(response)

if __name__ == "__main__":
    main()
