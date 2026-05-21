# 💱 Simple Currency Converter

A lightweight command-line currency converter written in Python that fetches live exchange rates and converts between any two supported currencies in real time.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Supported Currencies](#supported-currencies)
- [Example Session](#example-session)
- [Error Handling](#error-handling)

---

## Overview

This script connects to the [Open Exchange Rates API](https://open.er-api.com) to retrieve the latest exchange rates and allows you to interactively convert amounts between any two currencies — all from your terminal.

---

## Features

- 🌐 **Live exchange rates** — fetches real-time data from `open.er-api.com`
- 🔄 **Multi-currency support** — works with every currency code the API provides
- ♾️ **Looped conversions** — convert multiple times in a single session
- 🛡️ **Input validation** — catches invalid currency codes and non-numeric amounts gracefully
- 🖥️ **Zero configuration** — no API key or sign-up required

---

## Usage

Run the script directly from your terminal:

```bash
python currency_converter.py
```

You will be prompted to enter:

| Prompt | Description |
|---|---|
| `From currency code` | The currency you are converting **from** (e.g. `USD`) |
| `To currency code` | The currency you are converting **to** (e.g. `KES`) |
| `Amount` | The numeric amount to convert |

After each conversion, you can choose to convert again or exit.

---

## How It Works

1. **Fetch rates** — on startup, the script makes a single `GET` request to:
   ```
   https://open.er-api.com/v6/latest
   ```
   This returns a JSON object containing exchange rates for 160+ currencies, all relative to **USD** as the base.

2. **Cross-rate calculation** — to convert between any two non-USD currencies, the script uses the following formula:

   ```
   result = (amount / rate[from_currency]) * rate[to_currency]
   ```

   This converts the input amount to USD first, then to the target currency.

3. **Interactive loop** — after displaying the result, the user is asked whether to perform another conversion. The loop continues until the user enters anything other than `y`.

---

## Supported Currencies

The API supports **160+ currencies**. Some popular ones include:

| Code | Currency |
|---|---|
| `USD` | US Dollar |
| `EUR` | Euro |
| `GBP` | British Pound |
| `JPY` | Japanese Yen |
| `CAD` | Canadian Dollar |
| `AUD` | Australian Dollar |
| `CNY` | Chinese Yuan |
| `INR` | Indian Rupee |
| `KES` | Kenyan Shilling |
| `ZAR` | South African Rand |

For a full list, refer to the [Open Exchange Rates currency list](https://open.er-api.com/v6/latest).

---

## Example Session

```
Simple Currency Converter
Getting exchange rates...
Got rates successfully!
Popular: USD EUR GBP JPY CAD AUD CNY INR

Enter details:
From currency code (eg. USD): USD
To currency code (e.g. EUR): KES
Amount in USD: 100

Result: 100.0 USD = 12950.00 KES
Rate: 1 USD = 129.5000 KES

Convert again? (y/n): y

Enter details:
From currency code (eg. USD): GBP
To currency code (e.g. EUR): JPY
Amount in GBP: 50

Result: 50.0 GBP = 9408.73 JPY
Rate: 1 GBP = 188.1746 JPY

Convert again? (y/n): n
Thanks for playing!
```

---

## Error Handling

| Scenario | Behaviour |
|---|---|
| No internet / API unreachable | Prints an error message and exits cleanly |
| Invalid currency code entered | Notifies the user and re-prompts without crashing |
| Non-numeric amount entered | Notifies the user and re-prompts without crashing |

---
