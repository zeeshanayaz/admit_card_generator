# AMFS Admit Card Generator

Python utility to generate examination admit cards from an Excel student list.

## Features

- Reads student records from `.xlsx`
- Generates one admit card per student
- Automatically creates a PDF
- Exactly 2 admit cards per A4 page
- Uses the AMFS logo
- Uses a male/female placeholder based on the `Gender` column
- Designed for printing and cutting
- Simple desktop interface

## Excel columns

The program recognizes these column names:

- Name of Student / Student Name / Name
- Class / Class Name / Grade
- Roll No / Roll No. / Roll Number
- Father's Name / Father Name
- Mother's Name / Mother Name
- Contact No / Contact / Phone / Mobile
- Gender / Sex

Column matching is case-insensitive and ignores spaces/punctuation.

Example:

| Name of Student | Class | Roll No | Father's Name | Mother's Name | Contact No | Gender |
|---|---|---|---|---|---|---|
| MD JAMAL | STD V-A | 1 | MD IMTIAZ | SITARA KHATOON | 9995000009 | Male |
| Ayesha Khan | STD V-A | 2 | MD ASLAM | ZEHRA KHATOON | 9995000010 | Female |

## Install

Open Command Prompt in this folder:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

## Run desktop application

```bash
python app.py
```

Select the Excel file and click:

`Generate Admit Cards PDF`

The PDF will be created in the same folder as the Excel file as:

`AMFS_Admit_Cards.pdf`

## Command-line usage

```bash
python admit_card_generator.py students.xlsx
```

Or:

```bash
python admit_card_generator.py students.xlsx -o output/admit_cards.pdf
```

## Important

The current template uses the information provided for this project:

School:
AL MUSLEH FOUNDATION SCHOOL

Examination:
Mid-Term Examination 2026-27

The sample admit card supplied by the user was used only as a visual reference. The generated design is adapted for AMFS and uses 2 cards per A4 page.
