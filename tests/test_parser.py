import sys
import json
from pathlib import Path

# Add the src directory to the Python path
src_dir = Path(__file__).parent.parent / 'src'
sys.path.append(str(src_dir))

from controllers.poliza_controller import PolizaController


def main():
    # Initialize the controller
    controller = PolizaController()
    
    # Path to the test poliza file
    file_path = Path(__file__).parent.parent / 'prueba_poliza.txt'
    
    print("Reading file:", file_path)
    print("-" * 80)
    
    # Parse the file
    controller.parse_file(file_path)
    
    # Convert to dictionary and print as JSON
    polizas = controller.to_dict()
    print(json.dumps(polizas, indent=2, ensure_ascii=False))
    
    # Print some stats
    print("\nStats:")
    print(f"Total polizas found: {len(polizas)}")
    print(f"Total movements: {sum(p['total_movements'] for p in polizas)}")


if __name__ == '__main__':
    main()
