from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent / 'src'))
from controllers.CSV_poliza_controller import CSVPolizaController

def main():
    # Initialize controller
    controller = CSVPolizaController()
    
    # Get the path to the test file (same as your JSON test)
    file_path = Path(__file__).parent.parent / 'pólizas_ING.txt'
    print(f"Reading file: {file_path}")
    print('-' * 80)
    
    # Parse the file
    controller.parse_file(file_path)
    
    # Write to CSV file
    output_path = Path(__file__).parent.parent / 'output_polizas_aux.csv'
    controller.write_csv(output_path)
    
    print(f"\nCSV file written to: {output_path}")
    
    # Show first few lines of the CSV
    print("\nFirst few lines of CSV:")
    print('-' * 80)
    with open(output_path, 'r') as f:
        for i, line in enumerate(f):
            if i < 5:  # Show first 5 lines
                print(line.strip())
            else:
                break
    
if __name__ == '__main__':
    main()