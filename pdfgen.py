import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

#Haemotology
category_A = {"Blood Group":{"Result":"","Reference Range":"-NA-"},"Platelet Count Cell Counter": {"Result": "","Reference Range": "150-400","Unit": "10^3/ul"},"Differential Leucocyte Count": {"Neutrophil Microscopy": {"Result": "","Reference Range": "40-80","Unit": "%"},"Lymphocyte Microscopy": {"Result": "","Reference Range": "24-44","Unit": "%"},"Eosinophils Microscopy": {"Result": "","Date": "01/06/2024","Unit": "%"},"Monocytes Microscopy": {"Result": "","Date": "02/10/2024","Unit": "%"},"Basophils Microscopy": {"Result": "","Reference Range": "0-1","Unit": "%"}},"Absolute Neutrophil Count": {"Result": "","Reference Range": "2.0-7.0","Unit": "X 10^3/uL"},"Absolute Lymphocyte Count": {"Result": "","Reference Range": "1.5-4.0","Unit": "X 10^3/uL"},"Absolute Eosinophil Count": {"Result": "","Reference Range": "0.02-0.50","Unit": "X 10^3 cells/uL"},"Absolute Basophil Count": {"Result": "","Reference Range": "0.00-0.00","Unit": "X 10^3 cells/uL"},"Absolute Monocyte Count": {"Result": "","Reference Range": "0.2-1.0","Unit": "X 10^3/uL"},"PDW": {"Result": "","Reference Range":"8-12"},"PCT": {"Result": "","Reference Range":"0-0.5"},"Mean Platelet Volume": {"Result": "","Reference Range":"9-13","Unit":"fL"},"RDW-CV Dc Detection Method (Calculated)": {"Result": "","Reference Range": "11.5-14.5","Unit": "%"},"Erythrocyte Sedimentation Westergren Rate (ESR)": {"Result": "","Reference Range": "0-20","Unit": "mm/h"},"RDW-SD Cell Counter": {"Result": "","Reference Range": "39.0-46.0","Unit": "fl"}}

#Biochemistry
category_B = {
    "Sodium, Serum Ion Selective Electrode": {"Result": "","Reference Range": "136.0-149.0","Unit": "mmol/L"},
    "Potassium, Serum Ion Selective Electrode": {"Result": "","Reference Range": "3.50-5.50","Unit": "mmol/L"},
    "Chloride Ion Selective Electrode": {"Result": "","Reference Range": "98.0-109.0","Unit": "mmol/L"},
    "Calcium [Ionic] Ion Selective Electrode": {"Result": "","Reference Range": "1.15-1.29","Unit": "mmol/L"},
    "Calcium, Serum Arsenazo": {"Result": "","Reference Range": "8.40-10.40","Unit": "mg/dL"},
    "Total Cholesterol CHOD-PAP": {"Result": "","Reference Range": "0.0-200.0","Unit": "mg/dL"},
    "Triglyceride GPO (Trinders)": {"Result": "","Reference Range": "35.0-135.0","Unit": "mg/dl"},
    "HDL Cholesterol Direct (PVS/PEGME precipitation & Trinder reaction)": {"Result": "","Reference Range": "35.3-79.5","Unit": "mg/dL"},
    "VLDL Cholesterol calculated": {"Result": "","Reference Range": "4.7-21.1","Unit": "mg/dL"},
    "LDL Cholesterol Direct (PVS/PEGME precipitation & Trinder reaction)": {"Result": "","Reference Range": "0-100","Unit": "mg/dL"},
    "Total / HDL Cholesterol Ratio calculated": {"Result": "","Reference Range": "0.0-5.0","Unit": "Ratio"},
    "LDL/HDL Cholestrol Ratio calculated": {"Result": "","Reference Range": "0.00-3.55","Unit": "Ratio"},
    "Non HDL Cholesterol": {"Result": "","Reference Range": "0-130","Unit": "mg/dL"},
    "CRP (C-Reactive Protein)-Quantitative Turbidimetric Immunoassay": {"Result": "","Reference Range": "0-5","Unit": "mg/L"},
    "Iron, Serum Colorimetric": {"Result": "","Reference Range": "50.00-170.00","Unit": "ug/dL"},
    "Unsaturated Iron Binding Capacity": {"Result": "","Reference Range": "110.0-370.0","Unit": "ug/dL"},
    "Total Iron Binding capacity": {"Result": "","Reference Range": "250-400","Unit": "ug/dL"},
    "Transferrin Saturation %": {"Result": "","Reference Range": "12-45","Unit": "%"},
    "Urea, Blood Urease-GLDH": {"Result": "","Reference Range": "13.00-43.00","Unit": "mg/dL"},
    "Blood Urea Nitrogen (BUN) Spectro-photometry": {"Result": "","Reference Range": "7.00-18.00","Unit": "mg/dL"},
    "Creatinine, Serum Jaffe Kinetic": {"Result": "","Reference Range": "0.60-1.10","Unit": "mg/dL"},
    "Uric Acid, Serum Uricase": {"Result": "","Reference Range": "2.50-6.80","Unit": "mg/dL"},
    "BUN / Creatinine Ratio": {"Result": "","Reference Range": "0.8-1.3","Unit": "mg/dL"},
    "Urea / Creatinine Ratio": {"Result": "","Reference Range": "1.8-7.1","Unit": "mg/dL"},
    "Bilirubin, Total Diazo": {"Result": "","Reference Range": "0.30-1.20","Unit": "mg/dL"},
    "Bilirubin, Direct Diazo": {"Result": "","Reference Range": "0.00-0.20","Unit": "mg/dL"},
    "Bilirubin, Indirect": {"Result": "","Reference Range": "0.10-1.00","Unit": "mg/dL"},
    "SGOT (AST), Serum IFCC without pyridoxal phosphate": {"Result": "","Reference Range": "0.00-31.00","Unit": "IU/L"},
    "SGPT (ALT), Serum IFCC without pyridoxal phosphate": {"Result": "","Reference Range": "0.00-32.00","Unit": "IU/L"},
    "Alkaline Phosphatase (ALP), Serum PNP AMP Kinetic": {"Result": "","Reference Range": "42.0-98.0","Unit": "U/L"},
    "Protein, Total Biuret": {"Result": "","Reference Range": "6.0-8.0","Unit": "g/dL"},
    "Albumin, Serum Bromo Cresol Green (BCG)": {"Result": "3.7","Reference Range": "3.20-5.00","Unit": "g/dL"},
    "Globulin": {"Result": "","Reference Range": "2.00-3.50","Unit": "g/dL"},
    "Microalbumin Immunoturbidity": {"Result": "","Reference Range": "0.0-30.0","Unit": "mg/L"},
    "Creatinine, Random Urine Jaffe Kinetic": {"Result": "","Reference Range": "20.0-370.0","Unit": "mg/dL"},
    "Microalbumin/Creatinine Ratio": {"Result": "","Reference Range": "0-30.0","Unit": "mg/g creat"},
    "Arthritis Screen": {"Result": "","Reference Range": "","Unit": ""},
    "Calcium": {"Result": "","Reference Range": "8.5-10.5","Unit": "mg/dL"},
    "Phosphorous Ammonium molybdate UV": {"Result": "","Reference Range": "2.50-5.00","Unit": "mg/dL"},
    "Rheumatoid Factor (RA Factor) - Quantitative Immunoturbidimety": {"Result": "","Reference Range": "0-30","Unit": "IU/ml"},
    "Sodium (Urine) Ion Selective Electrode": {"Result": "","Reference Range": "40-220","Unit": "mmol/L"},
    "Potassium (Urine Spot Test)": {"Result": "","Reference Range": "25-125","Unit": "mmol/day"},
    "Chloride (Urine Spot Test)": {"Result": "","Reference Range": "110-250","Unit": "mmol/l/day"}
}

#Immunosay
category_C = {
    "Free Triiodothyronine (FT3) Chemiluminescence Immunoassay (CLIA)": {"Result": "","Reference Range": "1.76-4.20","Unit": "pg/mL"},
    "Free Thyroxine (FT4) Chemiluminescence Immunoassay (CLIA)": {"Result": "","Reference Range": "0.89-1.76","Unit": "ng/dL"},
    "Vitamin B12 Level Chemiluminescence Immunoassay(CLIA)": {"Result": "","Reference Range": "211.0-911.0","Unit": "pg/mL"},
    "Triiodothyronine, Total (T3) Chemiluminescence Immunoassay (CLIA)": {"Result": "","Reference Range": "58.6-156.2","Unit": "ng/dL"},
    "Thyroxine, Total (T4) Chemiluminescence Immunoassay (CLIA)": {"Result": "","Reference Range": "4.8-10.4","Unit": "ug/dL"},
    "Thyroid Stimulating Hormone (TSH) Chemiluminescence Immunoassay (CLIA)": {"Result": "","Reference Range": "0.35-5.50","Unit": "ulU/mL"}
}

#Clinical Pathlogy
category_D = {
    "Colour": {"Result": "", "Reference Range": "Pale Yellow", "Unit": ""},
    "Appearance": {"Result": "", "Reference Range": "Clear", "Unit": ""},
    "pH Double Indicators Test": {"Result": "", "Reference Range": "4.6-8.0", "Unit": ""},
    "Specific Gravity Refractometric": {"Result": "", "Reference Range": "1.003-1.030", "Unit": ""},
    "Urine Protein Protein Indicator": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Urine Sugar Oxidation Reaction": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Ketones Sodium nitroprusside": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Nitrite Diazotisation Reaction": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Blood Peroxidase Reaction": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Urobilinogen Modified Ehrlich Reaction": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Urine Bilirubin Diazotisation": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "R.B.C. Microscopy": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Pus Cells": {"Result": "", "Reference Range": "0-5", "Unit": ""},
    "Epithelial Cells Microscopy": {"Result": "", "Reference Range": "0-3", "Unit": "/HPF"},
    "Casts Microscopy": {"Result": "", "Reference Range": "Negative", "Unit": "/LPF"},
    "Crystals Microscopy": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Bacteria Microscopy": {"Result": "", "Reference Range": "Negative", "Unit": ""},
    "Others": {"Result": "", "Reference Range": "", "Unit": ""}
}


categories = {
    'Haemotology': category_A,
    'Biochemistry': category_B,
    'Immunosay': category_C,
    'Clinical Pathlogy': category_D
}


def generate_random_data(details):
    reference_range = details.get('Reference Range')
    exceptions = details.get('Exceptions', {})
    
    if reference_range:
        if reference_range.lower() == "negative":
            if random.random() < 0.1:
                return "Positive", "Abnormal"
            else:
                return "Negative", "Normal"
        elif reference_range.lower() == "pale yellow":
            if random.random() < 0.1:
                return "Dark Yellow", "Abnormal"
            else:
                return "Pale Yellow", "Normal"
        elif reference_range.lower() == "clear":
            if random.random() < 0.1:
                return "Cloudy", "Abnormal"
            else:
                return "Clear", "Normal"
        elif reference_range.lower() == "-na-":
            blood_groups = ["A", "B", "AB", "O"]
            random_value = random.choice(blood_groups)
            return random_value,""
        else:
            try:
                min_value, max_value = map(float, reference_range.split('-'))
                range_width = max_value - min_value
                below_threshold = min_value - 0.1 * range_width
                above_threshold = max_value + 0.1 * range_width
                random_value = random.uniform(min_value, max_value)

                for key, value in exceptions.items():
                    if key in details:
                        if value == 'above':
                            return round(random.uniform(max_value, above_threshold), 2), "Abnormal"
                        elif value == 'below':
                            return round(random.uniform(below_threshold, min_value), 2), "Abnormal"
                        elif value == 'normal':
                            return round(random_value, 2), "Normal"

                if random.random() < 0.1:
                    return round(random.uniform(below_threshold, min_value), 2), "Abnormal"
                elif random.random() < 0.1:
                    return round(random.uniform(max_value, above_threshold), 2), "Abnormal"
                else:
                    return round(random_value, 2), "Normal"
            except (ValueError, AttributeError):
                return "", ""
    else:
        return "", ""






def create_pdf(filename, lab,categories):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    data = []
    story = []
    data.append(["Test", "Status", "Result", "Reference Range", "Unit"])
    
    for category, tests in categories.items():
        category_header_style = ParagraphStyle(name='CategoryHeader', fontName='Helvetica-Bold', underline=True,fontSize=12)
        category_header = Paragraph(category, category_header_style)
        
        data.append([category_header, "", "", "", ""])
        for test, details in tests.items():
            result,status = generate_random_data(details)
            test_name = test
            test_name = Paragraph(test_name, getSampleStyleSheet()["Normal"])
            result = Paragraph(str(result), getSampleStyleSheet()["Normal"])
            ref_range = Paragraph(details.get('Reference Range', ''), getSampleStyleSheet()["Normal"])
            unit = Paragraph(details.get('Unit', ''), getSampleStyleSheet()["Normal"])
            status = Paragraph(status, getSampleStyleSheet()["Normal"])
            row = [test_name, status, result, ref_range, unit]
            data.append(row)
            data.append([Spacer(1, 0.1 * inch)])
            
    # Determine column widths
    col_widths = [180, 80, 80, 100, 100]
    
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('GRID', (0, 0), (-1, -1), 0, colors.white)]))

    story.append(table)
    doc.build(story, onFirstPage=draw_header, onLaterPages=draw_header)

def draw_header(canvas, doc):
    header_image_path = "images/header_C.png"
    canvas.drawImage(header_image_path, 35, 710, width=540, height=80)
    
    footer_image_path = "images/footer_C.png"
    canvas.drawImage(footer_image_path,130,0,width=350,height=80)


def create_pdf_with_shuffled_categories(filename, lab):
    shuffled_category_names = list(categories.keys())
    random.shuffle(shuffled_category_names)
    
    shuffled_categories = {category: categories[category] for category in shuffled_category_names}
    
    create_pdf(filename, lab, shuffled_categories)

for i in range(1, 21):
    filename = f"report_{i}.pdf"
    create_pdf_with_shuffled_categories(filename, "Lab XYZ")
print("Done")