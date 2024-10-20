def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r',) as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_dict)

        return cats_info
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    file_path = "/Users/julia/Desktop/goit-pycore-hw-04/02/cats.txt"
    cats_info = get_cats_info(file_path)
    
    print(cats_info)

if __name__ == "__main__":
    main()
