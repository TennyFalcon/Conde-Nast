import pandas as pd
import csv
import xlwt
from xlwt import Workbook
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Environment, FileSystemLoader
from datetime import date


input_path = input('Enter the input files path: ')
input_path = str(input_path) + '/'
output_path = input('Enter the output files path: ')
output_path = str(output_path) + '/'
source_files = []
target_files = []

for r,d,f in os.walk(input_path):
    for file in f:
        if '.csv' in file:
            target_files.append(file)
        elif '.xlsx' in file:
            source_files.append(file)


for s_file in source_files:
    positions = []
    res = None
    for i in range(0, len(s_file)):
        if s_file[i] == '_':
            res = i + 1
            positions.append(res)
    countryname = s_file[positions[0]:positions[1]-1]

    for t_file in target_files:
        if countryname in t_file:
            source_file = str(input_path) + str(s_file)
            target_file = str(input_path) + str(t_file)

            # Path
            path = os.path.join(output_path, countryname)

            # Create the directory
            # 'GeeksForGeeks' in
            # '/home / User / Documents'
            os.mkdir(path)

            output_file_path = str(output_path) + str(countryname) + '/'

            # Setting range and target_filename
            if countryname == 'Japan':
                target_filename1 = countryname
                ranges = 999999
            elif countryname == 'Italy':
                target_filename1 = countryname
                ranges = 999999
            elif countryname == 'US':
                target_filename1 = countryname
                ranges = 999999
            elif countryname == 'India':
                target_filename1 = countryname
                ranges = 999999
            elif countryname == 'France':
                target_filename1 = countryname
                ranges = 999999
            elif countryname == 'China':
                target_filename1 = countryname
                ranges = 99999
            elif countryname == 'Russia':
                target_filename1 = countryname
                ranges = 99999
            elif countryname == 'Taiwan':
                target_filename1 = countryname
                ranges = 99999
            else:
                target_filename1 = countryname
                ranges = 9999

            # xlsx file to csv
            df1 = pd.read_excel(source_file,sheet_name='Consolidated Template')
            new_df = df1.drop([0, 1, 2, 3])
            new_df.replace("COUTURE, LEATHER GOODS & EYEWEAR", "COUTURE LEATHER GOODS & EYEWEAR", inplace=True)
            new_df.replace("COUTURE, LEATHER GOODS & EYEWEAR Total", "COUTURE LEATHER GOODS & EYEWEAR Total", inplace=True)
            new_df.to_csv(str(output_file_path) + 'BR_consolidated_sheet_data.csv', index=False, header=False, encoding='UTF-8')

            with open(str(output_file_path) + 'BR_consolidated_sheet_data.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)

            for y in range(0, 648):
                for x in range(1, 4):
                    if data[y][x] == '':
                        data[y][x] = '-'
                for z in range(4, 9):
                    if data[y][z] == '-':
                        data[y][z] = '0'
                    elif data[y][z] == '':
                        data[y][z] = '0'

            file = open(str(output_file_path) + 'BR_source' + str(target_filename1) + '.csv', 'w+', newline='')

            with file:
                write = csv.writer(file)
                write.writerows(data)

            # Target CSV file modification
            fin = open(target_file, 'r')
            target_file_final = str(output_file_path) + 'BR_target_' + str(target_filename1) + '.csv'
            fout = open(target_file_final, 'w')

            for line in fin:
                line1 = line.replace('|', ',')
                line2 = line1.replace('COUTURE, LEATHER GOODS & EYEWEAR', 'COUTURE LEATHER GOODS & EYEWEAR')
                fout.write(line2)

            fin.close()
            fout.close()

            #Creating xlsx sheet for writing the results
            # Workbook is created
            wb = Workbook()

            #Result_sheet1
            sheetname1 = target_filename1 + str('_Validation')
            sheet1 = wb.add_sheet(sheetname1)
            first_col = sheet1.col(0)
            first_col.width = 256 * 30
            style = xlwt.easyxf('font: bold 1, color red;')
            tall_style = xlwt.easyxf('font:bold 1, height 720;')
            first_row = sheet1.row(0)
            first_row.set_style(tall_style)

            sheet1.write(0, 0, 'Validation Name')
            sheet1.write(0, 1, 'Test Result')
            sheet1.write(0, 2, 'Comments (If FAIL)')
            sheet1.write(1, 0, 'Source vs Target Validation')
            sheet1.write(2, 0, 'Target vs Source Validation')
            sheet1.write(3, 0, 'Range Validation for 2020_Q1')
            sheet1.write(4, 0, 'Range Validation for 2020_Q2')
            sheet1.write(5, 0, 'Range Validation for 2020_Q3')
            sheet1.write(6, 0, 'Range Validation for 2020_Q4')
            sheet1.write(7, 0, 'Parent column empty/null check')
            sheet1.write(8, 0, 'Parent count check')
            sheet1.write(9, 0, 'Platform Validation')
            sheet1.write(10, 0, 'Non numeric value check for 2020_Q1')
            sheet1.write(11, 0, 'Non numeric value check for 2020_Q2')
            sheet1.write(12, 0, 'Non numeric value check for 2020_Q3')
            sheet1.write(13, 0, 'Non numeric value check for 2020_Q4')
            sheet1.write(14, 0, 'Non numeric value check for Total')
            '''
            sheet1.write(15, 0, 'Negative value check for Q1')
            sheet1.write(16, 0, 'Negative value check for Q2')
            sheet1.write(17, 0, 'Negative value check for Q3')
            sheet1.write(18, 0, 'Negative value check for Q4')
            sheet1.write(19, 0, 'Negative value check for Total')
            '''

            #Result_sheet2
            sheetname2 = 'SourceVsTarget'
            sheet2 = wb.add_sheet(sheetname2)

            #Result_sheet3
            sheetname3 = 'TargetVsSource'
            sheet3 = wb.add_sheet(sheetname3)
            '''
            #Result_sheet4
            sheetname4 = 'Missing_Target'
            sheet4 = wb.add_sheet(sheetname4)

            #Result_sheet5
            sheetname5 = 'Missing_Source'
            sheet5 = wb.add_sheet(sheetname5)
            '''

            # source vs target csv validation code
            file1 = open(str(output_file_path) + 'BR_source' + str(target_filename1) + '.csv', 'r')
            file2 = open(target_file_final , 'r')

            f1 = file1.readlines()
            f2 = file2.readlines()
            file1.close()
            file2.close()
            #missing_target = open(str(output_file_path) + 'BR_missing_target.csv', 'w')
            #missing_source = open(str(output_file_path) + 'BR_missing_source.csv', 'w')
            target_miss_count = 0
            source_miss_count = 0
            line_count = 0
            missing_line_count = 0
            error_count = 0

            for line in f1:
                if line not in f2:
                    #missing_target.write(line)
                    sheetname4 = 'Missing_Target'
                    sheet4 = wb.add_sheet(sheetname4)
                    sheet4.write(missing_line_count, 0, 'Line' + str(missing_line_count))
                    sheet4.write(missing_line_count, 1, line)
                    missing_line_count = missing_line_count + 1
                    target_miss_count = target_miss_count + 1
                    error_count = error_count + 1
                    if line_count == 0:
                        sheet2.write(line_count, 0, 'Header')
                        sheet2.write(line_count, 1, 'FAIL')
                    else:
                        sheet2.write(line_count, 0, 'Line' + str(line_count))
                        sheet2.write(line_count, 1, 'FAIL')
                else:
                    if line_count == 0:
                        sheet2.write(line_count, 0, 'Header')
                        sheet2.write(line_count, 1, 'PASS')
                    else:
                        sheet2.write(line_count, 0, 'Line' + str(line_count))
                        sheet2.write(line_count, 1, 'PASS')
                line_count = line_count + 1

            line_count = 0
            missing_line_count = 0
            for line in f2:
                if line not in f1:
                    #missing_source.write(line)
                    sheetname5 = 'Missing_Source'
                    sheet5 = wb.add_sheet(sheetname5)
                    sheet5.write(missing_line_count, 0, 'Line' + str(missing_line_count))
                    sheet5.write(missing_line_count, 1, line)
                    missing_line_count = missing_line_count + 1
                    source_miss_count = source_miss_count + 1
                    error_count = error_count + 1
                    if line_count == 0:
                        sheet3.write(line_count, 0, 'Header')
                        sheet3.write(line_count, 1, 'FAIL')
                    else:
                        sheet3.write(line_count, 0, 'Line' + str(line_count))
                        sheet3.write(line_count, 1, 'FAIL')
                else:
                    if line_count == 0:
                        sheet3.write(line_count, 0, 'Header')
                        sheet3.write(line_count, 1, 'PASS')
                    else:
                        sheet3.write(line_count, 0, 'Line' + str(line_count))
                        sheet3.write(line_count, 1, 'PASS')
                line_count = line_count + 1

            if target_miss_count == 0:
                sheet1.write(1, 1, 'PASS')
            else:
                sheet1.write(1, 1, 'FAIL')

            if source_miss_count == 0:
                sheet1.write(2, 1, 'PASS')
            else:
                sheet1.write(2, 1, 'FAIL')

            target_df = pd.read_csv(target_file_final, encoding="ISO-8859-1", error_bad_lines=False)

            # Range Validation for Q1
            Q1_df = target_df['2020_Q1'].where(target_df['2020_Q1'] > ranges)
            Q1_count = Q1_df.count()
            #print('Q1_error count: ' + str(Q1_count))
            if Q1_count == 0:
                sheet1.write(3, 1, 'PASS')
            else:
                sheet1.write(3, 1, 'FAIL')
                error_count = error_count + 1
                Q1_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q1.csv',
                             index=True)

            # Range Validation for Q2
            Q2_df = target_df['2020_Q2'].where(target_df['2020_Q2'] > ranges)
            Q2_count = Q2_df.count()
            #print('Q2_error count: ' + str(Q2_count))
            if Q2_count == 0:
                sheet1.write(4, 1, 'PASS')
            else:
                sheet1.write(4, 1, 'FAIL')
                error_count = error_count + 1
                Q2_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q2.csv',
                             index=True)

            # Range Validation for Q3
            Q3_df = target_df['2020_Q3'].where(target_df['2020_Q3'] > ranges)
            Q3_count = Q3_df.count()
            #print('Q3_error count: ' + str(Q3_count))
            if Q3_count == 0:
                sheet1.write(5, 1, 'PASS')
            else:
                sheet1.write(5, 1, 'FAIL')
                error_count = error_count + 1
                Q3_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q3.csv',
                             index=True)

            # Range Validation for Q4
            Q4_df = target_df['2020_Q4'].where(target_df['2020_Q4'] > ranges)
            Q4_count = Q4_df.count()
            #print('Q4_error count: ' + str(Q4_count))
            if Q3_count == 0:
                sheet1.write(6, 1, 'PASS')
            else:
                sheet1.write(6, 1, 'FAIL')
                error_count = error_count + 1
                Q4_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q4.csv',
                             index=True)

            # Parent null validation
            Parent_df = pd.read_csv(target_file_final, encoding="ISO-8859-1", error_bad_lines=False)
            Parent_null_count = Parent_df['Parent'].isna().sum()
            if Parent_null_count == 0:
                sheet1.write(7, 1, 'PASS')
                #print('Parent column does not contain any null/empty values')
            else:
                sheet1.write(7, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(7, 2, 'Parent column contains' + str(Parent_null_count) + 'null/empty values')
                #print('Parent column contains' + str(Parent_null_count) + 'null/empty values')

            # Parent null validation
            Parent_count = Parent_df['Parent'].count()
            if Parent_count == 647:
                sheet1.write(8, 1, 'PASS')
            else:
                sheet1.write(8, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(8, 2, 'Parent column count is ' + str(Parent_count) )

            # Platform validation
            a = ['Print', 'Digital (ex: Video)', 'Video', 'Business Services', '-']
            diff = set(target_df['Platform']) - set(a)
            if len(diff) == 0:
                sheet1.write(9, 1, 'PASS')
            else:
                sheet1.write(9, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(9, 2, 'Platform column contains other than the allowed values')
                #print('Platform column validation failed. Contains other values')
                #print(diff)

            # Non-numeric checks for Q1,Q2,Q3,Q4,Total
            Q1_mask = pd.to_numeric(target_df['2020_Q1'], errors='coerce').isna()
            Q1_non_numeric_values_count = Q1_mask.sum()
            if Q1_non_numeric_values_count == 0:
                sheet1.write(10, 1, 'PASS')
            else:
                sheet1.write(10, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(10, 2, '2020_Q1 contains ' + str(Q1_non_numeric_values_count) + ' values')
                #print('Number of non numeric values in 2020_Q1: ' + str(Q1_non_numeric_values_count))

            Q2_mask = pd.to_numeric(target_df['2020_Q2'], errors='coerce').isna()
            Q2_non_numeric_values_count = Q2_mask.sum()
            if Q2_non_numeric_values_count == 0:
                sheet1.write(11, 1, 'PASS')
            else:
                sheet1.write(11, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(11, 2, '2020_Q2 contains ' + str(Q2_non_numeric_values_count) + ' values')
                #print('Number of non numeric values in 2020_Q2: ' + str(Q2_non_numeric_values_count))

            Q3_mask = pd.to_numeric(target_df['2020_Q3'], errors='coerce').isna()
            Q3_non_numeric_values_count = Q3_mask.sum()
            if Q3_non_numeric_values_count == 0:
                sheet1.write(12, 1, 'PASS')
            else:
                sheet1.write(12, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(12, 2, '2020_Q3 contains ' + str(Q3_non_numeric_values_count) + ' values')
                #print('Number of non numeric values in 2020_Q3: ' + str(Q3_non_numeric_values_count))


            Q4_mask = pd.to_numeric(target_df['2020_Q4'], errors='coerce').isna()
            Q4_non_numeric_values_count = Q4_mask.sum()
            if Q4_non_numeric_values_count == 0:
                sheet1.write(13, 1, 'PASS')
            else:
                sheet1.write(13, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(13, 2, '2020_Q4 contains ' + str(Q4_non_numeric_values_count) + ' values')
                #print('Number of non numeric values in 2020_Q4: ' + str(Q4_non_numeric_values_count)))

            Total_mask = pd.to_numeric(target_df['Total '], errors='coerce').isna()
            Total_non_numeric_values_count = Total_mask.sum()
            if Total_non_numeric_values_count == 0:
                sheet1.write(14, 1, 'PASS')
            else:
                sheet1.write(14, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(14, 2, '2020_Q4 contains ' + str(Total_non_numeric_values_count) + ' values')
                #print('Number of non numeric values in 2020_Q4: ' + str(Total_non_numeric_values_count)))

            '''
            # -ve value Validation for Q1
            Q1_negative_df = target_df['2020_Q1'].where(target_df['2020_Q1'] < 0)
            Q1_negative_count = Q1_negative_df.count()
            if Q1_negative_count == 0:
                sheet1.write(15, 1, 'PASS')
            else:
                sheet1.write(15, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(15, 2, 'Q1 column contains '+ str(Q1_negative_count) + ' negative values')
                Q1_negative_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q1.csv',
                             index=True)


            # -ve value Validation for Q2
            Q2_negative_df = target_df['2020_Q2'].where(target_df['2020_Q2'] < 0)
            Q2_negative_count = Q2_negative_df.count()
            if Q2_negative_count == 0:
                sheet1.write(16, 1, 'PASS')
            else:
                sheet1.write(16, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(16, 2, 'Q2 column contains ' + str(Q2_negative_count) + ' negative values')
                Q2_negative_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q2.csv',
                             index=True)


            # -ve value Validation for Q3
            Q3_negative_df = target_df['2020_Q3'].where(target_df['2020_Q3'] < 0)
            Q3_negative_count = Q3_negative_df.count()
            if Q3_negative_count == 0:
                sheet1.write(17, 1, 'PASS')
            else:
                sheet1.write(17, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(17, 2, 'Q3 column contains ' + str(Q3_negative_count) + ' negative values')
                Q3_negative_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q3.csv',
                             index=True)


            # -ve value Validation for Q4
            Q4_negative_df = target_df['2020_Q4'].where(target_df['2020_Q4'] < 0)
            Q4_negative_count = Q4_negative_df.count()
            if Q4_negative_count == 0:
                sheet1.write(18, 1, 'PASS')
            else:
                sheet1.write(18, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(18, 2, 'Q4 column contains ' + str(Q4_negative_count) + ' negative values')
                Q4_negative_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q4.csv',
                             index=True)


            # -ve value Validation for Total
            Total_negative_df = target_df['Total '].where(target_df['Total '] < 0)
            Total_negative_count = Total_negative_df.count()
            if Total_negative_count == 0:
                sheet1.write(19, 1, 'PASS')
            else:
                sheet1.write(19, 1, 'FAIL')
                error_count = error_count + 1
                sheet1.write(19, 2, 'Total column contains ' + str(Total_negative_count) + ' negative values')
                Total_negative_df.to_csv(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Total.csv',
                             index=True)
            '''
            wb.save(str(output_file_path) + str(countryname) + '_Validation_Results.xls')

            if error_count == 0:
                email_status = 'Success'
            else:
                email_status = 'Failed'

            msg = MIMEMultipart()
            sender_email_addr = 'tennyfalcon444@gmail.com'
            receiver_email_list = ['tennyfalcon444@gmail.com', 'tennyson_paul@condenast.com']
            msg['From'] = sender_email_addr
            msg['To'] = ", ".join(receiver_email_list)
            msg['Subject'] = 'L2C - {0} Data Validation {1}'.format(countryname,email_status)
            root = os.path.dirname(os.path.abspath(__file__))
            templates_dir = os.path.join(root, 'templates')
            env = Environment(loader=FileSystemLoader(templates_dir))
            template = env.get_template('index.html')
            body = template.render(
                rev_type='Booked Revenue',
                date= date.today(),
                market= countryname,
                status= email_status,
                file_name = 'BookedRevenue_{0}'.format(countryname),
                job_name='Data Validation')
            msg.attach(MIMEText(body, 'html'))
            attachments = [(str(output_file_path) + str(countryname) + '_Validation_Results.xls')]
            if os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q1.csv'):
                attachments.append((str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q1.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q2.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q2.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q3.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q3.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q4.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Range_validation_Q4.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q1.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q1.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q2.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q2.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q3.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q3.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q4.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Q4.csv'))
            elif os.path.exists(str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Total.csv'):
                attachments.append(
                    (str(output_file_path) + 'BR_target_' + str(target_filename1) + 'Negative_Values_Total.csv'))

            for a_file in attachments:
                attachment = open(a_file, 'rb')
                file_name = os.path.basename(a_file)
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                part.add_header('Content-Disposition',
                                'attachment',
                                filename=file_name)
                encoders.encode_base64(part)
                msg.attach(part)

            # sends email

            smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
            smtpserver.starttls()

            # Authentication
            smtpserver.login(sender_email_addr, "Tenny@444")
            smtpserver.sendmail(sender_email_addr, receiver_email_list, msg.as_string())
            smtpserver.quit()
            print(str(countryname) + ' File Validation completed')




