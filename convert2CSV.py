import json
import csv

def lighthouse_json_to_csv(json_path, csv_path):
    # Load the Lighthouse JSON data
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract accessibility issues from the report
    accessibility_issues = data['categories']['accessibility']['auditRefs']
    
    # Prepare rows for CSV based on the extracted data
    rows = []
    for issue in accessibility_issues:
        audit_id = issue['id']
        audit_details = data['audits'][audit_id]
        
        # Extract relevant details
        description = audit_details.get('description', 'N/A')
        help_text = audit_details.get('helpText', 'N/A')
        score = audit_details.get('score', 'N/A')
        
        # Append issue data to rows
        rows.append({
            'Audit ID': audit_id,
            'Description': description,
            'Help Text': help_text,
            'Score': score
        })
    
    # Define the CSV columns
    columns = ['Audit ID', 'Description', 'Help Text', 'Score']
    
    # Write the data to a CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

# Example usage
lighthouse_json_to_csv('Insert path to the accessibilty report in json format', 'Inser path of where you want the CSV output of the script')

