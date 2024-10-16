import logging

def process(data):
    logging.info(f"Processing {len(data)} items")
    return [x.strip() for x in data if x]
