import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / 'src'
sys.path.append(str(src_path))

from controllers.poliza_filter_controller import PolizaFilterController

def main():
    # Example input file - adjust path as needed
    input_file = "pólizas_check.txt"
    
    # Create controller
    controller = PolizaFilterController(input_file)
    
    # Example: Filter by folio
    folios_to_find = ["2121", "456","159","1011","1014","1015"]  # Replace with actual folios
    
    # Filter and save results
    output_file = "filtered_polizas.csv"
    success = controller.filter_and_save(
        field="folio",
        references=folios_to_find,
        output_path=output_file
    )
    
    # Print results
    if success:
        print(f"✅ All polizas found and saved to {output_file}")
        
        # Show what was found
        print("\nFound polizas:")
        results = controller.get_results()
        for row in results:
            if row[0] == 'CA':  # Header row
                print(f"\nPoliza: {row[3]}")  # folio is at index 3
            else:  # Movement row
                print(f"  Movement {row[1]}")
    else:
        print("❌ Some polizas were not found")
        
        # Show what was found anyway
        results = controller.get_results()
        if results:
            print("\nPartial results found:")
            found_folios = set()
            for row in results:
                if row[0] == 'CA':
                    found_folios.add(row[3])
            print(f"Found folios: {found_folios}")
            print(f"Missing folios: {set(folios_to_find) - found_folios}")
        else:
            print("No matching polizas found")

if __name__ == "__main__":
    main()
