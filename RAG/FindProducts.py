import os
import json

# Define the path to the directory containing the text files
directory_path = 'products'

# Output file where consolidated data will be saved
output_file = 'FinalProductsList.txt'

# Read each file in the directory
def read_product_files(directory):
    products_data = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = file.read()
                corrected_data = '[' + data.replace('}\n\n{', '},\n{') + ']'
                try:
                    product_info = json.loads(corrected_data)
                    products_data.append(product_info)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {filename}: {e}")
    return products_data

# Extract product description specifically looking more robustly
def extract_description(description_text):
    # Attempt to extract the portion after "Product Description"
    desc_start = description_text.find("Product Description:")
    if desc_start != -1:
        # Extract starting from the found index through the end of the description
        desc_substr = description_text[desc_start:]
        desc_end = desc_substr.find("<br/>")
        if desc_end != -1:
            return desc_substr[len("Product Description:"):desc_end].strip()
        else:
            return desc_substr[len("Product Description:"):].strip()
    return "Description not found."

# Write the consolidated product info to an output file
def write_product_info(products_data, output_file):
    with open(output_file, 'w') as outfile:
        for i, product in enumerate(products_data, start=1):
            product_dict = {}
            for segment in product:
                product_dict.update(segment)

            product_name = product_dict.get("Product Name", "N/A")
            category_path = product_dict.get("Category", "N/A").replace('"', '')
            brand_name = product_dict.get("Brand Name", "N/A")
            seller_name = product_dict.get("Seller Name", "N/A")
            url = product_dict.get("URL", "N/A")
            price_info = product_dict.get("Price Info", [])
            price_details = " | ".join([f"Original: {p[1]}, Discounted: {p[2]}" for p in price_info])
            # description = extract_description(product_dict.get("desc", "").replace("<br/>", "\n"))
            additional_info = product_dict.get("Additional Info", {})
            positive_ratings = additional_info.get("Positive Seller Ratings", "N/A")
            ship_on_time = additional_info.get("Ship on Time", "N/A")
            return_policy = product_dict.get("Return Policy", {})
            return_details = f"{return_policy.get('Title', 'N/A')} ({return_policy.get('Subtitle', 'N/A')})"

            # product_entry = f"Product {i:02d}: Product Name = {product_name}, Product Category = {category_path}, Brand Name = {brand_name}, Seller Name = {seller_name}, URL = {url}, Price Details = {price_details}, Description = {description}, Positive Seller Ratings = {positive_ratings}, Ship on Time = {ship_on_time}, Return Policy = {return_details}\n"
            product_entry = f"Product {i:02d}: Product Name = {product_name}, Product Category = {category_path}, Brand Name = {brand_name}, Seller Name = {seller_name}, URL = {url}, Price Details = {price_details}, Positive Seller Ratings = {positive_ratings}, Ship on Time = {ship_on_time}, Return Policy = {return_details}\n"
            outfile.write(product_entry)

# Main function to handle operations
def main():
    products_data = read_product_files(directory_path)
    write_product_info(products_data, output_file)
    print("Data consolidation complete.")

if __name__ == "__main__":
    main()
