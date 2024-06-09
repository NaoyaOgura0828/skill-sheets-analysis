import os
import pandas as pd
import logging


logging.basicConfig(level=logging.ERROR)


def search_keywords_in_skill_sheets(directory, keywords):
    """
    Search for specific keywords in all Excel skill sheets within a directory.

    This function searches through all Excel files in a given directory and checks each sheet within each file for the presence of specified keywords.
    If any of the keywords are found in any sheet, the file name is added to a list of matched skill sheets.

    Args:
        directory (str): The directory containing the skill sheet Excel files.
        keywords (list of str): A list of keywords to search for within the skill sheets.

    Returns:
        list of str: A list of filenames where the keywords are found.

    """
    all_skill_sheets = [f for f in os.listdir(directory) if f.endswith('.xlsx') or f.endswith('.xls')]
    matched_skill_sheets = []

    for skill_sheet in all_skill_sheets:
        file_path = os.path.join(directory, skill_sheet)
        try:
            if skill_sheet.endswith('.xlsx'):
                excel_data = pd.ExcelFile(file_path)
            else:
                excel_data = pd.ExcelFile(file_path, engine='xlrd')

            for sheet_name in excel_data.sheet_names:
                df = pd.read_excel(file_path, sheet_name=sheet_name)
                if df.astype(str).apply(lambda x: x.str.contains('|'.join(keywords), case=False, na=False)).any().any():
                    matched_skill_sheets.append(skill_sheet)
                    break
        except Exception as error:
            logging.error(f"An error occurred while loading the file: {file_path}, ERROR: {error}")

    return matched_skill_sheets


directory = './skill_sheets/'
keywords = ['tensorflow', 'sklearn', 'xgboost', 'lightgbm', 'keras', 'mxnet', 'nltk', 'spacy', 'transformers', 'pandas', 'numpy', 'matplotlib', 'seaborn', 'pyplot', 'pytorch']
# keywords = ['AI', '機械学習', 'Python']
matched_skill_sheets = search_keywords_in_skill_sheets(directory, keywords)

print("キーワードが含まれているファイル:")
for skill_sheet in matched_skill_sheets:
    print(skill_sheet)
