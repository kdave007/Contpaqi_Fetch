from pathlib import Path
import sys
from datetime import datetime
sys.path.append(str(Path(__file__).parent.parent / 'src'))
from src.controllers.CSV_poliza_controller import CSVPolizaController
from src.controllers.poliza_filter_controller import PolizaFilterController

def main():
    # Initialize controller
    controller = CSVPolizaController()
    
    # Ask for the file name
    print("\nPresiona 'q' para salir en cualquier momento")
    while True:
        file_name = input("\nNombre de archivo (.txt): ").strip()
        
        # Check for exit command
        if file_name.lower() == 'q':
            print("\nSaliendo del programa...")
            sys.exit(0)
            
        if not file_name:
            print("Error: El nombre del archivo no puede estar vacío")
            continue
            
        # Ensure the file has .txt extension
        if not file_name.lower().endswith('.txt'):
            print("Error: El archivo debe ser .txt")
            continue
            
        # Look for the file in the same directory as the script
        file_path = Path(__file__).parent / file_name
        
        if not file_path.is_file():
            print(f"Error: Archivo '{file_name}' no encontrado")
            continue
            
        # If we reach here, we have a valid file
        break

    while True:
        print('\n1.- Convertir archivo completo')
        print('2.- Convertir solo folios especificos')
        action = input("--- Selecciona una acción: ").strip()
        
        if action == 'q':
            print("\nSaliendo del programa...")
            sys.exit(0)
            
        if action not in ['1', '2']:
            print("Error: Selecciona una opción válida (1 o 2)")
            continue
        break

    # If action 2, collect folios
    folios = []
    if action == '2':
        print("\nIngresa hasta 10 folios (presiona Enter sin escribir texto para terminar):")
        for i in range(10):
            folio = input(f"Folio {i+1}: ").strip()
            if not folio:
                break
            if folio == 'q':
                print("\nSaliendo del programa...")
                sys.exit(0)
            folios.append(folio)
        
        if not folios:
            print("Error: Debes ingresar al menos un folio")
            sys.exit(1)

    # Now process the file
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = Path(__file__).parent / f'output_polizas_aux_{timestamp}.csv'

        if action == '1':
            # Process all polizas
            controller.parse_file(file_path)
            controller.write_csv(output_path)
            print(f"\nArchivo creado: {output_path}")
        else:
            # Process only specific folios
            filter_controller = PolizaFilterController(str(file_path))
            success = filter_controller.filter_and_save(
                field="folio",
                references=folios,
                output_path=str(output_path)
            )
            
            if success:
                print(f"\nArchivo creado: {output_path}")
            else:
                print("\nAdvertencia: Algunos folios no fueron encontrados")


    except Exception as e:
        print(f"Error processing file: {e}")
        return

if __name__ == '__main__':
    main()