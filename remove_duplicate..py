from csv import DictReader,DictWriter
print(">> Using Python for Problem Statement")
print(">> Removing duplicates from sample_data.txt file and saving new\
 data in sample_data_no_dupicates.txt")

with open('sample_data.txt') as input_file, open('sample_data_no_dupicates.txt','w') as output_file:
    tsv_reader = DictReader(input_file,delimiter='\t')
    tsv_writer = DictWriter(output_file,delimiter='\t', lineterminator='\n',\
                            fieldnames=["Name","Age","Location"])
    tsv_writer.writeheader()
    existing_records_list =[]
    dup_records = []
    for row in tsv_reader:
        composite_key = (row['Name'], row['Age'])
        if composite_key in existing_records_list:
            dup_records.append({
                "Name":row["Name"],
                "Age": row["Age"],
                "Location": row["Location"]
            })
        else:
            existing_records_list.append(composite_key)
            tsv_writer.writerow({
                "Name":row['Name'],
                "Age": row['Age'],
                "Location":row['Location']
            })
    print(">> Removed Duplicates records are:")
    for i in dup_records:
        print(i)