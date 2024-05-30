from ragas import evaluate
from ragas.metrics import answer_relevancy, faithfulness
from datasets import Dataset

# Define your data
query = "What are your refund policies?"
correct_answer = "Free & Easy Returns Policy. If your product is damaged, defective, incorrect or incomplete at the time of delivery, please raise a return request on Daraz app or website.. Return request must be raised within 14 days for all items from the date of delivery.. All Daraz Mall items are 100% Authentic by Trusted Brands and are covered under 2x Money Back Guarantee.. Note: Groceries and Digital Goods are excluded from 2x Money Back Guarantee.. For electronic appliances & mobile phones related issues after usage or after the return policy period, please check if the product is covered under seller warranty or brand warranty.. For purchases under Daraz Like New, your product is covered under 3-Months Warranty (for phones) and 6-Months Warranty (for laptops and tablets). Refer to Daraz Like New Warranty Policy and Warranty Policy for complete Terms and Conditions.. For selected categories, we accept a change of mind. Please refer to the section below on Return Policy per Category for more information.. Valid reasons to return an item. Delivered product is damaged (i.e. physically destroyed or broken) / defective (e.g. unable to switch on). Delivered product is incomplete (i.e. has missing items and/or accessories).. Delivered product is incorrect (i.e. wrong product/size/colour, fake item, or expired). Delivered product is does not match product description or picture (i.e product not as advertised). Delivered product does not fit. (i.e. size is unsuitable)"
llm_answer = "Daraz's refund policy allows for returns or refunds on items that are damaged, defective, incorrect, or incomplete. However, for device-related issues after usage or beyond the return policy period, it is recommended to check if the item is covered under Seller or Brand Warranty. Items that are non-returnable include any custom-made items. For Buy More, Save More orders, partial cancellations are not permitted, but partial returns are allowed. This means that if you wish to return certain items from a Buy More, Save More order, you can do so, but you would need to cancel the entire order if you want to return one or two specific products. After the returned items have been quality checked by Daraz, a partial refund will be issued to the customer on an item-level basis for each bundle. To submit a return request, customers must do so within 14 days of receiving their order. Decisions on returns and refunds will be taken by Daraz in its sole discretion. Customers attempting to circumvent the terms and conditions and abuse subsidies by creating new accounts will be unable to place their orders."

data = {
    'question': [query],
    'answer': [llm_answer],
    'contexts': [["Context information retrieved (if any)"]],
    'ground_truths': [[correct_answer]]
}

dataset = Dataset.from_dict(data)

result = evaluate(
    dataset=dataset,
    metrics=[
        answer_relevancy,  # Measures how relevant the generated answer is to the question
        faithfulness,      # Measures the factual accuracy of the generated answer
    ]
)

df = result.to_pandas()
print(df)
