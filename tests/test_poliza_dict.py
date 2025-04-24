import sys
import json
from pathlib import Path

# Add the src directory to the Python path
src_dir = Path(__file__).parent.parent / 'src'
sys.path.append(str(src_dir))

from controllers.poliza_controller import PolizaController


def print_poliza(poliza_dict):
    # Print header fields
    print('Header Fields:')
    for key, value in poliza_dict.items():
        if key != 'parts':
            print(f"  {key}: {value}")
    
    # Print movements
    print('\nMovements:')
    if 'parts' in poliza_dict:
        for mov_num, movement in poliza_dict['parts'].items():
            print(f"\n{mov_num}. Movement:")
            for key, value in movement.items():
                if key == 'debe' and value:
                    print(f"  {key}: ${float(value):.2f}")
                elif key == 'haber' and value:
                    print(f"  {key}: ${float(value):.2f}")
                else:
                    print(f"  {key}: {value}")
    else:
        print("  No movements found")


def main():
    # Initialize controller
    controller = PolizaController()
    
    # Get the path to the test file
    file_path = Path(__file__).parent.parent / 'prueba_poliza.txt'
    print(f"Reading file: {file_path}")
    print('-' * 80)
    
    # Parse the file
    controller.parse_file(file_path)
    
    # Get all polizas
    polizas = controller.to_dict()
    total_movements = sum(len(p.get('parts', {})) for p in polizas.values())
    
    print(f"Found {len(polizas)} polizas")
    print(f"Total movements: {total_movements}")
    print('\n')
    
    while True:
        print("Options:")
        print("1. Show all polizas")
        print("2. Show specific poliza")
        print("3. Show raw JSON")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            for num, poliza in polizas.items():
                print(f"\nPoliza #{num}:")
                print('-' * 80)
                print_poliza(poliza)
        
        elif choice == '2':
            num = int(input("Enter poliza number: "))
            if num in polizas:
                print(f"\nPoliza #{num}:")
                print('-' * 80)
                print_poliza(polizas[num])
            else:
                print("Invalid poliza number")
        
        elif choice == '3':
            print(json.dumps(polizas, indent=2))
        
        else:
            print("Invalid choice")
            continue
        
        break


if __name__ == '__main__':
    main()
