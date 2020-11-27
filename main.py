import os

import pywaves as py
import pandas as pd
import json

py.setNode('https://privatenode.blackturtle.eu', 'TN', 'L')
py.setMatcher('https://privatematcher.blackturtle.eu')
py.DEFAULT_BASE_FEE = 2000000
address = py.Address(
    seed=os.getenv("SEED"))
oracle = py.Oracle(
    seed=os.getenv("SEED"))

##Black liating scams
SCAM_URL = "https://raw.githubusercontent.com/BlackTurtle123/TN-community/master/scam-v2.csv"

wine_csv_url = SCAM_URL
wine_data = pd.read_csv(wine_csv_url, header=None, nrows=None)
for value in wine_data.values:
    print(value[0])
    oracle.storeData('scam_<' + value[0] + '>', 'boolean', True, minimalFee=2000000)

##Add basic data provider info

oracle.storeData('data_provider_version', 'integer', 0, minimalFee=2000000)
oracle.storeData('data_provider_name', 'string', 'Turtle Network', minimalFee=2000000)
oracle.storeData('data_provider_email', 'string', 'support@turtlenetwork.eu', minimalFee=2000000)
oracle.storeData('data_provider_lang_list', 'string', 'en', minimalFee=2000000)
oracle.storeData('data_provider_link', 'string', 'https://turtlenetwork.eu', minimalFee=2000000)
oracle.storeData('data_provider_description_<en>', 'string', 'Description https://turtlenetwork.eu', minimalFee=2000000)
oracle.storeData('data_provider_logo_meta', 'string', 'data:image/svg+xml;base64', minimalFee=2000000)
oracle.storeData('data_provider_logo', 'string',
                 "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHZpZXdCb3g9IjAgMCAzMCAzMCI+CiAgPGRlZnM+CiAgICA8Y2xpcFBhdGggaWQ9ImNsaXAtY3VzdG9tXzEiPgogICAgICA8cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMzAiLz4KICAgIDwvY2xpcFBhdGg+CiAgPC9kZWZzPgogIDxnIGlkPSJjdXN0b21fMSIgZGF0YS1uYW1lPSJjdXN0b20g4oCTIDEiIGNsaXAtcGF0aD0idXJsKCNjbGlwLWN1c3RvbV8xKSI+CiAgICA8cmVjdCB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIGZpbGw9IiNmZmYiLz4KICAgIDxnIGlkPSJHcm91cF8xIiBkYXRhLW5hbWU9Ikdyb3VwIDEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuMzU5IDAuNjU3KSI+CiAgICAgIDxwYXRoIGlkPSJQYXRoXzgiIGRhdGEtbmFtZT0iUGF0aCA4IiBkPSJNNDAyLjU2LTM2OC4zbC0uMTY0LjYxNiwxLjE2NiwxLjY2OS4zMzcuMTc1aDQuMzc2bC4zMjctLjE3NSwxLjE2OC0xLjY2OS0uMTU5LS42MTZBOC4wNzMsOC4wNzMsMCwwLDAsNDAyLjU2LTM2OC4zWiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTM5NC42NyAzNzAuMDc5KSIgZmlsbD0iIzE2NTMxNiIvPgogICAgICA8cGF0aCBpZD0iUGF0aF85IiBkYXRhLW5hbWU9IlBhdGggOSIgZD0iTTY1NC4yMTUtMzExLjAzOGwtMS4xMDYsMS41Njl2LjUyOWwxLjgxNCwyLjU2LjM0NC4yMTFoM2wuMjI2LS41NzRhMTEuNDc3LDExLjQ3NywwLDAsMC0zLjY4LTQuMzkxWiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTYzOC41MTggMzEzLjY4NykiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfMTAiIGRhdGEtbmFtZT0iUGF0aCAxMCIgZD0iTTY1OS42NzMtMTExLjk3bC0uNzUxLS4yNjlINjU1LjgzbC0uMjguMTUyLTEuODYxLDIuNjI2di41NDhsMS44NjEsMi42MS4yOC4xNjFoNC40NDJsLjUtLjQ4MkExNS41MywxNS41MywwLDAsMCw2NTkuNjczLTExMS45N1oiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02MzkuMDgxIDEyMC4yMzcpIiBmaWxsPSIjMTY1MzE2Ii8+CiAgICAgIDxwYXRoIGlkPSJQYXRoXzExIiBkYXRhLW5hbWU9IlBhdGggMTEiIGQ9Ik02NTkuODYxLDEyNy45MTRoLTQuNDE4bC0uMzQ3LjE4Mi0xLjg0MiwyLjYzdi41MWwxLjg0MiwyLjYxLjM0Ny4xNzNoMy4wODhsLjcyNi0uMjQ4YTE2LjI0NCwxNi4yNDQsMCwwLDAsMS4xMDctNS4zMTlaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjM4LjY1OCAtMTEzLjMzOSkiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfMTIiIGRhdGEtbmFtZT0iUGF0aCAxMiIgZD0iTTY1OC43NzEsMzY5LjIyaC0zLjAxNGwtLjI3NC4xNTYtMS44NTksMi42MDl2LjU0bDEuMSwxLjU2Ni42MTEuMDgxQTEyLjQ0NCwxMi40NDQsMCwwLDAsNjU5LDM2OS44MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjM5LjAxOSAtMzQ4LjAzOCkiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfMTMiIGRhdGEtbmFtZT0iUGF0aCAxMyIgZD0iTTQwMy43OTMsNDg5LjQzNWwtLjI3OS4xMzUtMS4yMSwxLjY4LjE1NC42MzZhOC4zNDcsOC4zNDcsMCwwLDAsNy4wNywwbC4xNDctLjYzNi0xLjE4MS0xLjY4LS4yODEtLjEzNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0zOTQuNTggLTQ2NC45NikiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfMTQiIGRhdGEtbmFtZT0iUGF0aCAxNCIgZD0iTTIyNy40NjUsMzc0LjUzOGwuNTc4LS4xLDEuMTM1LTEuNTU5di0uNWwtMS44NjUtMi42NC0uMy0uMTVoLTMuMDIybC0uMjExLjU2QTExLjY2MywxMS42NjMsMCwwLDAsMjI3LjQ2NSwzNzQuNTM4WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIyMC45NDYgLTM0OC4zOTEpIiBmaWxsPSIjMTY1MzE2Ii8+CiAgICAgIDxwYXRoIGlkPSJQYXRoXzE1IiBkYXRhLW5hbWU9IlBhdGggMTUiIGQ9Ik0xNjEuNDc5LDEyOC44ODFsLjQ2Mi0uNTA3aDQuNDM1bC4zNTIuMTY0LDEuODYsMi42MzN2LjUwNmwtMS44NiwyLjYzMi0uMy4xNjFoLTMuMTEybC0uNzQ5LS4yNTJBMTQuODcyLDE0Ljg3MiwwLDAsMSwxNjEuNDc5LDEyOC44ODFaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYwLjM1IC0xMTMuNzg2KSIgZmlsbD0iIzE2NTMxNiIvPgogICAgICA8cGF0aCBpZD0iUGF0aF8xNiIgZGF0YS1uYW1lPSJQYXRoIDE2IiBkPSJNMTYxLjc3Mi0xMTEuNDZsLjc0My0uMjI4aDMuMTA4bC4zMTQuMTc2LDEuODMyLDIuNjJ2LjUxMmwtMS44MzIsMi42LS4zMTQuMTc2LTQuNDU5LjAzNS0uNTEtLjUxM0ExNy43NjIsMTcuNzYyLDAsMCwxLDE2MS43NzItMTExLjQ2WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTE1OS41NDggMTE5LjcwMSkiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfMTciIGRhdGEtbmFtZT0iUGF0aCAxNyIgZD0iTTIyNy4zMS0zMTEuMTczbC41NjguMUwyMjktMzA5LjUxMVYtMzA5bC0xLjgzNiwyLjYtLjMyMi4xN2gtM2wtLjI0NC0uNTU2QTExLjgwNSwxMS44MDUsMCwwLDEsMjI3LjMxLTMxMS4xNzNaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjIwLjc2OCAzMTMuNzI0KSIgZmlsbD0iIzE2NTMxNiIvPgogICAgICA8cGF0aCBpZD0iUGF0aF8xOCIgZGF0YS1uYW1lPSJQYXRoIDE4IiBkPSJNMzc5LjU4Ni0yMzJoNC40NjRsLjMxNi4yLDEuODI0LDIuNjA3di41MTdsLTEuNzgxLDIuNTA1LS4zNTkuMjMzaC00LjQ2NGwtLjMtLjEyNi0xLjgzMy0yLjYxMnYtLjUxN2wxLjgzMy0yLjYwN1oiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0zNzAuNDA2IDIzNi43MTYpIiBmaWxsPSIjMTY1MzE2Ii8+CiAgICAgIDxwYXRoIGlkPSJQYXRoXzE5IiBkYXRhLW5hbWU9IlBhdGggMTkiIGQ9Ik0zNzcsMTEuMTU5bDEuODUtMi42MDkuMzIzLS4xODZoNC40NGwuMzE4LjE4NiwxLjgzNCwyLjYwOXYuNDg5bC0xLjgzNCwyLjYwOC0uMzE4LjIwOWgtNC40NGwtLjMyMy0uMTc0TDM3NywxMS42NzdaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzY5Ljk3IDIuOTM2KSIgZmlsbD0iIzE2NTMxNiIvPgogICAgICA8cGF0aCBpZD0iUGF0aF8yMCIgZGF0YS1uYW1lPSJQYXRoIDIwIiBkPSJNMzc3LDI1Mi4ybDEuODc4LTIuNjMzLjI3NS0uMTQ0aDQuNDcxbC4yNjMuMTQ0LDEuODY0LDIuNjMzdi41bC0xLjgsMi41NTEtLjMzMS4yMzJoLTQuNDcxbC0uMjc1LS4xNjVMMzc3LDI1Mi43WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTM2OS45NyAtMjMxLjUyMikiIGZpbGw9IiMxNjUzMTYiLz4KICAgICAgPHBhdGggaWQ9IlBhdGhfNiIgZGF0YS1uYW1lPSJQYXRoIDYiIGQ9Ik05Ny40MzMtNDI2LjgyOWwuNzE1LS4yMjgtLjI5My0uNzI2YTEyLjc0OCwxMi43NDgsMCwwLDEsNC4zMDgtNS4wOWwuOTE3LjE0Mi4yMTktLjg0NWE5LjI4NCw5LjI4NCwwLDAsMSw4LjUzOCwwbC4xODMuODQ1Ljk5Mi0uMTM4YTEyLjg3NSwxMi44NzUsMCwwLDEsNC4yNjEsNS4wNjNsLS4yOS43NjEuNzUzLjIzMmExNy4zNjIsMTcuMzYyLDAsMCwxLDEuMjM5LDYuMDEzbC0uNTQ3LjUzNi41NDcuNTc0YTE2Ljc4MywxNi43ODMsMCwwLDEtMS4yNDEsNi4wMTJsLS43NTguMjMzLjMuNzU2YTEzLjI4NCwxMy4yODQsMCwwLDEtNC4zLDUuMDVsLS45MS0uMTQxLS4yNDguODUzYTkuNjI4LDkuNjI4LDAsMCwxLTguNTE3LDBsLS4yNDEtLjg1OC0uOTE1LjE4OWExMy41MTQsMTMuNTE0LDAsMCwxLTQuMjgzLTUuMWwuMzEzLS43NjEtLjc5My0uMjEzYTIxLjExMywyMS4xMTMsMCwwLDEtMS4yMzEtNi4wMThsLjYxMS0uNTU5LS42MTEtLjU5MUExNy44NTIsMTcuODUyLDAsMCwxLDk3LjQzMy00MjYuODI5WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTk2LjE1OSA0MzQuNjA0KSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjNzA3MDcwIiBzdHJva2Utd2lkdGg9IjAuNSIvPgogICAgPC9nPgogIDwvZz4KPC9zdmc+Cg==",
                 minimalFee=2000000)

def add_token(ticker, status, email, asset_id, description='Description', link='example.com', logo='', version=0):
    data = [{
        'type': 'string',
        'key': 'ticker_<' + asset_id + '>',
        'value': ticker
    },
        {
            'type': 'integer',
            'key': 'status_<' + asset_id + '>',
            'value': status
        },
        {
            'type': 'integer',
            'key': 'version_<' + asset_id + '>',
            'value': version
        },
        {
            'type': 'string',
            'key': 'email_<' + asset_id + '>',
            'value': email
        },

        {
            'type': 'string',
            'key': 'description_<en>_<' + asset_id + '>',
            'value': description
        },
        {
            'type': 'string',
            'key': 'link_<' + asset_id + '>',
            'value': link
        }
    ]
    if logo == '':
        data.append({
            'type': 'string',
            'key': 'logo_<' + asset_id + '>',
            'value': logo})
    else:
        data.append({
            'type': 'string',
            'key': 'logo_<' + asset_id + '>',
            'value': 'data:image/svg+xml;base64,' + logo
        })

    ticker_tx = address.dataTransaction(data, baseFee=2000000, minimalFee=2500000)

    print(ticker_tx)


###
# SCAM = -2,
# SUSPICIOUS = -1,
# NOT_VERIFY = 0,
# DETAILED = 1,
# VERIFIED = 2

# TODO: Status 2 seems to be when an asset is active and verified
with open('oracledata.json') as json_file:
    verified = json.load(json_file)

for token in verified:
    add_token(token['ticker'], token['status'], token['email'], token['asset_id'], token['description'], token['link'], token['logo'], token['version'])

# Not verified
add_token('BTN', 0, '------', 'ExbYSuz4DZwf9grp3K8s3CSbNtE9fob2DtTKgbLGFXsJ')
add_token('FR', 0, '------', '4xUv25qFsjQ1Gd6oCmzU14FoPMSDXrwub5PbKRgETf97')
add_token('KA', 0, '------', '5Dy1qVUzEwq6WEUGMy7CkkkbmFuxb2RTBRfs4JKc5b88')
add_token('MLT', 0, '------', '7jcY6DDYsSo7NuZEAruWhrB5apebA2cERhrBx6RFk5tL')
add_token('HN', 0, '------', '3GvqjyJFBe1fpiYnGsmiZ1YJTkYiRktQ86M2KMzcTb2s')
add_token('MN', 0, '------', 'DfutD8DdUhDphHoaMds2RQhw7oCmsf7W41s2zR5ZDq9F')
